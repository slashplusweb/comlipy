import unittest

from ...lib.rule_checker import RuleChecker


class TestRuleChecker(unittest.TestCase):

    def setUp(self):
        self.set_up_case_tests()
        self.set_up_length_tests()
        self.set_up_is_negated_test()
        self.set_up_is_valid_empty_test()
        self.set_up_is_valid_enum_test()
        self.set_up_is_valid_full_stop_test()
        self.set_up_is_valid_leading_blank_test()

    def set_up_case_tests(self):
        self.case_string1 = 'demo()1243: ademoString:sda'
        self.case_string2 = 'FooF BaR BaZ'
        self.case_string3 = 'da'
        self.case_string4 = ''
        self.case_string5 = 'a'
        self.case_string6 = 'A'
        self.case_string7 = 'PascalCase'
        self.case_string8 = 'camelCase'
        self.case_string9 = 'kebab-case'
        self.case_string10 = 'snake_case'
        self.case_string11 = 'Start Case'
        self.case_string12 = 'Sentence case'
        self.case_string13 = 'DADADBABA'
        self.case_string14 = 'FooFBaRBaZ'
        self.case_string15 = 'FooBarBaZ'

        self.case_list1 = ['lower-case', 'upper-case']
        self.case_list2 = []
        self.case_list3 = ['', 'lower-case']
        self.case_list4 = ['Foo', 'lower-case']
        self.case_list5 = ['\n', 'upper-case']
        self.case_list6 = ['sentence-case', 'start-case']
        self.case_list7 = ['sentence-case', 'pascal-case']
        self.case_list8 = ['sentence-case', 'camel-case']

        self.case_negated1 = 'never'  # means is_negated == True (see corresponding test)
        self.case_negated2 = 'always'  # means is_negated == False (see corresponding test)

    def set_up_is_valid_enum_test(self):
        self.enum_list1 = ['build', 'chore', 'ci', 'docs', 'feat', 'fix', 'improvement']
        self.enum_list2 = []
        self.enum_list3 = ['', 'chore', 'ci', 'docs', 'feat', 'fix', 'improvement']
        self.enum_list4 = ['chore', 'chore', 'docs']
        self.enum_list5 = ['\n', 'docs']

    def set_up_length_tests(self):
        self.length_str1 = ''
        self.length_str2 = '\n'
        self.length_str3 = 'ASSFAasd asd'
        self.length_str4 = '0123456789'
        self.length_str5 = '01234567891'
        self.length_str6 = '012345678'
        self.length_str7 = '012345678\nasdasd\nasdasd'
        self.length_str8 = '012345678\nfoo fuu f00 baar baz\nasdasd'
        self.length_str9 = '012345678\n             \nasdasd'
        self.length_str10 = '012345678\n             \nasdasd'
        self.length_str11 = None

    def set_up_is_negated_test(self):
        self.negated_str1 = 'never'
        self.negated_str2 = 'always'
        self.negated_str3 = 'Foo bar baz'
        self.negated_str4 = ''
        self.negated_str5 = '\n'
        self.negated_str6 = '\nnever'
        self.negated_str7 = None

    def set_up_is_valid_empty_test(self):
        self.empty_str1 = ''
        self.empty_str2 = '\n'
        self.empty_str3 = '\nFoo bar baz'
        self.empty_str4 = 'Foo'
        self.empty_str5 = '\t'
        self.empty_str6 = 'Abc'
        self.empty_str7 = None

    def test_is_valid_enum(self):
        error_string = 'Incorrect is_valid_enum in self.enum_list1{} with input_str `{}`'

        input_str = ''
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list1), error_string.format(1, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list2), error_string.format(2, input_str))
        self.assertTrue(RuleChecker.is_valid_enum(input_str, self.enum_list3), error_string.format(3, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list4), error_string.format(4, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list5), error_string.format(5, input_str))

        input_str = 'build'
        self.assertTrue(RuleChecker.is_valid_enum(input_str, self.enum_list1), error_string.format(1, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list2), error_string.format(2, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list3), error_string.format(3, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list4), error_string.format(4, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list5), error_string.format(5, input_str))

        input_str = 'Foo'
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list1), error_string.format(1, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list2), error_string.format(2, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list3), error_string.format(3, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list4), error_string.format(4, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list5), error_string.format(5, input_str))

        input_str = '\n'
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list1), error_string.format(1, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list2), error_string.format(2, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list3), error_string.format(3, input_str))
        self.assertFalse(RuleChecker.is_valid_enum(input_str, self.enum_list4), error_string.format(4, input_str))
        self.assertTrue(RuleChecker.is_valid_enum(input_str, self.enum_list5), error_string.format(5, input_str))

    def set_up_is_valid_full_stop_test(self):
        self.full_stop_str1 = ''
        self.full_stop_str2 = 'Foo'
        self.full_stop_str3 = '\n'
        self.full_stop_str4 = '.'
        self.full_stop_str5 = '. '
        self.full_stop_str6 = '#'
        self.full_stop_str7 = ' '

    def set_up_is_valid_leading_blank_test(self):
        self.leading_blank_str1 = ''
        self.leading_blank_str2 = 'Foo'
        self.leading_blank_str3 = '\n'
        self.leading_blank_str4 = '.'
        self.leading_blank_str5 = '\n\n'
        self.leading_blank_str6 = '\nasasas\n'
        self.leading_blank_str7 = '   asasas\n'
        self.leading_blank_str8 = '   \nasasas'

    def test_is_negated(self):
        error_string = 'Incorrect is_negated in self.negated_str{}'

        self.assertTrue(RuleChecker.is_negated(self.negated_str1), error_string.format(1))
        self.assertFalse(RuleChecker.is_negated(self.negated_str2), error_string.format(2))
        self.assertFalse(RuleChecker.is_negated(self.negated_str3), error_string.format(3))
        self.assertFalse(RuleChecker.is_negated(self.negated_str4), error_string.format(4))
        self.assertFalse(RuleChecker.is_negated(self.negated_str5), error_string.format(5))
        self.assertFalse(RuleChecker.is_negated(self.negated_str6), error_string.format(6))
        self.assertFalse(RuleChecker.is_negated(self.negated_str7), error_string.format(7))

    def test_is_valid_case(self):
        # True, if the string is valid for ALL cases defined in the case list

        error_string = 'Incorrect is_valid_case for self.case_string{} with default applicable (`{}`) in case_list{}'

        applicable = self.case_negated2
        case_list = self.case_list1
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                         error_string.format(2, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                         error_string.format(6, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                         error_string.format(7, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                         error_string.format(11, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                         error_string.format(12, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                         error_string.format(13, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                         error_string.format(14, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                         error_string.format(15, applicable, 1))

        case_list = self.case_list2
        self.assertTrue(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                        error_string.format(1, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                        error_string.format(2, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                        error_string.format(3, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                        error_string.format(5, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                        error_string.format(7, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                        error_string.format(8, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                        error_string.format(9, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                        error_string.format(10, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                        error_string.format(11, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                        error_string.format(12, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                        error_string.format(13, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                        error_string.format(14, applicable, 2))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                        error_string.format(15, applicable, 2))

        case_list = self.case_list3
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string1, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string2, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string3, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string4, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string5, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string6, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string7, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string8, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string9, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string10, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string11, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string12, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string13, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string14, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string15, applicable, case_list))

        case_list = self.case_list4
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string1, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string2, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string3, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string4, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string5, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string6, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string7, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string8, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string9, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string10, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string11, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string12, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string13, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string14, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string15, applicable, case_list))

        case_list = self.case_list5
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string1, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string2, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string3, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string4, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string5, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string6, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string7, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string8, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string9, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string10, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string11, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string12, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string13, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string14, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string15, applicable, case_list))

        case_list = self.case_list6
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                        error_string.format(2, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                        error_string.format(7, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                        error_string.format(11, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                         error_string.format(12, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                        error_string.format(13, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                        error_string.format(14, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                        error_string.format(15, applicable, 6))

        case_list = self.case_list7
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                         error_string.format(2, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                        error_string.format(7, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                         error_string.format(11, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                         error_string.format(12, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                         error_string.format(13, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                         error_string.format(14, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                        error_string.format(15, applicable, 7))

        case_list = self.case_list8
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                         error_string.format(2, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                         error_string.format(6, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                         error_string.format(7, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                         error_string.format(11, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                         error_string.format(12, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                         error_string.format(13, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                         error_string.format(14, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                         error_string.format(15, applicable, 8))

    def test_is_valid_case_negated(self):
        # True, if the string is valid for at least one of the cases defined int case list
        error_string = 'Incorrect is_valid_case for self.case_string{} with negated applicable (`{}`) in case_list{}'

        applicable = self.case_negated1
        case_list = self.case_list1
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                         error_string.format(2, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                        error_string.format(3, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                        error_string.format(5, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                         error_string.format(7, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                        error_string.format(9, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                        error_string.format(10, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                         error_string.format(11, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                         error_string.format(12, applicable, 1))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                        error_string.format(13, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                         error_string.format(14, applicable, 1))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                         error_string.format(15, applicable, 1))

        case_list = self.case_list2
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                         error_string.format(2, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                         error_string.format(4, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                         error_string.format(6, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                         error_string.format(7, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                         error_string.format(11, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                         error_string.format(12, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                         error_string.format(13, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                         error_string.format(14, applicable, 2))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                         error_string.format(15, applicable, 2))

        case_list = self.case_list3
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string1, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string2, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string3, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string4, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string5, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string6, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string7, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string8, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string9, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string10, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string11, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string12, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string13, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string14, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string15, applicable, case_list))

        case_list = self.case_list4
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string1, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string2, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string3, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string4, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string5, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string6, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string7, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string8, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string9, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string10, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string11, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string12, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string13, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string14, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string15, applicable, case_list))

        case_list = self.case_list5
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string1, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string2, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string3, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string4, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string5, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string6, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string7, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string8, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string9, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string10, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string11, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string12, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string13, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string14, applicable, case_list))
        self.assertRaises(TypeError, lambda: RuleChecker.is_valid_case(self.case_string15, applicable, case_list))

        case_list = self.case_list6
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                        error_string.format(2, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                        error_string.format(7, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 6))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                        error_string.format(11, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                        error_string.format(12, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                        error_string.format(13, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                        error_string.format(14, applicable, 6))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                        error_string.format(15, applicable, 6))

        case_list = self.case_list7
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                        error_string.format(2, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                         error_string.format(3, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                         error_string.format(5, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                        error_string.format(7, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                         error_string.format(8, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 7))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                        error_string.format(11, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                        error_string.format(12, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                        error_string.format(13, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                        error_string.format(14, applicable, 7))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                        error_string.format(15, applicable, 7))

        case_list = self.case_list8
        self.assertFalse(RuleChecker.is_valid_case(self.case_string1, applicable, case_list),
                         error_string.format(1, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string2, applicable, case_list),
                        error_string.format(2, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string3, applicable, case_list),
                        error_string.format(3, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string4, applicable, case_list),
                        error_string.format(4, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string5, applicable, case_list),
                        error_string.format(5, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string6, applicable, case_list),
                        error_string.format(6, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string7, applicable, case_list),
                        error_string.format(7, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string8, applicable, case_list),
                        error_string.format(8, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string9, applicable, case_list),
                         error_string.format(9, applicable, 8))
        self.assertFalse(RuleChecker.is_valid_case(self.case_string10, applicable, case_list),
                         error_string.format(10, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string11, applicable, case_list),
                        error_string.format(11, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string12, applicable, case_list),
                        error_string.format(12, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string13, applicable, case_list),
                        error_string.format(13, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string14, applicable, case_list),
                        error_string.format(14, applicable, 8))
        self.assertTrue(RuleChecker.is_valid_case(self.case_string15, applicable, case_list),
                        error_string.format(15, applicable, 8))

    def test_is_valid_empty(self):
        error_string = 'Incorrect is_valid_empty in self.empty_str{}'

        self.assertTrue(RuleChecker.is_valid_empty(self.empty_str1), error_string.format(1))
        self.assertFalse(RuleChecker.is_valid_empty(self.empty_str2), error_string.format(2))
        self.assertFalse(RuleChecker.is_valid_empty(self.empty_str3), error_string.format(3))
        self.assertFalse(RuleChecker.is_valid_empty(self.empty_str4), error_string.format(4))
        self.assertFalse(RuleChecker.is_valid_empty(self.empty_str5), error_string.format(5))
        self.assertFalse(RuleChecker.is_valid_empty(self.empty_str6), error_string.format(6))
        self.assertTrue(RuleChecker.is_valid_empty(self.empty_str7), error_string.format(7))

    def test_is_valid_full_stop(self):
        error_string = 'Incorrect is_valid_full_stop in self.full_stop_str{} compared with `{}`'

        fullstop = '.'
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str1, fullstop), error_string.format(1, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str2, fullstop), error_string.format(2, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str3, fullstop), error_string.format(3, fullstop))
        self.assertTrue(RuleChecker.is_valid_full_stop(self.full_stop_str4, fullstop), error_string.format(4, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str5, fullstop), error_string.format(5, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str6, fullstop), error_string.format(6, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str7, fullstop), error_string.format(7, fullstop))

        fullstop = ''
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str1, fullstop), error_string.format(1, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str2, fullstop), error_string.format(2, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str3, fullstop), error_string.format(3, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str4, fullstop), error_string.format(4, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str5, fullstop), error_string.format(5, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str6, fullstop), error_string.format(6, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str7, fullstop), error_string.format(7, fullstop))

        fullstop = ' '
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str1, fullstop), error_string.format(1, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str2, fullstop), error_string.format(2, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str3, fullstop), error_string.format(3, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str4, fullstop), error_string.format(4, fullstop))
        self.assertTrue(RuleChecker.is_valid_full_stop(self.full_stop_str5, fullstop), error_string.format(5, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str6, fullstop), error_string.format(6, fullstop))
        self.assertTrue(RuleChecker.is_valid_full_stop(self.full_stop_str7, fullstop), error_string.format(7, fullstop))

        fullstop = 'ABC'
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str1, fullstop), error_string.format(1, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str2, fullstop), error_string.format(2, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str3, fullstop), error_string.format(3, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str4, fullstop), error_string.format(4, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str5, fullstop), error_string.format(5, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str6, fullstop), error_string.format(6, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str7, fullstop), error_string.format(7, fullstop))

        fullstop = '\n'
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str1, fullstop), error_string.format(1, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str2, fullstop), error_string.format(2, fullstop))
        self.assertTrue(RuleChecker.is_valid_full_stop(self.full_stop_str3, fullstop), error_string.format(3, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str4, fullstop), error_string.format(4, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str5, fullstop), error_string.format(5, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str6, fullstop), error_string.format(6, fullstop))
        self.assertFalse(RuleChecker.is_valid_full_stop(self.full_stop_str7, fullstop), error_string.format(7, fullstop))

    def test_is_valid_leading_blank(self):
        error_string = 'Incorrect is_valid_leading_blank in self.leading_blank_str{}'

        self.assertTrue(RuleChecker.is_valid_leading_blank(self.leading_blank_str1), error_string.format(1))
        self.assertFalse(RuleChecker.is_valid_leading_blank(self.leading_blank_str2), error_string.format(2))
        self.assertTrue(RuleChecker.is_valid_leading_blank(self.leading_blank_str3), error_string.format(3))
        self.assertFalse(RuleChecker.is_valid_leading_blank(self.leading_blank_str4), error_string.format(4))
        self.assertTrue(RuleChecker.is_valid_leading_blank(self.leading_blank_str5), error_string.format(5))
        self.assertTrue(RuleChecker.is_valid_leading_blank(self.leading_blank_str6), error_string.format(6))
        self.assertFalse(RuleChecker.is_valid_leading_blank(self.leading_blank_str7), error_string.format(7))
        self.assertTrue(RuleChecker.is_valid_leading_blank(self.leading_blank_str8), error_string.format(8))

    def test_is_valid_min_length(self):
        error_string = 'Incorrect is_valid_min_length in self.length_str{} with length {}'

        length = 0
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str1, length), error_string.format(1, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str2, length), error_string.format(2, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str3, length), error_string.format(3, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str4, length), error_string.format(4, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str5, length), error_string.format(5, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str6, length), error_string.format(6, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str7, length), error_string.format(7, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str8, length), error_string.format(8, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str9, length), error_string.format(9, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str10, length), error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str11, length), error_string.format(11, length))

        length = 5
        self.assertFalse(RuleChecker.is_valid_min_length(self.length_str1, length), error_string.format(1, length))
        self.assertFalse(RuleChecker.is_valid_min_length(self.length_str2, length), error_string.format(2, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str3, length), error_string.format(3, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str4, length), error_string.format(4, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str5, length), error_string.format(5, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str6, length), error_string.format(6, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str7, length), error_string.format(7, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str8, length), error_string.format(8, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str9, length), error_string.format(9, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str10, length), error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str11, length), error_string.format(11, length))

        length = 10
        self.assertFalse(RuleChecker.is_valid_min_length(self.length_str1, length), error_string.format(1, length))
        self.assertFalse(RuleChecker.is_valid_min_length(self.length_str2, length), error_string.format(2, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str3, length), error_string.format(3, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str4, length), error_string.format(4, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str5, length), error_string.format(5, length))
        self.assertFalse(RuleChecker.is_valid_min_length(self.length_str6, length), error_string.format(6, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str7, length), error_string.format(7, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str8, length), error_string.format(8, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str9, length), error_string.format(9, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str10, length), error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_min_length(self.length_str11, length), error_string.format(11, length))

    def test_is_valid_max_length(self):
        error_string = 'Incorrect is_valid_max_length in self.length_str{} with length {}'

        length = 0
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str1, length), error_string.format(1, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str2, length), error_string.format(2, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str3, length), error_string.format(3, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str4, length), error_string.format(4, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str5, length), error_string.format(5, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str6, length), error_string.format(6, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str7, length), error_string.format(7, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str8, length), error_string.format(8, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str9, length), error_string.format(9, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str10, length), error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str11, length), error_string.format(11, length))

        length = 5
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str1, length), error_string.format(1, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str2, length), error_string.format(2, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str3, length), error_string.format(3, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str4, length), error_string.format(4, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str5, length), error_string.format(5, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str6, length), error_string.format(6, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str7, length), error_string.format(7, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str8, length), error_string.format(8, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str9, length), error_string.format(9, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str10, length), error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str11, length), error_string.format(11, length))

        length = 10
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str1, length), error_string.format(1, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str2, length), error_string.format(2, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str3, length), error_string.format(3, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str4, length), error_string.format(4, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str5, length), error_string.format(5, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str6, length), error_string.format(6, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str7, length), error_string.format(7, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str8, length), error_string.format(8, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str9, length), error_string.format(9, length))
        self.assertFalse(RuleChecker.is_valid_max_length(self.length_str10, length), error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_max_length(self.length_str11, length), error_string.format(11, length))

    def test_is_valid_max_line_length(self):
        error_string = 'Incorrect test_is_valid_max_line_length in self.length_str{} with length {}'

        length = 0
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str1, length), error_string.format(1, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str2, length), error_string.format(2, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str3, length), error_string.format(3, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str4, length), error_string.format(4, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str5, length), error_string.format(5, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str6, length), error_string.format(6, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str7, length), error_string.format(7, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str8, length), error_string.format(8, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str9, length), error_string.format(9, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str10, length),
                         error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str11, length),
                        error_string.format(11, length))

        length = 5
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str1, length), error_string.format(1, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str2, length), error_string.format(2, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str3, length), error_string.format(3, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str4, length), error_string.format(4, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str5, length), error_string.format(5, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str6, length), error_string.format(6, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str7, length), error_string.format(7, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str8, length), error_string.format(8, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str9, length), error_string.format(9, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str10, length),
                         error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str11, length),
                        error_string.format(11, length))

        length = 10
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str1, length), error_string.format(1, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str2, length), error_string.format(2, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str3, length), error_string.format(3, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str4, length), error_string.format(4, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str5, length), error_string.format(5, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str6, length), error_string.format(6, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str7, length), error_string.format(7, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str8, length), error_string.format(8, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str9, length), error_string.format(9, length))
        self.assertFalse(RuleChecker.is_valid_max_line_length(self.length_str10, length),
                         error_string.format(10, length))
        self.assertTrue(RuleChecker.is_valid_max_line_length(self.length_str11, length),
                        error_string.format(11, length))


if __name__ == '__main__':
    unittest.main()
