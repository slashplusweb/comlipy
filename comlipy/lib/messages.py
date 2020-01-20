from termcolor import colored

from .parser import Parser
from .config import Config


class Messages:
    ICON_ERROR = '✖'
    ICON_WARNING = '⚠'
    ICON_SUCCESS = u"\xE2\x9C\x93"  # check (UTF-8)
    ICON_HELP = 'ⓘ'
    ICON_INFO = 'ℹ'
    ICON_HOURGLASS = '⧗'

    def __init__(self, parser: Parser, config: Config):
        self._messages = {}
        self._parser = parser
        self._config = config

    def add_rule_result(self, message: str, level: int):
        self._messages.setdefault(level, []).append(message)

    def show(self):
        if self.__is_problem():
            self.print_info()
            self.print_rules()
            self.print_summary()
            self.print_help()

    def __is_problem(self):
        problem_levels = {1, 2}
        return bool(self._messages.keys() & problem_levels)

    def print_info(self):
        header = self._parser.header

        if header is not None:
            icon = colored(self.ICON_INFO, 'grey')
            header = colored(header, attrs=['bold'])
            print('{}    input: {}'.format(icon, header))

    def print_help(self):
        help_string = self._config.get_setting('global_help')

        if help_string is not None:
            print('    '.join(filter(None, [self.ICON_HELP, str(help_string)])))

    def print_rules(self):
        for level, messages in self._messages.items():
            for message in messages:
                self.__print(message, level)

    def print_rule_by_level(self, level):
        for message in self._messages[level]:
            self.__print(message, level)

    def print_summary(self):

        messages = self._messages
        warnings = messages[1] if 1 in messages else []
        errors = messages[2] if 2 in messages else []

        summary = colored('found {} problems, {} warnings'.format(len(errors), len(warnings)), attrs=['bold'])
        icon = colored(self.ICON_ERROR, 'red') if len(errors) > 0 else colored(self.ICON_WARNING, 'yellow')

        print('\n{}    {}'.format(icon, summary))

    def __print(self, message, level):
        icon = None

        if level == 0:
            return
        elif level == 1:
            icon = colored(self.ICON_WARNING, 'yellow')
        elif level == 2:
            icon = colored(self.ICON_ERROR, 'red')
            message = colored(message, attrs=['bold'])
        elif level == 3:
            icon = colored(self.ICON_SUCCESS, 'green')
        else:
            TypeError('Unknown level `{}`'.format(level))

        print('    '.join(filter(None, [icon, str(message)])))
