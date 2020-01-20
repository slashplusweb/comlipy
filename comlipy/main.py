import sys

import click
from .lib.config import Config
from .lib.parser import Parser
from .lib.validator import Validator
from .lib.messages import Messages


@click.command()
@click.argument('message')
@click.option('-c', '--config', 'config_file_path', default=None, help='path to the config file (.yml)')
# @click.option('-q', '--quiet', 'is_quiet', default=None, help='Toggle console output')
def cli(message, config_file_path):
    # get the config
    config = Config(config_file_path)
    parser = Parser(message)

    # init message system
    messages = Messages(parser, config)

    # validate all parts of the message in accordance with the given config
    validator = Validator(config, parser, messages)
    validator.validate()

    messages.show()
    if messages.contains_error():
        exit(1)
