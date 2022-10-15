### Unit Test case for validating the given JSON FILES and JSON FILE Result
import json






def validateJSON(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

