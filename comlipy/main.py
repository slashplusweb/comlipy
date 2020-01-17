import click
from .lib.parser import Parser


@click.command()
@click.argument('message')
def cli(message):
    click.echo('demo 1234 ')
    Parser(message)
