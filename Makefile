install:
	poetry install

dev:
	poetry run uvicorn main:app

test:
	poetry run pytest -v app/test/

lint:
	poetry run flake8 app