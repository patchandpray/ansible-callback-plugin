# mock-server for callback plugin testing

## Configure the server

Using the server\_config.ini file

### configuration parameters
host = the ip address the server should serve from - default: 0.0.0.0
port = the port the server should server from - default: 5000
user = the username for basic auth - default: admin
password = the password for basic auth - default: password

## To run the server

* `python3 -m venv env` or `virtualenv env` (for python2.x)
* `source env/bin/activate`
* `pip install -r requirements.txt`
* optionally configure api server defaults in server\_config.ini
* `make run`

### available functions

* post using `make post` (requires auth)
* list using `make list`
