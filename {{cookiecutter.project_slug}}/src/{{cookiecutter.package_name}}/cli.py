"""Console script for {{cookiecutter.package_name}}."""

{% if cookiecutter.include_cli == "y" %}
import click


@click.command()
def main():
    """Main entrypoint."""
    click.echo("{{ cookiecutter.project_slug }}")
    click.echo("=" * len("{{ cookiecutter.project_slug }}"))
    click.echo("{{ cookiecutter.project_short_description }}")


if __name__ == "__main__":
    main()
    
{% endif %}