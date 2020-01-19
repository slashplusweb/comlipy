import unittest
from ..lib.string import String


class StringTest(unittest.TestCase):

    def setUp(self):
        self.test_string1 = String('demo()1243: ademoString:sda')
        self.test_string2 = String('FooF BaR BaZ')
        self.test_string3 = String('da')
        self.test_string4 = String('')
        self.test_string5 = String('a')
        self.test_string6 = String('A')
        self.test_string7 = String('PascalCase')
        self.test_string8 = String('camelCase')
        self.test_string9 = String('kebab-case')
        self.test_string10 = String('snake_case')
        self.test_string11 = String('Start Case')
        self.test_string12 = String('Sentence case')

    def runTest(self):
        self.test_to_camel_case()
        self.test_to_kebab_case()
        self.test_to_snake_case()
        self.test_to_pascal_case()
        self.test_to_start_case()
        self.test_to_upper_case()
        self.test_to_sentence_case()
        self.test_to_lower_case()

    def test_to_pascal_case(self):
        error_string = 'Incorrect pascal-case in test_string{}'
        self.assertEqual(self.test_string1.to_pascal_case(), 'DemoAdemoStringsda', error_string.format(1))
        self.assertEqual(self.test_string2.to_pascal_case(), 'FooFBaRBaZ', error_string.format(2))
        self.assertEqual(self.test_string3.to_pascal_case(), 'Da', error_string.format(3))
        self.assertEqual(self.test_string4.to_pascal_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_pascal_case(), 'A', error_string.format(5))
        self.assertEqual(self.test_string6.to_pascal_case(), 'A', error_string.format(6))
        self.assertEqual(self.test_string7.to_pascal_case(), 'PascalCase', error_string.format(7))
        self.assertEqual(self.test_string8.to_pascal_case(), 'CamelCase', error_string.format(8))
        self.assertEqual(self.test_string9.to_pascal_case(), 'Kebabcase', error_string.format(9))
        self.assertEqual(self.test_string10.to_pascal_case(), 'Snakecase', error_string.format(10))
        self.assertEqual(self.test_string11.to_pascal_case(), 'StartCase', error_string.format(11))
        self.assertEqual(self.test_string12.to_pascal_case(), 'SentenceCase', error_string.format(12))
    

    def test_to_camel_case(self):
        error_string = 'Incorrect camel-case in test_string{}'
        self.assertEqual(self.test_string1.to_camel_case(), 'demoAdemoStringsda', error_string.format(1))
        self.assertEqual(self.test_string2.to_camel_case(), 'fooFBaRBaZ', error_string.format(2))
        self.assertEqual(self.test_string3.to_camel_case(), 'da', error_string.format(3))
        self.assertEqual(self.test_string4.to_camel_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_camel_case(), 'a', error_string.format(5))
        self.assertEqual(self.test_string6.to_camel_case(), 'a', error_string.format(6))
        self.assertEqual(self.test_string7.to_camel_case(), 'pascalCase', error_string.format(7))
        self.assertEqual(self.test_string8.to_camel_case(), 'camelCase', error_string.format(8))
        self.assertEqual(self.test_string9.to_camel_case(), 'kebabcase', error_string.format(9))
        self.assertEqual(self.test_string10.to_camel_case(), 'snakecase', error_string.format(10))
        self.assertEqual(self.test_string11.to_camel_case(), 'startCase', error_string.format(11))
        self.assertEqual(self.test_string12.to_camel_case(), 'sentenceCase', error_string.format(12))

    def test_to_kebab_case(self):
        error_string = 'Incorrect kebab-case in test_string{}'
        self.assertEqual(self.test_string1.to_kebab_case(), 'demo1243-ademostringsda', error_string.format(1))
        self.assertEqual(self.test_string2.to_kebab_case(), 'foof-bar-baz', error_string.format(2))
        self.assertEqual(self.test_string3.to_kebab_case(), 'da', error_string.format(3))
        self.assertEqual(self.test_string4.to_kebab_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_kebab_case(), 'a', error_string.format(5))
        self.assertEqual(self.test_string6.to_kebab_case(), 'a', error_string.format(6))
        self.assertEqual(self.test_string7.to_kebab_case(), 'pascalcase', error_string.format(7))
        self.assertEqual(self.test_string8.to_kebab_case(), 'camelcase', error_string.format(8))
        self.assertEqual(self.test_string9.to_kebab_case(), 'kebab-case', error_string.format(9))
        self.assertEqual(self.test_string10.to_kebab_case(), 'snakecase', error_string.format(10))
        self.assertEqual(self.test_string11.to_kebab_case(), 'start-case', error_string.format(11))
        self.assertEqual(self.test_string12.to_kebab_case(), 'sentence-case', error_string.format(12))

    def test_to_snake_case(self):
        error_string = 'Incorrect snake-case in test_string{}'
        self.assertEqual(self.test_string1.to_snake_case(), 'demo1243_ademostringsda', error_string.format(1))
        self.assertEqual(self.test_string2.to_snake_case(), 'foof_bar_baz', error_string.format(2))
        self.assertEqual(self.test_string3.to_snake_case(), 'da', error_string.format(3))
        self.assertEqual(self.test_string4.to_snake_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_snake_case(), 'a', error_string.format(5))
        self.assertEqual(self.test_string6.to_snake_case(), 'a', error_string.format(6))
        self.assertEqual(self.test_string7.to_snake_case(), 'pascalcase', error_string.format(7))
        self.assertEqual(self.test_string8.to_snake_case(), 'camelcase', error_string.format(8))
        self.assertEqual(self.test_string9.to_snake_case(), 'kebabcase', error_string.format(9))
        self.assertEqual(self.test_string10.to_snake_case(), 'snake_case', error_string.format(10))
        self.assertEqual(self.test_string11.to_snake_case(), 'start_case', error_string.format(11))
        self.assertEqual(self.test_string12.to_snake_case(), 'sentence_case', error_string.format(12))

    def test_to_start_case(self):
        error_string = 'Incorrect start-case in test_string{}'
        self.assertEqual(self.test_string1.to_start_case(), 'Demo()1243: AdemoString:sda', error_string.format(1))
        self.assertEqual(self.test_string2.to_start_case(), 'FooF BaR BaZ', error_string.format(2))
        self.assertEqual(self.test_string3.to_start_case(), 'Da', error_string.format(3))
        self.assertEqual(self.test_string4.to_start_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_start_case(), 'A', error_string.format(5))
        self.assertEqual(self.test_string6.to_start_case(), 'A', error_string.format(6))
        self.assertEqual(self.test_string7.to_start_case(), 'PascalCase', error_string.format(7))
        self.assertEqual(self.test_string8.to_start_case(), 'CamelCase', error_string.format(8))
        self.assertEqual(self.test_string9.to_start_case(), 'Kebab-case', error_string.format(9))
        self.assertEqual(self.test_string10.to_start_case(), 'Snake_case', error_string.format(10))
        self.assertEqual(self.test_string11.to_start_case(), 'Start Case', error_string.format(11))
        self.assertEqual(self.test_string12.to_start_case(), 'Sentence Case', error_string.format(12))

    def test_to_sentence_case(self):
        error_string = 'Incorrect sentence-case in test_string{}'
        self.assertEqual(self.test_string1.to_sentence_case(), 'Demo()1243: ademoString:sda', error_string.format(1))
        self.assertEqual(self.test_string2.to_sentence_case(), 'FooF BaR BaZ', error_string.format(2))
        self.assertEqual(self.test_string3.to_sentence_case(), 'Da', error_string.format(3))
        self.assertEqual(self.test_string4.to_sentence_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_sentence_case(), 'A', error_string.format(5))
        self.assertEqual(self.test_string6.to_sentence_case(), 'A', error_string.format(6))
        self.assertEqual(self.test_string7.to_sentence_case(), 'PascalCase', error_string.format(7))
        self.assertEqual(self.test_string8.to_sentence_case(), 'CamelCase', error_string.format(8))
        self.assertEqual(self.test_string9.to_sentence_case(), 'Kebab-case', error_string.format(9))
        self.assertEqual(self.test_string10.to_sentence_case(), 'Snake_case', error_string.format(10))
        self.assertEqual(self.test_string11.to_sentence_case(), 'Start Case', error_string.format(11))
        self.assertEqual(self.test_string12.to_sentence_case(), 'Sentence case', error_string.format(12))

    def test_to_lower_case(self):
        error_string = 'Incorrect lower-case in test_string{}'
        self.assertEqual(self.test_string1.to_lower_case(), 'demo()1243: ademostring:sda', error_string.format(1))
        self.assertEqual(self.test_string2.to_lower_case(), 'foof bar baz', error_string.format(2))
        self.assertEqual(self.test_string3.to_lower_case(), 'da', error_string.format(3))
        self.assertEqual(self.test_string4.to_lower_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_lower_case(), 'a', error_string.format(5))
        self.assertEqual(self.test_string6.to_lower_case(), 'a', error_string.format(6))
        self.assertEqual(self.test_string7.to_lower_case(), 'pascalcase', error_string.format(7))
        self.assertEqual(self.test_string8.to_lower_case(), 'camelcase', error_string.format(8))
        self.assertEqual(self.test_string9.to_lower_case(), 'kebab-case', error_string.format(9))
        self.assertEqual(self.test_string10.to_lower_case(), 'snake_case', error_string.format(10))
        self.assertEqual(self.test_string11.to_lower_case(), 'start case', error_string.format(11))
        self.assertEqual(self.test_string12.to_lower_case(), 'sentence case', error_string.format(12))

    def test_to_upper_case(self):
        error_string = 'Incorrect upper-case in test_string{}'
        self.assertEqual(self.test_string1.to_upper_case(), 'DEMO()1243: ADEMOSTRING:SDA', error_string.format(1))
        self.assertEqual(self.test_string2.to_upper_case(), 'FOOF BAR BAZ', error_string.format(2))
        self.assertEqual(self.test_string3.to_upper_case(), 'DA', error_string.format(3))
        self.assertEqual(self.test_string4.to_upper_case(), '', error_string.format(4))
        self.assertEqual(self.test_string5.to_upper_case(), 'A', error_string.format(5))
        self.assertEqual(self.test_string6.to_upper_case(), 'A', error_string.format(6))
        self.assertEqual(self.test_string7.to_upper_case(), 'PASCALCASE', error_string.format(7))
        self.assertEqual(self.test_string8.to_upper_case(), 'CAMELCASE', error_string.format(8))
        self.assertEqual(self.test_string9.to_upper_case(), 'KEBAB-CASE', error_string.format(9))
        self.assertEqual(self.test_string10.to_upper_case(), 'SNAKE_CASE', error_string.format(10))
        self.assertEqual(self.test_string11.to_upper_case(), 'START CASE', error_string.format(11))
        self.assertEqual(self.test_string12.to_upper_case(), 'SENTENCE CASE', error_string.format(12))

if __name__ == '__main__':
    unittest.main()
