# cookiecutter-pypackage-minimal
Just pre-commit formatting, pytest, and mkdocs. (I am scared of tox)

Loosely based on https://waynerv.github.io/cookiecutter-pypackage/ with only the bare minimum necessary for Python dev work, because I do not want to have to think about Python packaging config ever again.

## Features
- poetry build system
- pre-commit hooks with flake8 and black
- code in a `src` folder
- mkdocs in a `docs` folder (optional)
- pytest in a `tests` folder (optional)
- CLI with Click (optional) 

## Usage


### Installation
Make your repo on Github first, and clone it locally. Then:
- `pip install cookiecutter`
- `cookiecutter https://github.com/wllgrnt/cookiecutter-pypackage-minimal.git`

Note: this will install pre-commit as part of the installation process. It will also unpack itself into whatever directory you are currently in, **overwriting any existing files with the same names**.


The package is installed with `pip install . ` or `poetry install` from the repo root. To include the dev dependencies, use:

`poetry install --extras "dev"` or `pip install '.[dev]'`

(pyproject.toml doesn't use the newest pyproject.toml syntax or poetry 'with' syntax to maintain pip installability)

Remember to run `pre-commit install` before commiting new code.

### Testing
Run `pytest` from the repo root.

### Docs
After installing the package, run `mkdocs serve` from the repo root. Docs will be served at localhost:8000.

### CLI
Whatever you decide to call your package, an executable with that name will be added to your PATH, which runs `cli.py:main()`. This can be configured using Click.
