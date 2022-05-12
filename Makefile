install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv test/test_hello.py
format:
	black src/python-pytest/*.py

lint:
	pylint --disable=C $$(git ls-files 'src/*.py')

all: install lint test format
