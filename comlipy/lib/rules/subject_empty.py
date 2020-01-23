from ..ensure import Ensure
from .abstract_rule import AbstractRule


class SubjectEmpty(AbstractRule):

    def check(self):
        subject = self._parser.subject

        if subject is None:
            return True

        return Ensure.is_empty(subject)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'subject {} be empty'.format('may not' if self.negated(self._when) else 'must')

        return result, message, self._level
