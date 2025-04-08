dev:
		uv run manage.py runserver
build:
		./build.sh
render-start:
		gunicorn task_manager.wsgi
lint:
		uv run ruff check
lint-fix:
		uv run ruff check --fix
install:
		uv sync
collectstatic:
		manage.py collectstatic --no-input
migrate:
		manage.py migrate