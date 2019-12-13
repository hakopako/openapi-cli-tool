
test:
	python -m unittest discover -v -s tests/unit -p "test_*.py"


build:
	python setup.py install

clean:
	find ./ -name "*.pyc"  -exec rm {} \;
