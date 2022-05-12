install:
	pip install -upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv test/test_hello.py
format:
	black *.py

lint:
	pylint hello.py

all: install lint test format