from ..rule_checker import RuleChecker
from .abstract_rules import AbstractBodyRule


class BodyEmpty(AbstractBodyRule):

    def check(self):
        return RuleChecker.is_valid_empty(self.get_rule_input())

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if RuleChecker.is_negated(self._when) else result
        message = 'body {} be empty'.format('may not' if RuleChecker.is_negated(self._when) else 'must')

        return result, message, self._level
