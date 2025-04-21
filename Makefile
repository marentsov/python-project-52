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
		uv run manage.py collectstatic --no-input
migrations:
		uv run manage.py makemigrations
migrate:
		uv run manage.py migrate
makemessages:
		django-admin makemessages --ignore="static" --ignore=".env"  -l ru
compilemessages:
		django-admin compilemessages

