import os
import shutil
import subprocess

include_pytest = '{{ cookiecutter.include_pytest }}'
include_mkdocs = '{{ cookiecutter.include_mkdocs }}'
include_cli = '{{ cookiecutter.include_cli }}'

docs_path = 'docs'
tests_path = 'tests'
cli_path = os.path.join('src', '{{ cookiecutter.package_name }}', 'cli.py')

# Function to remove directories
def remove_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)

# Function to remove files
def remove_file(path):
    if os.path.exists(path):
        os.remove(path)

if __name__ == "__main__":
    # Remove directories or files based on user input
    if include_pytest == 'n':
        remove_directory(tests_path)

    if include_mkdocs == 'n':
        remove_directory(docs_path)

    if include_cli == 'n':
        remove_file(cli_path)

    # install hooks
    subprocess.run(['pre-commit', 'install'])