.PHONY: install lint test run-api run-dashboard train generate flow docker-build compose-up

install:
	pip install -r requirements.txt

lint:
	ruff check src tests
	ruff format --check src tests

test:
	pytest

run-api:
	uvicorn src.isat_pipeline.api.main:app --reload --port 8000

run-dashboard:
	streamlit run dashboard/app.py

generate:
	python generator/generate.py --n 5000 --output data/raw/

flow:
	python -m src.isat_pipeline.orchestrator

docker-build:
	docker build -t isat-pipeline:latest .

compose-up:
	docker compose up --build
