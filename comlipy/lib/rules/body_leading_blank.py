from ..ensure import Ensure
from .abstract_rule import AbstractRule


class BodyLeadingBlank(AbstractRule):

    def check(self):
        body = self._parser.body

        if body is None:
            return True

        return Ensure.is_leading_blank_line(body)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'body {} have leading blank line'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
