import sys
from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask_httpauth import HTTPBasicAuth

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

app = Flask(__name__)
auth = HTTPBasicAuth()
api = Api(app)


# api in memory endpoints
tasks = {
        '1': {'task_name': 'sometask',
              'task_output': 'I have failed',
              'state': 'failed'}
        }
    

# parser configuration for POST request
parser = reqparse.RequestParser()
parser.add_argument('task_name')
parser.add_argument('task_output')
parser.add_argument('state')

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

class TaskList(Resource):
    def get(self):
        return tasks
    
    @auth.login_required
    def post(self):
        args = parser.parse_args()
        task_id = str(len(tasks.keys()) + 1)
        tasks[task_id] = {'task_name': args['task_name'],
                          'task_output': args['task_output'],
                          'state': args['state']}
        print(task_id)
        print(tasks[task_id])
        return tasks[task_id], 201

api.add_resource(TaskList, '/tasks')

if __name__ == "__main__":

    config = configparser.ConfigParser()
    config_file = ('server_config.ini')

    try:
        open('server_config.ini', 'r')
    except Exception as err:
        print('Error: {0}\n Unable to get read file {1}.'.format(err, config_file))
        sys.exit(1)
        
    config.read(config_file)

    # defaults
    host = config.get('defaults', 'host')
    port = config.get('defaults', 'port')
    debug_enabled = config.get('defaults', 'debug_enabled')

    # auth
    username = config.get('auth', 'username')
    password = config.get('auth', 'password')
    users = {
            username: password
            }

               
    # start up the server
    app.run(debug=debug_enabled, host=host, port=port) 
