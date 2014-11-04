PYTHON=python
.PHONY: migrate runserver test test-strict pytest flakes flake8

migrate:
	$(PYTHON) ./withenv.py manage.py migrate

runserver:
	$(PYTHON) ./withenv.py manage.py runserver

test: pytest flakes

test-strict: pytest flake8

pytest:
	$(PYTHON) ./withenv.py py.test

flakes:
	$(PYTHON) ./withenv.py pyflakes coopbox_base

flake8:
	$(PYTHON) ./withenv.py flake8 coopbox_base

clean:
	find -name '*.pyc' -delete
	find -name '*.pyo' -delete
	find -name '__pycache__' -type d -delete
