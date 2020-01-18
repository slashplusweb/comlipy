import os
import yaml


class Config:
    CONFIG_FILE_NAME = 'config-comlipy.yml'

    def __init__(self, config_file_path=None):
        self._custom_config_file_path = config_file_path
        self._config = self.__load()

    def __load(self):
        """
        Load all configuration files.

        Returns:
            dict: configuration dict
        """
        config = self.__load_default()
        custom_config = self.__load_custom()

        if custom_config is not None:
            config = self.__merge(config, custom_config)

        return config

    def __merge(self, dict_default, dict_merge, add_keys=True):
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
        base_config_path = "{}/../../".format(os.path.dirname(__file__))
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
                print('Config file with filepath {} could not be found.'.format(self._custom_config_file_path))

    def __load_file(self, config_path):
        """
        Load a yaml configuration file into a dict.
        """
        with open(config_path) as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    def get_setting(self, key: str):
        """
        Get a specific configuration setting by splitting the `key` taking `_` as delimiter character.

        Returns:
            str: the configuration setting
        """
        setting_keys = key.split('_')

        config = self._config
        for setting_key in setting_keys:
            try:
                config = config[setting_key]
            except KeyError:
                print('Configuration setting with key `{}` could not be found. (Assumed cause: `{}`) '.format(key, setting_key))
                exit(1)

        return config
