from ..rule_checker import RuleChecker
from .abstract_rules import AbstractHeaderRule


class HeaderFullStop(AbstractHeaderRule):

    def check(self):
        return RuleChecker.is_valid_full_stop(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if RuleChecker.is_negated(self._when) else result
        message = 'header {} end with full stop'.format('may not' if RuleChecker.is_negated(self._when) else 'must')

        return result, message, self._level
