# cookiecutter-pypackage-minimal
Just pre-commit formatting, pytest, and mkdocs. (I am scared of tox)

Loosely based on https://waynerv.github.io/cookiecutter-pypackage/ with only the bare minimum necessary for Python dev work.

## Features
- poetry build system
- pre-commit hooks with flake8, black, and isort formatting (not optional)
- mkdocs for anything in `docs/` (optional)
- pytest (optional)
- CLI with Click (optional) 
- TODO mkdocstrings (optional)
- TODO switch to ruff
- TODO add github tags

## Usage

Make your repo on Github first, and clone it locally. Then:
- `pip install cookiecutter`
- `cookiecutter https://github.com/wllgrnt/cookiecutter-pypackage-minimal.git`
