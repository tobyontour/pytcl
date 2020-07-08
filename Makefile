# python3 -m unittest tests.test_set.TestSetCommand.test_simple_set_script_string

test:
	python3 -m unittest discover -s tests

fast:
	python3 -m unittest discover -s tests -f

coverage: venv
	venv/bin/coverage run -m unittest discover
	venv/bin/coverage report -m
	venv/bin/coverage html

chrome:
	google-chrome htmlcov/index.html

venv:
	virtualenv --python=python3 venv
	venv/bin/pip install -r requirements.txt
