from ..ensure import Ensure
from .abstract_rule import AbstractRule


class BodyEmpty(AbstractRule):

    def check(self):
        body = self._parser.body

        if body is None:
            return True

        return Ensure.is_empty(body)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'body {} be empty'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
