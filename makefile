install:
	uv pip install --system -r pyproject.toml

migrate:
	python manage.py migrate

collectstatic:
	python manage.py collectstatic --no-input

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi