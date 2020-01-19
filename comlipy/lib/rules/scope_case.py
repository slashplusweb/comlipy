from ..ensure import Ensure
from .abstract_rule import AbstractRule


class ScopeCase(AbstractRule):

    def check(self):
        scope = self._parser.scope
        if scope is None:
            return True

        # convert to list if necessary
        value = [self._value] if not isinstance(self._value, list) else self._value

        return all(isinstance(case, str) and Ensure.is_case(scope, case) for case in value)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'scope must {}be {}'.format('not ' if self.negated(self._when) else '', self._value), self._level

        return result, message
