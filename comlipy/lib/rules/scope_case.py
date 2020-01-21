from ..ensure import Ensure
from .abstract_rule import AbstractRule


class ScopeCase(AbstractRule):

    def check(self):
        scope = self._parser.scope
        if scope is None:
            return True if not self.negated(self._when) else False

        # convert to list if necessary
        value = [self._value] if not isinstance(self._value, list) else self._value

        if self.negated(self._when):
            return any(isinstance(case, str) and Ensure.is_case(scope, case) for case in value)

        return all(isinstance(case, str) and Ensure.is_case(scope, case) for case in value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'scope must {}be {}'.format('not ' if self.negated(self._when) else '', self._value)

        return result, message, self._level
