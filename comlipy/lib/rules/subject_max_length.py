from comlipy.lib.rule_checker import RuleChecker
from comlipy.lib.rules.abstract_rules import AbstractSubjectRule


class SubjectMaxLength(AbstractSubjectRule):

    def check(self):
        return RuleChecker.is_valid_max_length(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        message = 'subject must not be longer than {} characters'.format(self._value)

        return result, message, self._level
