env:
	@. ./py3/bin/activate


update_req:
	pip freeze > requirements.txt

migrate_servies:
	cd geohub_project
	python manage.py makemigrations services

migrate:
	cd geohub_project
	python manage.py migrate

.ONESHELL: migrate migrate_servies