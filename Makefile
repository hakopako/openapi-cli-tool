
test:
	python -m unittest discover -v -s tests

build:
	python setup.py install

clean:
	find ./ -name "*.pyc"  -exec rm {} \;
