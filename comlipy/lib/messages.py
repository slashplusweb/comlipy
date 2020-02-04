from typing import List

from .color import Color
from .config import Config
from .parser import Parser


class Messages:
    ICON_ERROR = '✖'
    ICON_WARNING = '⚠'
    ICON_SUCCESS = '✓'
    ICON_HELP = 'ⓘ'
    ICON_INFO = 'ℹ'
    ICON_HOURGLASS = '⧗'

    def __init__(self, parser: Parser, config: Config):
        self._messages = {}
        self._parser = parser
        self._config = config
        self._is_mono = False
        self._is_verbose = False

    def add_rule_result(self, message: str, level: int, rule: str):
        self._messages.setdefault(level, []).append({'message': message, 'rule': rule})

    def show(self, is_mono: bool = False, is_verbose: bool = False):
        if is_mono:
            self._is_mono = True

        if is_verbose:
            self._is_verbose = True

        if self.__is_problem() or self._is_verbose:
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
            icon = self.__colored(self.ICON_HOURGLASS, 'grey')
            header = self.__colored(header, attrs=['bold'])
            print('{}    input: {}'.format(icon, header))

    def print_help(self):
        help_string = self._config.get_setting('global_help')

        if help_string is not None:
            print('    '.join(filter(None, [self.ICON_HELP, str(help_string)])))

    def print_rules(self):
        for level, messages in self._messages.items():
            for message_dict in messages:
                self.__print(message_dict['message'], level, message_dict['rule'])

    def print_rule_by_level(self, level):
        for message_dict in self._messages[level]:
            self.__print(message_dict['message'], level, message_dict['rule'])

    def print_summary(self):

        messages = self._messages
        warnings = messages[1] if 1 in messages else []
        errors = messages[2] if 2 in messages else []

        summary = self.__colored('found {} problems, {} warnings'.format(len(errors), len(warnings)), attrs=['bold'])
        if self._is_verbose:
            hidden = messages[0] if 0 in messages else []
            success = messages[3] if 3 in messages else []
            summary += self.__colored(', {} successes, {} hidden'.format(len(success), len(hidden)), attrs=['bold'])

        icon = self.__colored(self.ICON_ERROR, 'red') if len(errors) > 0 else self.__colored(self.ICON_WARNING,
                                                                                             'yellow')

        print('\n{}    {}'.format(icon, summary))

    def __print(self, message: str, level, rule: str):
        if level not in [0, 3] or self._is_verbose:
            icon = None
            rule = self.__colored('[{}]'.format(rule), 'grey')

            if level == 0:
                # only in verbose mode
                icon = self.__colored(self.ICON_INFO, 'white')
            elif level == 1:
                icon = self.__colored(self.ICON_WARNING, 'yellow')
            elif level == 2:
                icon = self.__colored(self.ICON_ERROR, 'red')
                message = self.__colored(message, attrs=['bold'])
            elif level == 3:
                # only in verbose mode
                icon = self.__colored(self.ICON_SUCCESS, 'green')
            else:
                TypeError('Unknown level `{}`'.format(level))

            full_str = ' '.join([str(message), rule])
            print('    '.join(filter(None, [icon, str(full_str)])))

    def __colored(self, text: str, color: str = None, attrs: List[str] = None):
        if self._is_mono:
            return text
        return Color.colorize(text, color, attrs)
