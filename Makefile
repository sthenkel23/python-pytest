install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src/mylib tests/*.py

format:
	black src/mylib/*.py

lint:
	pylint --disable=C $$(git ls-files 'src/*.py')

all: install lint test format
