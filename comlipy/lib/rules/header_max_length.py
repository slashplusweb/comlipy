from ..ensure import Ensure
from .abstract_rule import AbstractRule


class HeaderMaxLength(AbstractRule):

    def check(self):
        header = self._parser.header

        if header is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_max(header, self._value)

    def execute(self):
        result = self.check()
        message = 'header must not be longer than {} characters'.format(self._value), self._level

        return result, message
