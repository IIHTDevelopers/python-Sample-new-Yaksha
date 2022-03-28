import json
class TestCaseResultDto:
    methodName = ""
    methodType = ""
    actualScore = 0
    earnedScore = 0
    status = ""
    isMandatory = True
    erroMessage = ""

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)