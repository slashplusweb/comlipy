from comlipy.lib.rule_checker import RuleChecker
from comlipy.lib.rules.abstract_rules import AbstractSubjectRule


class SubjectFullStop(AbstractSubjectRule):

    def check(self):
        return RuleChecker.is_valid_full_stop(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if RuleChecker.is_negated(self._when) else result
        message = 'subject {} end with full stop'.format('may not' if RuleChecker.is_negated(self._when) else 'must')

        return result, message, self._level
