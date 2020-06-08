from comlipy.lib.rule_checker import RuleChecker
from comlipy.lib.rules.abstract_rules import AbstractFooterRule


class FooterMaxLength(AbstractFooterRule):

    def check(self):
        return RuleChecker.is_valid_max_length(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'footer must not be longer than {} characters'.format(self._value)

        return result, message, self._level
