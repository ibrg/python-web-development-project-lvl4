runserver:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test tests

lint:
	poetry run python -m flake8 task_manager
