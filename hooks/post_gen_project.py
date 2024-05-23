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
        remove_file('mkdocs.yml')

    if include_cli == 'n':
        remove_file(cli_path)

    # install hooks
    subprocess.run(['pre-commit', 'install'])

    # import os
    import shutil

    # Get the current directory path
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the parent directory path
    parent_dir = os.path.dirname(current_dir)

    # Move the generated files to the parent directory
    for item in os.listdir(current_dir):
        if item != '__pycache__':
            shutil.move(os.path.join(current_dir, item), parent_dir)