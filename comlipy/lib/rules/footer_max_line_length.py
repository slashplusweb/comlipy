from ..rule_checker import RuleChecker
from .abstract_rules import AbstractFooterRule


class FooterMaxLineLength(AbstractFooterRule):

    def check(self):
        return RuleChecker.is_valid_max_line_length(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'footer\'s lines must not be longer than than {} characters'.format(self._value)

        return result, message, self._level
