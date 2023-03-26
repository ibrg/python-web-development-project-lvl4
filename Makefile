runserver:
	poetry run python manage.py migrate
	poetry run gunicorn --env DJANGO_SETTINGS_MODULE=task_manager.settings --chdir task_manager task_manager.wsgi

test:
	poetry run python manage.py test tests

lint:
	poetry run python -m flake8 task_manager
