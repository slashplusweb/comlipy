import unittest

from .lib.test_ensure import TestEnsure


def suite():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestEnsure)

    return test_suite
