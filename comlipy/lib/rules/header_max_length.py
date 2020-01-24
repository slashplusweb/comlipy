from ..rule_checker import RuleChecker
from .abstract_rules import AbstractHeaderRule


class HeaderMaxLength(AbstractHeaderRule):

    def check(self):
        return RuleChecker.is_valid_max_length(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'header must not be longer than {} characters'.format(self._value)

        return result, message, self._level
