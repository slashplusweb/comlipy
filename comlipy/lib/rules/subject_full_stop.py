from ..ensure import Ensure
from .abstract_rule import AbstractRule


class SubjectFullStop(AbstractRule):

    def check(self):
        subject = self._parser.subject

        if subject is None or not isinstance(self._value, str):
            return True

        return Ensure.is_last_character(subject, self._value)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'subject {} end with full stop'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
