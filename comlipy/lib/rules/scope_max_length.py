from ..ensure import Ensure
from .abstract_rule import AbstractRule


class ScopeMaxLength(AbstractRule):

    def check(self):
        scope = self._parser.scope

        if scope is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_max(scope, self._value)

    def execute(self):
        result = self.check()
        message = 'scope must not be longer than {} characters'.format(self._value), self._level

        return result, message