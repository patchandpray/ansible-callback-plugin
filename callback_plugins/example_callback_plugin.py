# written for python2.7
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import requests
from requests.auth import HTTPBasicAuth

from ansible.plugins.callback import CallbackBase
from ansible import constants as C
from __main__ import cli

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

DOCUMENTATION = '''
    callback: example_callback_plugin
    type: notification
    short_description: Send callback on various runners to an API endpoint.
    description:
      - On ansible runner calls report state and task output to an API endpoint.
      - Configuration via callback_config.ini, place the file in the same directory 
        as the plugin.
    requirements:
      - python requests library
      - HTTPBasicAuth library from python requests.auth
      - ConfigParser for reading configuration file
    '''

class CallbackModule(CallbackBase):

    '''
    Callback to API endpoints on ansible runner calls.
    '''

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'notification'
    CALLBACK_NAME = 'example_callback_plugin'

    def __init__(self, *args, **kwargs):
        super(CallbackModule, self).__init__()

    def v2_playbook_on_start(self, playbook):
        self.playbook = playbook

    def v2_playbook_on_play_start(self, play):
        self.play = play
        self.extra_vars = self.play.get_variable_manager().extra_vars
        self.callback_url = self.extra_vars['callback_url']
        self.username = self.extra_vars['username']
        self.password = self.extra_vars['password']

        print('\nExtra vars that were passed to playbook are accessible to the callback plugin by calling the variable_manager on the play object for the method v2_playbook_on_play_start:\nextra_vars: {0}'.format(self.extra_vars))

    def v2_runner_on_ok(self, result):
        payload = {'state': 'success',
                   'task_name': result.task_name,
                   'task_output' : result._result
                  }
        print('On a succesfull task - Sending to endpoint:\n{0}\n'.format(requests.post(self.callback_url, auth=(self.username,self.password), data=payload).json()))
        pass

    def v2_runner_on_failed(self, result, ignore_errors=False):
        payload = {'state': 'failed',
                   'task_name': result.task_name,
                   'task_output' : result._result['msg']
                  }
        
        print('On a failed task - Sending to endpoint:\n{0}\n'.format(requests.post(self.callback_url, auth=(self.username,self.password), data=payload).json()))
        pass
        
