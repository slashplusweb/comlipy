from ..ensure import Ensure
from .abstract_rule import AbstractRule


class TypeEnum(AbstractRule):

    def check(self):
        type_string = self._parser.type

        if type_string is None:
            return True

        return Ensure.is_in_enum(type_string, self._value)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'type {} be one of [{}]'.format('may not' if self.negated(self._when) else 'must', ', '.join(self._value)), self._level

        return result, message
