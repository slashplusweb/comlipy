import sys

import click

from comlipy.lib.config import Config
from comlipy.lib.messages import Messages
from comlipy.lib.parser import Parser
from comlipy.lib.validator import Validator
from comlipy.lib.install import *

COMLIPY_VERSION = '1.2.0'


@click.command()
@click.argument('message')
@click.option('-c', '--config', 'config_file_path', default=None, help='Path to the config file (.yml)')
@click.option('-q', '--quiet', 'is_quiet', default=False, is_flag=True, help='Toggle console output')
@click.option('-m', '--monochrome', 'is_mono', default=False, is_flag=True, help='Toggle monochrome output')
@click.option('-v', '--verbose', 'is_verbose', default=False, is_flag=True,
              help='Enable verbose output (also print hidden & success messages)')
@click.version_option(version=COMLIPY_VERSION)
def cli(message, config_file_path, is_quiet, is_mono, is_verbose):
    # get the config
    config = Config(config_file_path)

    # parse the commit message
    parser = Parser(message)

    # init message system
    messages = Messages(parser, config)

    # validate all parts of the message in accordance with the given config
    validator = Validator(config, parser, messages)
    validator.validate()

    if not is_quiet:
        messages.show(is_mono, is_verbose)
    if validator.is_error():
        sys.exit(1)

    sys.exit(0)

@click.command()
@click.option('-c', '--config', 'config_file_path', default=None, help='Path to the config file (.yml)')
@click.version_option(version=COMLIPY_VERSION)
def install(config_file_path):
    run_path = os.getcwd()
    git_path = detect_git_path(run_path)

    if not git_path:
        Color.print('Git path not found: {!r}'.format(run_path))
        sys.exit(1)
    render_commit_hook(git_path, config_file_path)



if __name__ == '__main__':
    cli()
