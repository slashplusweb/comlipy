import unittest

from comlipy.lib.ensure import Ensure


class TestEnsure(unittest.TestCase):

    def setUp(self):
        self.set_up_case_test()
        self.set_up_str_test()

    def set_up_case_test(self):
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

    def set_up_str_test(self):
        self.str_string1 = ''
        self.str_string2 = 'Foo bar baz'
        self.str_string3 = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.'
        self.str_string4 = 'Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt \n' \
                           'ut labore et dolore magna aliquyam erat, sed diam voluptua. \n' \
                           'At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata\n' \
                           ' sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed\n' \
                           ' diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero\n' \
                           ' eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est\n' \
                           ' Lorem ipsum dolor sit amet.'
        self.str_string5 = '<p>Lorem ipsum dolor sit amet,<br> consetetur sadipscing  \n' \
                           ' \n' \
                           'elitr, sed diam nonumy eirmod tempor invidunt' \
                           'ut labore et dolore magna aliquyam.</p>'
        self.str_string6 = ' '
        self.str_string7 = '\n'
        self.str_string8 = '\t'
        self.str_string9 = '012345678\n'
        self.str_string10 = '0123456789\n0123456789\n0123456789101112\n0123456789\n'

    def test_is_case_pascal_case(self):
        error_string = 'Incorrect pascal-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'pascal-case'), error_string.format(1))
        self.assertFalse(Ensure.is_case(self.case_string2, 'pascal-case'), error_string.format(2))
        self.assertFalse(Ensure.is_case(self.case_string3, 'pascal-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'pascal-case'), error_string.format(4))
        self.assertFalse(Ensure.is_case(self.case_string5, 'pascal-case'), error_string.format(5))
        self.assertTrue(Ensure.is_case(self.case_string6, 'pascal-case'), error_string.format(6))
        self.assertTrue(Ensure.is_case(self.case_string7, 'pascal-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'pascal-case'), error_string.format(8))
        self.assertFalse(Ensure.is_case(self.case_string9, 'pascal-case'), error_string.format(9))
        self.assertFalse(Ensure.is_case(self.case_string10, 'pascal-case'), error_string.format(10))
        self.assertFalse(Ensure.is_case(self.case_string11, 'pascal-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'pascal-case'), error_string.format(12))
        self.assertFalse(Ensure.is_case(self.case_string13, 'pascal-case'), error_string.format(13))
        self.assertFalse(Ensure.is_case(self.case_string14, 'pascal-case'), error_string.format(14))
        self.assertTrue(Ensure.is_case(self.case_string15, 'pascal-case'), error_string.format(15))

    def test_is_case_camel_case(self):
        error_string = 'Incorrect camel-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'camel-case'), error_string.format(1))
        self.assertFalse(Ensure.is_case(self.case_string2, 'camel-case'), error_string.format(2))
        self.assertTrue(Ensure.is_case(self.case_string3, 'camel-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'camel-case'), error_string.format(4))
        self.assertTrue(Ensure.is_case(self.case_string5, 'camel-case'), error_string.format(5))
        self.assertFalse(Ensure.is_case(self.case_string6, 'camel-case'), error_string.format(6))
        self.assertFalse(Ensure.is_case(self.case_string7, 'camel-case'), error_string.format(7))
        self.assertTrue(Ensure.is_case(self.case_string8, 'camel-case'), error_string.format(8))
        self.assertFalse(Ensure.is_case(self.case_string9, 'camel-case'), error_string.format(9))
        self.assertFalse(Ensure.is_case(self.case_string10, 'camel-case'), error_string.format(10))
        self.assertFalse(Ensure.is_case(self.case_string11, 'camel-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'camel-case'), error_string.format(12))
        self.assertFalse(Ensure.is_case(self.case_string13, 'camel-case'), error_string.format(13))
        self.assertFalse(Ensure.is_case(self.case_string14, 'camel-case'), error_string.format(14))
        self.assertFalse(Ensure.is_case(self.case_string15, 'camel-case'), error_string.format(15))

    def test_is_case_kebab_case(self):
        error_string = 'Incorrect kebab-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'kebab-case'), error_string.format(1))
        self.assertFalse(Ensure.is_case(self.case_string2, 'kebab-case'), error_string.format(2))
        self.assertTrue(Ensure.is_case(self.case_string3, 'kebab-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'kebab-case'), error_string.format(4))
        self.assertTrue(Ensure.is_case(self.case_string5, 'kebab-case'), error_string.format(5))
        self.assertFalse(Ensure.is_case(self.case_string6, 'kebab-case'), error_string.format(6))
        self.assertFalse(Ensure.is_case(self.case_string7, 'kebab-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'kebab-case'), error_string.format(8))
        self.assertTrue(Ensure.is_case(self.case_string9, 'kebab-case'), error_string.format(9))
        self.assertFalse(Ensure.is_case(self.case_string10, 'kebab-case'), error_string.format(10))
        self.assertFalse(Ensure.is_case(self.case_string11, 'kebab-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'kebab-case'), error_string.format(12))
        self.assertFalse(Ensure.is_case(self.case_string13, 'kebab-case'), error_string.format(13))
        self.assertFalse(Ensure.is_case(self.case_string14, 'kebab-case'), error_string.format(14))
        self.assertFalse(Ensure.is_case(self.case_string15, 'kebab-case'), error_string.format(15))

    def test_is_case_snake_case(self):
        error_string = 'Incorrect snake-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'snake-case'), error_string.format(1))
        self.assertFalse(Ensure.is_case(self.case_string2, 'snake-case'), error_string.format(2))
        self.assertTrue(Ensure.is_case(self.case_string3, 'snake-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'snake-case'), error_string.format(4))
        self.assertTrue(Ensure.is_case(self.case_string5, 'snake-case'), error_string.format(5))
        self.assertFalse(Ensure.is_case(self.case_string6, 'snake-case'), error_string.format(6))
        self.assertFalse(Ensure.is_case(self.case_string7, 'snake-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'snake-case'), error_string.format(8))
        self.assertFalse(Ensure.is_case(self.case_string9, 'snake-case'), error_string.format(9))
        self.assertTrue(Ensure.is_case(self.case_string10, 'snake-case'), error_string.format(10))
        self.assertFalse(Ensure.is_case(self.case_string11, 'snake-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'snake-case'), error_string.format(12))
        self.assertFalse(Ensure.is_case(self.case_string13, 'snake-case'), error_string.format(13))
        self.assertFalse(Ensure.is_case(self.case_string14, 'snake-case'), error_string.format(14))
        self.assertFalse(Ensure.is_case(self.case_string15, 'snake-case'), error_string.format(15))

    def test_is_case_start_case(self):
        error_string = 'Incorrect start-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'start-case'), error_string.format(1))
        self.assertTrue(Ensure.is_case(self.case_string2, 'start-case'), error_string.format(2))
        self.assertFalse(Ensure.is_case(self.case_string3, 'start-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'start-case'), error_string.format(4))
        self.assertFalse(Ensure.is_case(self.case_string5, 'start-case'), error_string.format(5))
        self.assertTrue(Ensure.is_case(self.case_string6, 'start-case'), error_string.format(6))
        self.assertTrue(Ensure.is_case(self.case_string7, 'start-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'start-case'), error_string.format(8))
        self.assertFalse(Ensure.is_case(self.case_string9, 'start-case'), error_string.format(9))
        self.assertFalse(Ensure.is_case(self.case_string10, 'start-case'), error_string.format(10))
        self.assertTrue(Ensure.is_case(self.case_string11, 'start-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'start-case'), error_string.format(12))
        self.assertTrue(Ensure.is_case(self.case_string13, 'start-case'), error_string.format(13))
        self.assertTrue(Ensure.is_case(self.case_string14, 'start-case'), error_string.format(14))
        self.assertTrue(Ensure.is_case(self.case_string15, 'start-case'), error_string.format(15))

    def test_is_case_sentence_case(self):
        error_string = 'Incorrect sentence-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'sentence-case'), error_string.format(1))
        self.assertTrue(Ensure.is_case(self.case_string2, 'sentence-case'), error_string.format(2))
        self.assertFalse(Ensure.is_case(self.case_string3, 'sentence-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'sentence-case'), error_string.format(4))
        self.assertFalse(Ensure.is_case(self.case_string5, 'sentence-case'), error_string.format(5))
        self.assertTrue(Ensure.is_case(self.case_string6, 'sentence-case'), error_string.format(6))
        self.assertTrue(Ensure.is_case(self.case_string7, 'sentence-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'sentence-case'), error_string.format(8))
        self.assertFalse(Ensure.is_case(self.case_string9, 'sentence-case'), error_string.format(9))
        self.assertFalse(Ensure.is_case(self.case_string10, 'sentence-case'), error_string.format(10))
        self.assertTrue(Ensure.is_case(self.case_string11, 'sentence-case'), error_string.format(11))
        self.assertTrue(Ensure.is_case(self.case_string12, 'sentence-case'), error_string.format(12))
        self.assertTrue(Ensure.is_case(self.case_string13, 'sentence-case'), error_string.format(13))
        self.assertTrue(Ensure.is_case(self.case_string14, 'sentence-case'), error_string.format(14))
        self.assertTrue(Ensure.is_case(self.case_string15, 'sentence-case'), error_string.format(15))

    def test_is_case_lower_case(self):
        error_string = 'Incorrect lower-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'lower-case'), error_string.format(1))
        self.assertFalse(Ensure.is_case(self.case_string2, 'lower-case'), error_string.format(2))
        self.assertTrue(Ensure.is_case(self.case_string3, 'lower-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'lower-case'), error_string.format(4))
        self.assertTrue(Ensure.is_case(self.case_string5, 'lower-case'), error_string.format(5))
        self.assertFalse(Ensure.is_case(self.case_string6, 'lower-case'), error_string.format(6))
        self.assertFalse(Ensure.is_case(self.case_string7, 'lower-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'lower-case'), error_string.format(8))
        self.assertTrue(Ensure.is_case(self.case_string9, 'lower-case'), error_string.format(9))
        self.assertTrue(Ensure.is_case(self.case_string10, 'lower-case'), error_string.format(10))
        self.assertFalse(Ensure.is_case(self.case_string11, 'lower-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'lower-case'), error_string.format(12))
        self.assertFalse(Ensure.is_case(self.case_string13, 'lower-case'), error_string.format(13))
        self.assertFalse(Ensure.is_case(self.case_string14, 'lower-case'), error_string.format(14))
        self.assertFalse(Ensure.is_case(self.case_string15, 'lower-case'), error_string.format(15))

    def test_is_case_upper_case(self):
        error_string = 'Incorrect upper-case in self.case_string{}'
        self.assertFalse(Ensure.is_case(self.case_string1, 'upper-case'), error_string.format(1))
        self.assertFalse(Ensure.is_case(self.case_string2, 'upper-case'), error_string.format(2))
        self.assertFalse(Ensure.is_case(self.case_string3, 'upper-case'), error_string.format(3))
        self.assertTrue(Ensure.is_case(self.case_string4, 'upper-case'), error_string.format(4))
        self.assertFalse(Ensure.is_case(self.case_string5, 'upper-case'), error_string.format(5))
        self.assertTrue(Ensure.is_case(self.case_string6, 'upper-case'), error_string.format(6))
        self.assertFalse(Ensure.is_case(self.case_string7, 'upper-case'), error_string.format(7))
        self.assertFalse(Ensure.is_case(self.case_string8, 'upper-case'), error_string.format(8))
        self.assertFalse(Ensure.is_case(self.case_string9, 'upper-case'), error_string.format(9))
        self.assertFalse(Ensure.is_case(self.case_string10, 'upper-case'), error_string.format(10))
        self.assertFalse(Ensure.is_case(self.case_string11, 'upper-case'), error_string.format(11))
        self.assertFalse(Ensure.is_case(self.case_string12, 'upper-case'), error_string.format(12))
        self.assertTrue(Ensure.is_case(self.case_string13, 'upper-case'), error_string.format(13))
        self.assertFalse(Ensure.is_case(self.case_string14, 'upper-case'), error_string.format(14))
        self.assertFalse(Ensure.is_case(self.case_string15, 'upper-case'), error_string.format(15))

    def test_is_empty(self):
        error_string = 'Incorrect is_empty in self.str_string{}'
        self.assertTrue(Ensure.is_empty(self.str_string1), error_string.format(1))
        self.assertFalse(Ensure.is_empty(self.str_string2), error_string.format(2))
        self.assertFalse(Ensure.is_empty(self.str_string3), error_string.format(3))
        self.assertFalse(Ensure.is_empty(self.str_string4), error_string.format(4))
        self.assertFalse(Ensure.is_empty(self.str_string5), error_string.format(5))
        self.assertFalse(Ensure.is_empty(self.str_string6), error_string.format(6))
        self.assertFalse(Ensure.is_empty(self.str_string7), error_string.format(7))
        self.assertFalse(Ensure.is_empty(self.str_string8), error_string.format(8))
        self.assertFalse(Ensure.is_empty(self.str_string9), error_string.format(9))
        self.assertFalse(Ensure.is_empty(self.str_string10), error_string.format(10))

    def test_length_max(self):
        error_string = 'Incorrect length_max in self.str_string{}'
        self.assertTrue(Ensure.length_max(self.str_string1, 10), error_string.format(1))
        self.assertFalse(Ensure.length_max(self.str_string2, 10), error_string.format(2))
        self.assertFalse(Ensure.length_max(self.str_string3, 10), error_string.format(3))
        self.assertFalse(Ensure.length_max(self.str_string4, 10), error_string.format(4))
        self.assertFalse(Ensure.length_max(self.str_string5, 10), error_string.format(5))
        self.assertTrue(Ensure.length_max(self.str_string6, 10), error_string.format(6))
        self.assertTrue(Ensure.length_max(self.str_string7, 10), error_string.format(7))
        self.assertTrue(Ensure.length_max(self.str_string8, 10), error_string.format(8))
        self.assertTrue(Ensure.length_max(self.str_string9, 10), error_string.format(9))
        self.assertFalse(Ensure.length_max(self.str_string10, 10), error_string.format(10))

    def test_length_min(self):
        error_string = 'Incorrect length_min in self.str_string{}'
        self.assertFalse(Ensure.length_min(self.str_string1, 10), error_string.format(1))
        self.assertTrue(Ensure.length_min(self.str_string2, 10), error_string.format(2))
        self.assertTrue(Ensure.length_min(self.str_string3, 10), error_string.format(3))
        self.assertTrue(Ensure.length_min(self.str_string4, 10), error_string.format(4))
        self.assertTrue(Ensure.length_min(self.str_string5, 10), error_string.format(5))
        self.assertFalse(Ensure.length_min(self.str_string6, 10), error_string.format(6))
        self.assertFalse(Ensure.length_min(self.str_string7, 10), error_string.format(7))
        self.assertFalse(Ensure.length_min(self.str_string8, 10), error_string.format(8))
        self.assertTrue(Ensure.length_min(self.str_string9, 10), error_string.format(9))
        self.assertTrue(Ensure.length_min(self.str_string10, 10), error_string.format(10))

    def test_line_length_max(self):
        error_string = 'Incorrect line_length_max in self.str_string{}'
        self.assertTrue(Ensure.line_length_max(self.str_string1, 10), error_string.format(1))
        self.assertFalse(Ensure.line_length_max(self.str_string2, 10), error_string.format(2))
        self.assertFalse(Ensure.line_length_max(self.str_string3, 10), error_string.format(3))
        self.assertFalse(Ensure.line_length_max(self.str_string4, 10), error_string.format(4))
        self.assertFalse(Ensure.line_length_max(self.str_string5, 10), error_string.format(5))
        self.assertTrue(Ensure.line_length_max(self.str_string6, 10), error_string.format(6))
        self.assertTrue(Ensure.line_length_max(self.str_string7, 10), error_string.format(7))
        self.assertTrue(Ensure.line_length_max(self.str_string8, 10), error_string.format(8))
        self.assertTrue(Ensure.line_length_max(self.str_string9, 10), error_string.format(9))
        self.assertFalse(Ensure.line_length_max(self.str_string10, 10), error_string.format(10))


if __name__ == '__main__':
    unittest.main()
