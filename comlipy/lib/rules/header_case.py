from ..rule_checker import RuleChecker
from .abstract_rules import AbstractHeaderRule


class HeaderCase(AbstractHeaderRule):

    def check(self):
        return RuleChecker.is_valid_case(self.get_rule_input(), self._when, self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if RuleChecker.is_negated(self._when) else result
        message = 'header must {}be {}'.format('not ' if RuleChecker.is_negated(self._when) else '', self._value)

        return result, message, self._level
