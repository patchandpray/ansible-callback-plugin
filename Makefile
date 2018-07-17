.PHONY: run
run:
	python api_server/server.py

.PHONY: list
list:
	curl -X GET http://127.0.0.1:5000/tasks -v
	
.PHONY: post
post:
	curl -u admin:password -X POST http://127.0.0.1:5000/tasks -d "task_name=test" -d "task_output=test_output" -d "state=failed" -v
	`
.PHONY: playbook
playbook:
	ansible-playbook playbook.yml -e callback_url="http://127.0.0.1:5000/tasks" -e username=admin -e password=password
