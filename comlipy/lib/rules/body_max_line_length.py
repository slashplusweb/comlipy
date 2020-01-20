from ..ensure import Ensure
from .abstract_rule import AbstractRule


class BodyMaxLineLength(AbstractRule):

    def check(self):
        body = self._parser.body

        if body is None or not self.is_value_int():
            return True

        return Ensure.is_valid_line_length_max(body, self._value)

    def execute(self):
        result = self.check()
        message = 'body\'s lines must not be longer than than {} characters'.format(self._value), self._level

        return result, message
