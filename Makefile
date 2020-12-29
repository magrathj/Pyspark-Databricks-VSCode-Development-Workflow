setup:
	python3 -m venv ~/.myrepo

install:
	pip install --upgrade pip &&\
		pip install --user -r requirements.txt

test:
	python -m pytest 


all: install test