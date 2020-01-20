from ..ensure import Ensure
from .abstract_rule import AbstractRule


class FooterEmpty(AbstractRule):

    def check(self):
        footer = self._parser.footer

        if footer is None:
            return True

        return Ensure.is_empty(footer)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'footer {} be empty'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
