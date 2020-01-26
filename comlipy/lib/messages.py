from .color import Color as Col
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

    def add_rule_result(self, message: str, level: int, rule: str):
        self._messages.setdefault(level, []).append({'message': message, 'rule': rule})

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
            icon = Col.colorize(self.ICON_HOURGLASS, 'grey')
            header = Col.colorize(header, attrs=['bold'])
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

        summary = Col.colorize('found {} problems, {} warnings'.format(len(errors), len(warnings)), attrs=['bold'])
        icon = Col.colorize(self.ICON_ERROR, 'red') if len(errors) > 0 else Col.colorize(self.ICON_WARNING, 'yellow')

        print('\n{}    {}'.format(icon, summary))

    def __print(self, message: str, level, rule: str):
        if level != 0:
            icon = None
            rule = Col.colorize('[{}]'.format(rule), 'grey')

            if level == 1:
                icon = Col.colorize(self.ICON_WARNING, 'yellow')
            elif level == 2:
                icon = Col.colorize(self.ICON_ERROR, 'red')
                message = Col.colorize(message, attrs=['bold'])
            elif level == 3:
                icon = Col.colorize(self.ICON_SUCCESS, 'green')
            else:
                TypeError('Unknown level `{}`'.format(level))

            full_str = ' '.join([str(message), rule])
            print('    '.join(filter(None, [icon, str(full_str)])))
