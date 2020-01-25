import abc

from ..parser import Parser


class AbstractRule(abc.ABC):

    def __init__(self, parser: Parser, settings: list):
        self._parser = parser
        self._when, self._value, self._level = settings

    def get_rule_input(self):
        return getattr(self._parser, '_{}'.format(self.get_rule_type()))

    @abc.abstractmethod
    def get_rule_type(self):
        pass

    @abc.abstractmethod
    def execute(self) -> (bool, str, int):
        pass

    @abc.abstractmethod
    def check(self):
        pass


class AbstractHeaderRule(AbstractRule, abc.ABC):

    def get_rule_type(self):
        return 'header'


class AbstractBodyRule(AbstractRule, abc.ABC):

    def get_rule_type(self):
        return 'body'


class AbstractFooterRule(AbstractRule, abc.ABC):

    def get_rule_type(self):
        return 'footer'


class AbstractScopeRule(AbstractRule, abc.ABC):

    def get_rule_type(self):
        return 'scope'


class AbstractTypeRule(AbstractRule, abc.ABC):

    def get_rule_type(self):
        return 'type'


class AbstractSubjectRule(AbstractRule, abc.ABC):

    def get_rule_type(self):
        return 'subject'
