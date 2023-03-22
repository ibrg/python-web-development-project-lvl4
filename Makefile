runserver:
	gunicorn task_manager/task_manager/wsgi.py

dev:
	poetry run python task_manager/manage.py runserver

