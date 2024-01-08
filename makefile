init:
	python -m venv .env
	sudo su
	.env/bin/activate
	python -m pip install -r requirements.txt
#	mkdir -p /tmp/workspace/pyalb_env
#	cp -r .env /tmp/workspace/pyalb_env/
	echo "Installation complete!"

lint:
	.env/bin/activate
	python -m pylint pyalb/
	echo "Linting complete!"

test:
	.env/bin/activate
	python -m pytest
	echo "Testing complete!"

build:
	python -m pip install build
	mkdir -p /tmp/workspace/artifacts
	python -m build -o /tmp/workspace/artifacts

release:
	echo "Creating release.."
	ls -la /tmp/workspace/artifacts