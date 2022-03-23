from test.TestResults import TestResults
from test.TestCaseResultDto import TestCaseResultDto
import json
import requests

class TestUtils:
    GUID = "dc66f3c1-630f-40ab-8314-f7bb9ffcb71f"
    URL = "https://yaksha-stage-sbfn.azurewebsites.net/api/TestCaseResultsEnqueue?code=AjU0mofZlYs9oYbZnJpVwJWRY1dRKkDyS3QDY8aJAvrcjJvgBAXVDg=="

    @classmethod
    def yakshaAssert(self, test_name, result, test_type):
        ref = open("./custom.ih", "r")
        customData = ref.read()
        ref.close()
        #print(customData)
        test_results = TestResults()
        test_case_results = dict()

        result_status = "Failed"
        result_score = 0
        if result:
            result_status = "Passed"
            result_score = 1

        test_case_result_dto = TestCaseResultDto()
        test_case_result_dto.methodName = test_name
        test_case_result_dto.methodType = test_type
        test_case_result_dto.actualScore = 1
        test_case_result_dto.earnedScore = result_score
        test_case_result_dto.status = result_status
        test_case_result_dto.isMandatory = True
        test_case_result_dto.erroMessage = ""

        test_case_results[self.GUID] = test_case_result_dto
        test_results.testCaseResults = json.dumps(test_case_results)
        test_results.customData = customData

        final_result = json.dumps(test_results)

        requests.post(self.URL, json=final_result)
