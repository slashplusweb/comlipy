import click
from .lib.parser import Parser


@click.command()
def cli():
    click.echo('demo 1234 ')
    Parser()
