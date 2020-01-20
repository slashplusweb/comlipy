from ..ensure import Ensure
from .abstract_rule import AbstractRule


class HeaderFullStop(AbstractRule):

    def check(self):
        header = self._parser.header

        if header is None or not isinstance(self._value, str):
            return False

        return Ensure.is_last_character(header, self._value)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'header {} end with full stop'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
