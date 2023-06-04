- remove pkg package
- test: failed


- python setup.py install
- test: success


- remove pkg package
- pip install build
- python -m build
- test

- pip freeze > requirements.txt

- can pip install auto-update toml and requirements.txt?
