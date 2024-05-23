"""Console script for {{cookiecutter.pkg_name}}."""

{% if cookiecutter.include_cli == "click" %}
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