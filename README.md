# ANSIBLE CALLBACK PLUGIN

This repository shows how to use a custom ansible callback plugin to send the output 
of every task to an API endpoint.

The plugin will record the play and upon detecting a succesfull or failed task will be triggered to store the output of that task and send it using the python requests module to an API endpoint.

Configuration of the plugin will occur via plugin\_config.ini to be placed next to the plugin itself.

We will be using a mock api server to be found in the api\_server directory to handle the requests that we send to it to demonstrate the working of the callback plugin.

## Configuration parameters

It is possible to expose configuration parameters to the callback plugin as extra\_vars or from playbook variables.

- API Endpoint url
- username
- password

[extra\_vars]
callback\_url = the api endpoint callback url
username = the username for api authentication
password = the password for api authentication

## Outputs

For tasks the current payload is sent to the API backend

state = success or failed  
task\_name = the name of the task that was succesfull or failed  
task\_output = the output of the task  

## How it works

The custom ansible callback plugin is to be placed in a directory called callback\_plugins in the directory where the playbook is run from.
In the ansible.cfg file specify the custom callback\_plugins directory:
[defaults]  
callback\_plugins = ./callback\_plugins

Every callback plugin there of type notification will be picked up and run for all the runner calls it is configured for.

The plugin will make use of the python requests library to send the captured payload from a runner call as payload to a configured API endpoint. HTTPBasicAuth is supported for simulating calls that require API authentication.

For simulating the API endpoint a small server is implemented using Flask and flask\_restfull, this can be found in the api\_server directory.

All default available callback\_plugins can be found in your ansible install location, usually `/usr/lib/python2.7/site-packages/ansible/plugins/callback`

## How to run

Be sure to have the api\_server provided running or have your own API endpoint available which supports the fields {'state, 'task\_name', task\_output'}

Using the provided api\_server:
* `python3 -m venv env` or `virtualenv env` (for python2.x)
* `source env/bin/activate`
* `pip install -r requirements.txt`
* optionally configure api server defaults in server\_config.ini
* `make run`

### Using Makefile
`make playbook`  
You might have to change the extra vars passed for that makefile target to fit your configuration.

### Manual
`ansible-playbook playbook.yml -e callback_url=<http://api_host:port/tasks> -e username=<basic_auth_username> -e password=<basic_auth_password>`
