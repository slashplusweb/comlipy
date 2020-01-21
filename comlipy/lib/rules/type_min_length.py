from ..ensure import Ensure
from .abstract_rule import AbstractRule


class TypeMinLength(AbstractRule):

    def check(self):
        type_string = self._parser.type

        if type_string is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_min(type_string, self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'type must not be shorter than {} characters'.format(self._value)

        return result, message, self._level
