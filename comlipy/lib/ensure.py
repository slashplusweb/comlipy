import re

class Ensure:
    TARGET_CASE_TYPES = (
        'camel-case', 'kebab-case', 'snake-case', 'pascal-case', 'start-case', 'upper-case', 'uppercase',
        'sentence-case', 'sentencecase', 'lower-case', 'lowercase', 'lowerCase')

    def __init__(self):
        pass

    @staticmethod
    def is_case(input_string: str, target_case: str) -> bool:

        if target_case == 'camel-case':
            pattern = re.compile(r'^[^a-z]|[A-Z]{2}|[^a-zA-Z]')
        elif target_case == 'pascal-case':
            pattern = re.compile(r'^[^A-Z]|[A-Z]{2}|[^a-zA-Z]')
        elif target_case == 'kebab-case':
            pattern = re.compile(r'[^a-z|^-]')
        elif target_case == 'snake-case':
            pattern = re.compile(r'[^a-z|^_]')
        elif target_case == 'start-case':
            pattern = re.compile(r'^[^A-Z]|\s[^A-Z]')
        elif target_case in ('sentence-case', 'sentencecase'):
            pattern = re.compile(r'^[^A-Z]')
        elif target_case in ('upper-case', 'uppercase'):
            pattern = re.compile(r'[a-z]')
        elif target_case in ('lower-case', 'lowercase', 'lowerCase'):
            pattern = re.compile(r'[A-Z]')
        else:
            raise TypeError('ensure-case: Unknown target case `{}`'.format(target_case))

        return False if pattern.search(input_string) is not None else True

    @staticmethod
    def is_empty(input_string: str) -> bool:
        return len(input_string) == 0

    @staticmethod
    def length_max(input_string: str, length_max: int) -> bool:
        return len(input_string) <= length_max

    @staticmethod
    def length_min(input_string: str, length_min: int) -> bool:
        return len(input_string) >= length_min

    @staticmethod
    def line_length_max(input_string: str, line_length_max: int) -> bool:
        return all(Ensure.length_max(line, line_length_max) for line in re.split(r'\r?\n', input_string))

    @staticmethod
    def leading_blank_line(input_string: str) -> bool:
        """
        Checks is the given input_string starts with an blank line.
        This is considered true if the string is completely empty, contains only whitespace,
        or if it starts with a line that follows those criteria
        :param input_string:
        :return:
        """
        # return true if the complete string is empty
        if len(input_string) == 0 or input_string.isspace():
            return True

        # check for line breaks and if there is one, check if its empty
        split_lines = input_string.splitlines(True)
        return len(split_lines) > 0 and split_lines[0].isspace()

    @staticmethod
    def is_last_character(input_string: str, last_character) -> bool:
        if len(input_string) == 0 or len(last_character) != 1:
            return False

        return input_string[-1] == last_character

    @staticmethod
    def is_in_enum(input_string: str, enum: list):
        return input_string in enum

    @staticmethod
    def is_int(value):
        # of course we could check whether the value is of instance int,
        # but we also want to check whether we could cast it to int or not
        try:
            int(value)
        except (TypeError, ValueError):
            return False
        return True
