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
- validate certs


[inputs]
callback\_url = the api endpoint callback url
username = the username for api authentication
password = the password for api authentication

## Output configuration

Ideally an arbitrary number of output parameters can be configured by using an external configuration file.

[outputs]  
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

### Using Makefile

### Manual setup
