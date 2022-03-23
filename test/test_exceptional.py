import unittest
import sys
sys.path.append("..")
from count_chars import count_characters
from dateandday import get_week_day
from test.TestUtils import TestUtils


class ExceptionalTest(unittest.TestCase):

    def test_type_error_for_count(self):
        test_obj = TestUtils()
        try:
            count_characters("15")
            test_obj.yakshaAssert("TestTypeErrorForCount", True, "exception")
            print("TestTypeErrorForCount = Passed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForCount", False, "exception")
            print("TestTypeErrorForCount = Failed")

    def test_type_error_for_day(self):
        test_obj = TestUtils()
        try:
            get_week_day("12-5-2021")
            test_obj.yakshaAssert("TestTypeErrorForDay", True, "exception")
            print("TestTypeErrorForDay = Passed")
        except TypeError:
            test_obj.yakshaAssert("TestTypeErrorForDay", False, "exception")
            print("TestTypeErrorForDay = Failed")
