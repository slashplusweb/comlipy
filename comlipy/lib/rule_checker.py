from .ensure import Ensure


class RuleChecker:

    @staticmethod
    def is_negated(when: str) -> bool:
        return when == 'never'

    @staticmethod
    def is_valid_case(input_str: str, applicable: str, value):
        if input_str is None:
            return True if not RuleChecker.is_negated(applicable) else False

        # convert to list if necessary
        value = [value] if not isinstance(value, list) else value

        if RuleChecker.is_negated(applicable):
            return any(isinstance(case, str) and Ensure.is_case(input_str, case) for case in value)

        return all(isinstance(case, str) and Ensure.is_case(input_str, case) for case in value)

    @staticmethod
    def is_valid_empty(input_str: str):
        if input_str is None:
            return True

        return Ensure.is_empty(input_str)

    @staticmethod
    def is_valid_leading_blank(input_str: str):

        if input_str is None:
            return True

        return Ensure.leading_blank_line(input_str)

    @staticmethod
    def is_valid_max_length(input_str: str, value):
        # None is 'True', because the actual 'empty' rule is responsible for None handling, NOT the 'max-length' rule.
        # This way we do not throw more than one message
        if input_str is None or not Ensure.is_int(value):
            return True

        return Ensure.length_max(input_str, value)

    @staticmethod
    def is_valid_min_length(input_str: str, value):
        # None is 'True', because the actual 'empty' rule is responsible for None handling, NOT the 'min-length' rule.
        # This way we do not throw more than one message
        if input_str is None or not Ensure.is_int(value):
            return True

        return Ensure.length_min(input_str, value)

    @staticmethod
    def is_valid_max_line_length(input_str: str, value):
        # None is 'True', because the actual 'empty' rule is responsible for None handling, NOT the 'max-line-length'
        # rule. This way we do not throw more than one message
        if input_str is None or not Ensure.is_int(value):
            return True

        return Ensure.line_length_max(input_str, value)

    @staticmethod
    def is_valid_full_stop(input_str: str, value):
        if input_str is None or not isinstance(value, str):
            return False

        return Ensure.is_last_character(input_str, value)

    @staticmethod
    def is_valid_enum(input_str: str, value):
        if input_str is None:
            return True

        return Ensure.is_in_enum(input_str, value)
