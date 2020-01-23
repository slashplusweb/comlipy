from ..ensure import Ensure
from .abstract_rule import AbstractRule


class BodyMaxLength(AbstractRule):

    def check(self):
        body = self._parser.body

        if body is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_max(body, self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'body must not be longer than {} characters'.format(self._value)

        return result, message, self._level
