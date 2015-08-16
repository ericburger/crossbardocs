test:
	python util/server.py

find_images:
	python util/find.py

deps:
	pip install -U flask
	pip install -U pygments
	pip install -U jinja2_highlight
	pip install -U mistune
