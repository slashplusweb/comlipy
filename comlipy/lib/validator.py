from importlib import import_module
from .config import Config
from .parser import Parser
from .ensure import Ensure
from re import split


class Validator:

    def __init__(self, config: Config, parser: Parser):
        self._config = config
        self._parser = parser
        self._ensure = Ensure()

    def validate(self):
        '''
            Validate a list of rules one by one.
            Therefore import the rule module dynamically and run its execute method that expects the parser object.
            The module itself is responsible for validating the message and raising corresponding error messages.
        :return:
            todo: add return type (probably void)
        '''
        for rule_key in self.__get_rule_keys():
            try:
                rule_module = self.__get_rule_class(rule_key)
                rule = rule_module(self._parser, self._config.get_rules_setting(rule_key))
                rule.execute()
            except ModuleNotFoundError:
                # todo: remove continue und raise exception
                continue

    def __get_rule_keys(self):
        if not hasattr(self, '_rule_keys'):
            self._rule_keys = self._config.get_config_default()['rules'].keys()

        return self._rule_keys

    def __get_rule_class(selfs, rule: str):
        rule_module_name = rule.replace('-', '_')
        rule_class_name = ''.join(part.capitalize() for part in split(r'-', rule))
        rule_module = import_module('.{}'.format(rule_module_name), '{}.rules'.format(__package__))

        return getattr(rule_module, rule_class_name)

    # def __get_rule_types(self):
    #     return list(set(map(self.__get_type_from_string, self.__get_rule_keys())))

    # def __get_type_from_string(self, type_string):
    #     dash_index = type_string.find('-')
    #
    #     return type_string[:dash_index] if dash_index != -1 else type_string
