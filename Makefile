runserver:
	poetry run gunicorn task_manager.task_manager.wsgi:application

dev:
	poetry run python task_manager/manage.py runserver

