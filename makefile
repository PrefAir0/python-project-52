install:
	uv pip install --system -r pyproject.toml

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --no-input

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi