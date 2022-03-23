
import unittest
import sys
sys.path.append("..")
from count_chars import count_characters
from dateandday import get_week_day

from test.TestUtils import TestUtils


class FuctionalTests(unittest.TestCase):

    def test_is_array(self):
        obj = count_characters("Karthik Age Is 18 @2021")
        test_obj = TestUtils()
        if type(obj)==type([]):
            test_obj.yakshaAssert("TestIsArray", True, "functional")
            print("TestIsArray = Passed")

        else:
            test_obj.yakshaAssert("TestIsArray", False, "functional")
            print("TestIsArray = Failed")

    def test_is_str(self):
        obj=get_week_day("12-5-2021")
        test_obj = TestUtils()
        if type(obj)==type(" "):
            test_obj.yakshaAssert("TestIsString", True, "functional")
            print("TestIsString = Passed")
        else:
            test_obj.yakshaAssert("TestIsString", False, "functional")
            print("TestIsString = Failed")

    def test_to_count_characters(self):
        obj=count_characters("Karthik Age Is 18 @2021")
        test_obj = TestUtils()
        if obj!=None:
            if obj[0]==9 and obj[1]==3 and obj[2]==6 and obj[3]==1:
                test_obj.yakshaAssert("TestToCountCharacters", True, "functional")
                print("TestToCountCharacters = Passed")
            else:
                test_obj.yakshaAssert("TestToCountCharacters", False, "functional")
                print("TestToCountCharacters = Failed")
        else:
            test_obj.yakshaAssert("TestToCountCharacters", False, "functional")
            print("TestToCountCharacters = Failed")

    def test_is_day(self):
        day=get_week_day("12-9-2021")
        test_obj = TestUtils()
        if day=="Sunday":
            test_obj.yakshaAssert("TestIsDay", True, "functional")
            print("TestIsDay = Passed")
        else:
            test_obj.yakshaAssert("TestIsDay", False, "functional")
            print("TestIsDay = Failed")
