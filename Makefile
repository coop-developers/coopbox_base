PYTHON=python
.PHONY: all runserver test check

all:
	$(PYTHON) ./withenv.py -N

runserver:
	$(PYTHON) ./withenv.py manage.py runserver

test: check
	$(PYTHON) ./withenv.py py.test

check:
	# flakes

clean:
	find -name '*.pyc' -delete
	find -name '*.pyo' -delete
	find -name '__pycache__' -type d -delete
