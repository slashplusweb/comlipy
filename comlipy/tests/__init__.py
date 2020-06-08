import unittest

from comlipy.tests.lib.test_ensure import TestEnsure
from comlipy.tests.lib.test_rule_checker import TestRuleChecker


def suite():
    suites_list = []
    loader = unittest.TestLoader()
    suites_list.append(loader.loadTestsFromTestCase(TestEnsure))
    suites_list.append(loader.loadTestsFromTestCase(TestRuleChecker))

    return unittest.TestSuite(suites_list)
