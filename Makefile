install:
	uv sync

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi

tests:
	uv run coverage run manage.py test