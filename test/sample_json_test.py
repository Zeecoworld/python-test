import json


data_set = {"key1":[1,2,3],"key2":[1,2,4]}


json_result = json.dumps(data_set)
with open("sample.json","w") as outfile:
    json.dump(data_set,outfile)
