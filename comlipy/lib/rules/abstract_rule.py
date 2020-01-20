import abc

from ..parser import Parser


class AbstractRule(abc.ABC):

    def __init__(self, parser: Parser, settings: list):
        self._parser = parser
        self._when, self._value, self._level = settings

    @abc.abstractmethod
    def execute(self):
        pass

    @abc.abstractmethod
    def check(self):
        pass

    def negated(self, when: str) -> bool:
        return when == 'never'

    def is_value_int(self):
        # of course we could check whether the value is of instance int,
        # but we also want to check whether we could cast it to int or not
        try:
            int(self._value)
        except (TypeError, ValueError) as e:
            return False
        return True
