import os
import sys

import yaml


class Config:
    CONFIG_FILE_NAME = 'config-comlipy.yml'

    def __init__(self, config_file_path=None):
        self._custom_config_file_path = config_file_path

    def get_config(self):
        if not hasattr(self, '_config'):
            custom_config = self.__load_custom()
            config_default = self.get_config_default()

            self._config = self.__merge(config_default, custom_config) if custom_config is not None else config_default

        return self._config

    def get_config_default(self):
        if not hasattr(self, '_default_config'):
            self._default_config = self.__load_default()

        return self._default_config

    def get_setting(self, key: str):
        """
        Get a specific configuration setting by splitting the `key` taking `_` as delimiter character.

        Returns:
            str: the configuration setting
        """
        setting_keys = key.split('_')

        config = self.get_config()
        for setting_key in setting_keys:
            try:
                config = config[setting_key]
            except KeyError:
                print('Configuration setting with key `{}` invalid (Assumed cause: `{}`) '.format(key, setting_key))

        return config

    def get_rules_setting(self, key: str) -> list:
        """
        Get a specific configuration rules setting.

        Returns:
            list(str): the configuration rules setting (when, value, level)
        """
        config = self.get_config()

        try:
            config = config['rules'][key]
            when = config['applicable']
            value = config['value']
            level = config['level']

            return [when, value, level]
        except KeyError:
            print('Configuration rule `rules_{}` could not be found.'.format(key))

        return []

    def __merge(self, dict_default: dict, dict_merge: dict, add_keys=True) -> dict:
        """
        Recursive merge two dicts.
        Inspired by :meth:``dict.update()`` but instead of updating only top-level keys,
        `__merge` recurses down into dicts nested to an arbitrary depth, updating keys.
        The `dict_merge` is merged into `dict_default`.

        This version will return a copy of the dictionary and leave the original
        arguments untouched.

        The optional argument `add_keys`, determines whether keys which are
        present in `dict_merge` but not `dict_default` should be included in the
        new dict.

        Args:
            dict_default (dict) onto which the merge is executed
            dict_merge (dict): dct merged into dct
            add_keys (bool): whether to add new keys

        Returns:
            dict: updated dict
        """
        dict_return = dict_default.copy()
        if add_keys is False:
            dict_merge = {key: dict_merge[key] for key in set(dict_return).intersection(set(dict_merge))}

        dict_return.update({
            key: self.__merge(dict_return[key], dict_merge[key], add_keys=add_keys)
            if isinstance(dict_return.get(key), dict) and isinstance(dict_merge[key], dict)
            else dict_merge[key]
            for key in dict_merge.keys()
        })

        return dict_return

    def __load_default(self):
        """
        Load the default configuration file.
        """
        base_config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        default_config_file = os.path.join(base_config_path, self.CONFIG_FILE_NAME)

        return self.__load_file(default_config_file)

    def __load_custom(self):
        """
        Load the custom configuration file if it has bee passed.
        """
        if self._custom_config_file_path is not None:
            try:
                return self.__load_file(self._custom_config_file_path)
            except FileNotFoundError:
                print('Config file with filepath {} could not be found'.format(self._custom_config_file_path))
                sys.exit(1)

        return None

    def __load_file(self, config_path):
        """
        Load a yaml configuration file into a dict.
        """
        with open(config_path) as file:
            return yaml.safe_load(file)
