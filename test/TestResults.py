import json
class TestResults(dict):
    testCaseResults = ""
    customData = ""

    def __init__(self, testCaseResults, customData):
        dict.__init__(self, testCaseResults = testCaseResults, customData = customData)
    #def toJSON(self):
    #    return json.dumps(self, default=lambda o: o.__dict__,
    #                      sort_keys=True)
