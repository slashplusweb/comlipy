class Parser:

    def __init__(self, message):
        self._message = message
        self._header, self._body, self._footer = self.__format_message()
        self._type = self.__parse_type()
        self._scope = self.__parse_scope()
        self._subject = self.__parse_subject()

    def __format_message(self):
        split_list = self._message.splitlines()
        header = split_list[0] if len(split_list) > 0 else ""
        body = split_list[1] if len(split_list) > 1 else None
        footer = split_list[-1] if len(split_list) > 2 else None

        return header, body, footer

    def __has_scope(self):
        return self.__get_scope_positions() != -1

    def __get_scope_positions(self):
        header = self._header

        try:
            if not hasattr(self, '_scope_positions'):
                open_brace_index = header.find('(')
                # make sure the closing brace is not before opening brace
                close_brace_index = header.find('):', open_brace_index)

                if open_brace_index != -1 and close_brace_index != -1 and close_brace_index - open_brace_index > 1:
                    self._scope_positions = (open_brace_index, close_brace_index)

            return self._scope_positions
        except AttributeError:
            pass

        return -1

    def __parse_type(self):
        header = self._header

        if self.__has_scope():
            # if there is a scope try returning the string that occures before the scope
            open_brace_index, _ = self.__get_scope_positions()

            return header[:open_brace_index] if open_brace_index > 0 else None

        # else try returning the string that occurs before (): or before : or None if its an error or empty str
        empty_brace_index = header.find('():')
        colon_index = empty_brace_index if empty_brace_index != -1 else header.find(':')

        return header[:colon_index] if colon_index > 0 else None

    def __parse_scope(self):
        header = self._header

        if self.__has_scope():
            open_brace_index, close_brace_index = self.__get_scope_positions()

            return header[open_brace_index + 1:close_brace_index]

        return None

    def __parse_subject(self):
        """
        try returning the string that occures after the colon
        or None if its an error or the index is out of bounds
        """
        header = self._header

        if self.__has_scope():
            _, close_brace_index = self.__get_scope_positions()
            colon_index = close_brace_index + 1
        else:
            colon_index = header.find(': ')

        return header[colon_index + 2:] if 0 < colon_index < len(header) - 2 else None

    @property
    def header(self):
        return self._header

    @property
    def body(self):
        return self._body

    @property
    def footer(self):
        return self._footer

    @property
    def type(self):
        return self._type

    @property
    def scope(self):
        return self._scope

    @property
    def subject(self):
        return self._subject
