install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src/mylib tests/*.py

profile-test:
	python -m pytest -vv --durations=1 --durations-min=1.0 --cov=src/mylib tests/*.py

parallel-test:
	python -m pytest -vv -n auto --dist loadgroup tests/*.py

format:
	black $$(git ls-files '*.py')

lint:
	pylint --disable=C $$(git ls-files '*.py')

all: install lint test format
