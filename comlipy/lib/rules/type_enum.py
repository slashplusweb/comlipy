from ..rule_checker import RuleChecker
from .abstract_rules import AbstractTypeRule


class TypeEnum(AbstractTypeRule):

    def check(self):
        return RuleChecker.is_valid_enum(self.get_rule_input(), self._value)

    def execute(self) -> (bool, str, int):
        result = self.check()
        result = not result if RuleChecker.is_negated(self._when) else result
        message = 'type {} be one of [{}]'.format('may not' if RuleChecker.is_negated(self._when) else 'must', ', '.join(self._value))

        return result, message, self._level
