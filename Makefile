install:
	poetry install

study:
	poetry run uvicorn app.main:app

dev:
	poetry run fastapi dev app/main.py

test-unit:
	poetry run pytest -v app/test/unit

lint:
	poetry run flake8 app