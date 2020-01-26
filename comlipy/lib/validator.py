from importlib import import_module

from .config import Config
from .ensure import Ensure
from .messages import Messages
from .parser import Parser


class Validator:

    def __init__(self, config: Config, parser: Parser, messages: Messages):
        self._config = config
        self._parser = parser
        self._messages = messages
        self._ensure = Ensure()
        self._is_error = False

    def validate(self) -> None:
        """
            Validate a list of rules one by one.
            Therefore import the rule module dynamically and run its execute method that expects the parser object.
            The module itself is responsible for validating the message and raising corresponding error messages.
        :return: None
        """
        for rule_key in self.__get_rule_keys():
            rule_module = self.__get_rule_class(rule_key)
            rule = rule_module(self._parser, self._config.get_rules_setting(rule_key))
            is_valid_result, message, level = rule.execute()
            if not is_valid_result:
                # level 0 (hidden), 1 (warning), 2 (error)
                self._messages.add_rule_result(message, level, rule_key)

                # level 2 (error)
                if int(level) == 2:
                    self._is_error = True
            else:
                # level 3 (success)
                self._messages.add_rule_result(message, 3, rule_key)

    def is_error(self) -> bool:
        """
            Check if the rule validation has found an error.
            Default to False. The validation() method should be run before.
        :return: bool
        """
        return self._is_error

    def __get_rule_keys(self):
        if not hasattr(self, '_rule_keys'):
            self._rule_keys = self._config.get_config_default()['rules'].keys()

        return self._rule_keys

    def __get_rule_class(self, rule: str):
        rule_module_name = rule.replace('-', '_')
        rule_class_name = ''.join(part.capitalize() for part in rule.split('-'))
        rule_module = import_module('.{}'.format(rule_module_name), '{}.rules'.format(__package__))

        return getattr(rule_module, rule_class_name)
