from re import compile, split


class Ensure:
    TARGET_CASE_TYPES = (
        'camel-case', 'kebab-case', 'snake-case', 'pascal-case', 'start-case', 'upper-case', 'uppercase',
        'sentence-case', 'sentencecase', 'lower-case', 'lowercase', 'lowerCase')

    def __init__(self):
        pass

    # def case(self, raw: str, target: str = 'lowercase') -> bool:
    #     if target not in self.TARGET_CASE_TYPES:
    #         raise ValueError('case must be one of {}'.format(self.TARGET_CASE_TYPES))
    #
    #     input_string= re.sub('`.*?`|\".*?\"|\'.*?\'').strip()
    #
    #     transformed = self.__transform_to_case(input, target)

    # def __transform_to_case(self, input_string: str, case_type: str) -> str:
    #
    #     input_string = String(input_string)
    #
    #     if case_type == 'camel-case':
    #         return input_string.to_camel_case()
    #     elif case_type == 'kebab-case':
    #         return input_string.to_kebab_case()
    #     elif case_type == 'snake-case':
    #         return input_string.to_snake_case()
    #     elif case_type == 'pascal-case':
    #         return input_string.to_pascal_case()
    #     elif case_type == 'start-case':
    #         return input_string.to_start_case()
    #     elif case_type in ('upper-case', 'uppercase'):
    #         return input_string.to_upper_case()
    #     elif case_type in ('sentence-case', 'sentencecase'):
    #         return input_string.to_sentence_case()
    #     elif case_type in ('lower-case', 'lowercase', 'lowerCase'):
    #         return input_string.to_lower_case()
    #     else:
    #         raise TypeError('ensure-case: Unknown target case `{}`'.format(case_type))

    @staticmethod
    def is_case(input_string: str, target_case: str) -> bool:

        if target_case == 'camel-case':
            pattern = compile(r'^[^a-z]|[A-Z]{2}|[^a-zA-Z]')
        elif target_case == 'pascal-case':
            pattern = compile(r'^[^A-Z]|[A-Z]{2}|[^a-zA-Z]')
        elif target_case == 'kebab-case':
            pattern = compile(r'[^a-z|^-]')
        elif target_case == 'snake-case':
            pattern = compile(r'[^a-z|^_]')
        elif target_case == 'start-case':
            pattern = compile('^[^A-Z]|\s[^A-Z]')
        elif target_case in ('sentence-case', 'sentencecase'):
            pattern = compile(r'^[^A-Z]')
        elif target_case in ('upper-case', 'uppercase'):
            pattern = compile(r'[a-z]')
        elif target_case in ('lower-case', 'lowercase', 'lowerCase'):
            pattern = compile(r'[A-Z]')
        else:
            raise TypeError('ensure-case: Unknown target case `{}`'.format(target_case))

        return False if pattern.search(input_string) is not None else True

    @staticmethod
    def is_empty(input_string: str) -> bool:
        return len(input_string) == 0

    @staticmethod
    def is_valid_length_max(input_string: str, length_max: int) -> bool:
        return len(input_string) <= length_max

    @staticmethod
    def is_valid_length_min(input_string: str, length_min: int) -> bool:
        return len(input_string) >= length_min

    @staticmethod
    def is_valid_line_length_max(input_string: str, line_length_max: int) -> bool:
        return all(Ensure.is_valid_length_max(line, line_length_max) for line in split(r'/\r?\n', input_string))

    @staticmethod
    def is_leading_blank_line(input_string: str) -> bool:
        '''
        Checks is the given input_string starts with an blank line.
        This is considered true if the string is completely empty, contains only whitespace,
        or if it starts with a line that follows those criteria
        :param input_string:
        :return:
        '''
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
