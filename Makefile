all:
	@echo "Targets: test, deps, check_images, find_nonimage_work"

test: img
	python util/server.py

img:
	scons img

deps:
	pip install -U flask
	pip install -U pygments
	pip install -U jinja2_highlight
	pip install -U mistune
	#pip install -U scons
	pip install -U taschenmesser

check_images:
	python util/check_images.py

find_nonimage_work:
	find work -type f | grep -v "png" | grep -v "jpg" | grep -v "svg"

clean:
	rm -rf ./static/img/docs/gen/*
	rm -rf ./static/img/iotcookbook/gen/*
