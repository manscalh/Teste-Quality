# Install Linux

* open new terminal in project root folder
* delete .venv if already exists
* install new venv: python3 -m venv .venv
* activate venv:  source .venv/bin/activate
* install dependencies: pip install -r requirements.txt
* to execute all tests run: python3 -m unittest  -v tests/Test*.py

# Install Windows

* open new terminal in project root folder
* delete .venv if already exists
* install new venv: python -m venv .venv
* activate venv:  .\.venv\Scripts\activate
* install dependencies: pip install -r requirements.txt
* to execute all tests: python -m unittest  -v tests/Test*.py