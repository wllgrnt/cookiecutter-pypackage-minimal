import os
import shutil
import subprocess
import sys

include_pytest = "{{ cookiecutter.include_pytest }}"
include_mkdocs = "{{ cookiecutter.include_mkdocs }}"
include_cli = "{{ cookiecutter.include_cli }}"

docs_path = "docs"
tests_path = "tests"
cli_path = os.path.join("src", "{{ cookiecutter.package_name }}", "cli.py")


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
    if include_pytest == "n":
        remove_directory(tests_path)

    if include_mkdocs == "n":
        remove_directory(docs_path)
        remove_file("mkdocs.yml")

    if include_cli == "n":
        remove_file(cli_path)

    # install hooks
    if os.path.exists(".git"):
        subprocess.run(["pip", "install", "pre-commit"])
        subprocess.run(["pre-commit", "install"])

    # unpack the template into the parent dir
    current_dir = os.getcwd()
    parent_dir = os.path.dirname(current_dir)
    will_overwrite = False
    items = []
    for item in os.listdir(current_dir):
        if item != "__pycache__" and os.path.exists(os.path.join(parent_dir, item)):
            items.append(item)
            will_overwrite = True

    if will_overwrite:
        print("Moving the generated files to the parent directory will overwrite existing files:")
        for item in items:
            print(f"\t{item}")
        confirm = ' '
        while confirm not in ['y', 'n']:
            confirm = input("Do you want to proceed? (y/n): ")
        
        if confirm.lower() != "y":
            print("Aborted moving files to avoid overwriting.")
            sys.exit(1)

    # Move the generated files to the parent directory
    for item in os.listdir(current_dir):
        if item != "__pycache__":
            shutil.move(os.path.join(current_dir, item), os.path.join(parent_dir, item))

    os.rmdir(current_dir)
