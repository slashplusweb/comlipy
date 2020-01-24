from ..rule_checker import RuleChecker
from .abstract_rules import AbstractTypeRule


class TypeMinLength(AbstractTypeRule):

    def check(self):
        return RuleChecker.is_valid_min_length(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'type must not be shorter than {} characters'.format(self._value)

        return result, message, self._level
