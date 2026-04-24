.PHONY: 

install lint test run-api run-dashboard train generate

install:
	pip install -r requirements.txt

lint:
	ruff check src/ tests/
	ruff format --check src/ tests/

test:
	pytest

run-api:
	uvicorn isat_pipeline.api.main:app --reload --port 8000

run-dashboard:
	streamlit run dashboard/app.py

generate:
	python generator/generate.py --n 5000 --output data/raw/

train:
	jupyter nbconvert --to notebook --execute notebooks/train_model.ipynb`