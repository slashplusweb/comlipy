from ..ensure import Ensure
from .abstract_rule import AbstractRule


class TypeEmpty(AbstractRule):

    def check(self):
        type_string = self._parser.type

        if type_string is None:
            return True

        return Ensure.is_empty(type_string)

    def execute(self):
        result = self.check()
        result = not result if self.negated(self._when) else result
        message = 'type {} be empty'.format('may not' if self.negated(self._when) else 'must'), self._level

        return result, message
