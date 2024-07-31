

start:
	python main.py $(args)

list:
	python list.py

add:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt