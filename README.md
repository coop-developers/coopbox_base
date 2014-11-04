Coop in a Box
==============

## Quick Start
To get a dev environment setup, simply run the following:

```
make
make runserver
```

If you're using windows, have Python 2.7 installed, pip (https://pip.pypa.io/en/latest/installing.html) and virtualenv (pip install virtualenv), open cmd and do the following:
```
cd <path to project>
withenv.py python manage.py migrate
withenv.py python manage.py runserver
```

You can then visit the development version of the site at http://127.0.0.1:8000/

## Coding Style
Use 4-spaces indentation for each relevant file.  If you're using a supporting editor, install an EditorConfig plugin (see http://editorconfig.org/).  This will ensure your code have the correct indentation and line-ending.

Follow PEP-8 (http://legacy.python.org/dev/peps/pep-0008/) and PEP-257 (http://legacy.python.org/dev/peps/pep-0257/) as much as possible.  Use the following command to check conformance:

```
make flake8
```

## Testing
Please do both unit tests and integration tests when you have time.  We're using pytest-django. See http://pytest-django.readthedocs.org/en/latest/ for documentation

Before each commit, make sure you run the following

```
make test
```

This will run all existing test cases and ensure that basic python styles are followed for all Python code.  Run the following if you're a code purist in pursuit of PEP-8 conformance:

```
make test-strict
```

## Troubleshooting
Does any command not work?  Try `make clean` first!

If that still doesn't work, contact us or file an issue.

## Windows Developers
Python is in general quite Windows friendly. However, due to its simplicity, we're using Make to record command test/development commands.  Before we decide to move the whole lot into a Python-based solution however, please peek into `Makefile`, and copy-paste the corresponding snippets of code in `Makefile` into your cmd, with the `$(PYTHON)` part replaced with `python`.
