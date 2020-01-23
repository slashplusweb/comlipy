from ..ensure import Ensure
from .abstract_rule import AbstractRule


class ScopeEnum(AbstractRule):

    def check(self):
        scope = self._parser.scope

        if scope is None:
            return True

        return Ensure.is_in_enum(scope, self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'scope {} be one of [{}]'.format('may not' if self.negated(self._when) else 'must', ', '.join(self._value))

        return result, message, self._level
