from ..rule_checker import RuleChecker
from .abstract_rules import AbstractFooterRule


class FooterLeadingBlank(AbstractFooterRule):

    def check(self):
        return RuleChecker.is_valid_leading_blank(self.get_rule_input())

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if RuleChecker.is_negated(self._when) else result
        message = 'footer {} have leading blank line'.format('may not' if RuleChecker.is_negated(self._when) else 'must')

        return result, message, self._level
