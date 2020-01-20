from ..ensure import Ensure
from .abstract_rule import AbstractRule


class SubjectCase(AbstractRule):

    def check(self):
        subject = self._parser.subject
        if subject is None:
            return True

        # convert to list if necessary
        value = [self._value] if not isinstance(self._value, list) else self._value

        if self.negated(self._when):
            return any(isinstance(case, str) and Ensure.is_case(subject, case) for case in value)

        return all(isinstance(case, str) and Ensure.is_case(subject, case) for case in value)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'subject must {}be {}'.format('not ' if self.negated(self._when) else '', self._value), self._level

        return result, message
