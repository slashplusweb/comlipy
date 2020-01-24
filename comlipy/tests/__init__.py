import unittest

from .ensure_test import EnsureTest


def suite():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(EnsureTest)

    return test_suite
