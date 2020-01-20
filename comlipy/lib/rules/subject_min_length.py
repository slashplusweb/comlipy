from ..ensure import Ensure
from .abstract_rule import AbstractRule


class SubjectMinLength(AbstractRule):

    def check(self):
        subject = self._parser.subject

        if subject is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_min(subject, self._value)

    def execute(self):
        result = self.check()
        message = 'subject must not be shorter than {} characters'.format(self._value), self._level

        return result, message
