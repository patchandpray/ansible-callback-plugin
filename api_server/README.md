# mock-server for callback plugin testing

## Configure the server

Using the server\_config.ini file placed next to the server.py python file

### configuration parameters
host = the ip address the server should serve from - default: 0.0.0.0
port = the port the server should server from - default: 5000
user = the username for basic auth - default: admin
password = the password for basic auth - default: password

## To run the server

setup python virtualenv `virtualenv env`
install requirements `pip install -r requirements.txt`
source virtual env `source env/bin/activate`
run the mock server using `make run`

### available functions

post using `make post` (requires auth)

list using `make list`
