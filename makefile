init:
	python -m pip install -r requirements.txt
	echo "Installation complete!"

lint:
	python -m pylint pyalb/
	echo "Linting complete!"

test:
	python -m pytest
	echo "Testing complete!"