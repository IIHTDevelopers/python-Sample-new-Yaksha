import unittest
import sys
sys.path.append("..")
from dateandday import get_month_days
from test.TestUtils import TestUtils

class BoundaryTest(unittest.TestCase):

    def test_month_not_in_range(self):
        x=get_month_days(15,2021)
        test_obj = TestUtils()
        if x==-1:
            test_obj.yakshaAssert("TestMonthNotInRange", True, "boundary")
            print("TestMonthNotInRange = Passed")
        else:
            test_obj.yakshaAssert("TestMonthNotInRange", False, "boundary")
            print("TestMonthNotInRange = Failed")

    def test_month_in_range(self):
        x=get_month_days(4,2021)
        test_obj = TestUtils()
        if x!=-1:
            test_obj.yakshaAssert("TestMonthInRange", True, "boundary")
            print("TestMonthInRange = Passed")
        else:
            test_obj.yakshaAssert("TestMonthInRange", False, "boundary")
            print("TestMonthInRange = Failed")
