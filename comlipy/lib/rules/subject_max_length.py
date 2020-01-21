from ..ensure import Ensure
from .abstract_rule import AbstractRule


class SubjectMaxLength(AbstractRule):

    def check(self):
        subject = self._parser.subject

        if subject is None or not self.is_value_int():
            return True

        return Ensure.is_valid_length_max(subject, self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'subject must not be longer than {} characters'.format(self._value)

        return result, message, self._level
