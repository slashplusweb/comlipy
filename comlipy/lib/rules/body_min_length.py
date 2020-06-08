from comlipy.lib.rule_checker import RuleChecker
from comlipy.lib.rules.abstract_rules import AbstractBodyRule


class BodyMinLength(AbstractBodyRule):

    def check(self):
        return RuleChecker.is_valid_min_length(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'body must not be shorter than {} characters'.format(self._value)

        return result, message, self._level
