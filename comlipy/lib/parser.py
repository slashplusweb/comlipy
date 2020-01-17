import re


class Parser:

    def __init__(self, message):
        self._message = message
        self._type = self.__parse_type()
        self._scope = self.__parse_scope()
        self._subject = self.__parse_subject()
        print('message is {}'.format(message))
        print('type is {}'.format(self._type))
        print('scope is {}'.format(self._scope))
        print('subject is {}'.format(self._subject))

    def __has_scope(self):
        return self.__get_scope_positions() != -1

    def __get_scope_positions(self):
        try:
            if not hasattr(self, '_scope_positions'):
                open_brace_index = self._message.find('(')
                # make sure the closing brace is not before opening brace
                close_brace_index = self._message.find('):', open_brace_index)

                if open_brace_index != -1 and close_brace_index != -1 and close_brace_index-open_brace_index > 1:
                    self._scope_positions = (open_brace_index, close_brace_index)

            return self._scope_positions
        except AttributeError:
            return -1

    def __parse_type(self):
        if self.__has_scope():
            ''' if there is a scope try returning the string that occures before the scope'''
            open_brace_index, _ = self.__get_scope_positions()

            return self._message[:open_brace_index]
        else:
            ''' else try returning the string that occures before the colon or None if its an error or an empty str'''
            colon_index = self._message.find(':')
            return self._message[:colon_index] if colon_index > 0 else None

    def __parse_scope(self):
        if self.__has_scope():
            open_brace_index, close_brace_index = self.__get_scope_positions()

            return self._message[open_brace_index + 1:close_brace_index]

    def __parse_subject(self):
        ''' try returning the string that occures after the colon or None if its an error or the index is out of bounds'''
        if self.__has_scope():
            _, close_brace_index = self.__get_scope_positions()
            colon_index = close_brace_index + 1
        else:
            colon_index = self._message.find(':')
        return self._message[colon_index + 1:] if colon_index > 0 and len(self._message) - 1 > colon_index else None

    @property
    def type(self):
        return self._type

    @property
    def scope(self):
        return self._scope

    @property
    def subject(self):
        return self._subject
