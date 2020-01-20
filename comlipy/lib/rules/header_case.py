from ..ensure import Ensure
from .abstract_rule import AbstractRule


class HeaderCase(AbstractRule):

    def check(self):
        header = self._parser.header
        if header is None:
            return True if not self.negated(self._when) else False

        # convert to list if necessary
        value = [self._value] if not isinstance(self._value, list) else self._value

        if self.negated(self._when):
            return any(isinstance(case, str) and Ensure.is_case(header, case) for case in value)

        return all(isinstance(case, str) and Ensure.is_case(header, case) for case in value)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'header must {}be {}'.format('not ' if self.negated(self._when) else '', self._value), self._level

        return result, message
