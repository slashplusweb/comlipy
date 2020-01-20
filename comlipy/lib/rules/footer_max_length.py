from ..ensure import Ensure
from .abstract_rule import AbstractRule


class FooterMaxLength(AbstractRule):

    def check(self):
        footer = self._parser.footer

        if footer is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_max(footer, self._value)

    def execute(self):
        result = self.check()
        message = 'footer must not be longer than {} characters'.format(self._value), self._level

        return result, message
