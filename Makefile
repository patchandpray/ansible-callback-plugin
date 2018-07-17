run:
	python api_server/server.py
list:
	curl -X GET http://127.0.0.1:5000/tasks -v
post:
	curl -u admin:password -X POST http://127.0.0.1:5000/tasks -d "task_name=test" -d "task_output=test_output" -d "state=failed" -v
playbook:
	ansible-playbook playbook.yml -e test_var=testtest
