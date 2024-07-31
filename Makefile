

start:
	python main.py $(args)

list:
	python list.py

describe:
	python describe.py $(args)

add:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt