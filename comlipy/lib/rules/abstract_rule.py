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
