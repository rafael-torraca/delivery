# clean nao remove pastas no wsl2 windows.
clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	pip install -e .['dev'] --upgrade --no-cache

uninstall:
	pip uninstall delivery


install:
	pip install -e .['dev']


test:
	pytest tests -v --cov=delivery

# parte que eu coloquei
developer:
	export FLASK_APP=delivery/app.py
	export FLASK_ENV=development