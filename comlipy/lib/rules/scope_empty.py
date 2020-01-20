from ..ensure import Ensure
from .abstract_rule import AbstractRule


class ScopeEmpty(AbstractRule):

    def check(self):
        scope = self._parser.scope

        if scope is None:
            return True

        return Ensure.is_empty(scope)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'scope {} be empty'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
