import os
from typing import List


class Color:
    COLORS = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37,
        'grey': 90
    }
    ATTRIBUTES = {
        'bold': 1,
        'dark': 2,
        'underline': 4,
        'blink': 5,
        'reverse': 7,
        'concealed': 8
    }
    RESET = '\033[0m'

    @staticmethod
    def colorize(text: str, color: str = None, attrs: List[str] = None):
        """
        Colorize a string

        Available colors:
            black, red, green, yellow, blue, magenta, cyan, grey, white

        Available attrs:
            bold, dark, underline, blink, reverse, concealed

        Examples:
            colored('Foo Bar Error!', 'red', ['bold', 'underline'])
            colored('Foo Bar Success!', 'green')
        """
        if os.getenv('ANSI_COLORS_DISABLED') is None:
            fmt_str = '\033[{0:d}m{1:s}'
            if color is not None:
                text = fmt_str.format(Color.COLORS[color], text)

            if attrs is not None:
                for attr in attrs:
                    text = fmt_str.format(Color.ATTRIBUTES[attr], text)

            text += Color.RESET
        return text

    @staticmethod
    def print(text: str, color: str = None, attrs=None, **kwargs):
        """
        Print a colorized string

        Available colors:
            black, red, green, yellow, blue, magenta, cyan, grey, white

        Available attrs:
            bold, dark, underline, blink, reverse, concealed
        """
        print((Color.colorize(text, color, attrs)), **kwargs)
