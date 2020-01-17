import click
from .lib.parser import Parser


@click.command()
@click.argument('message')
@click.option('-c', 'config_path', default='./', help='Path to the configuration file (.yml)')
def cli(message, config_path):
    click.echo(config_path)
    Parser(message)
