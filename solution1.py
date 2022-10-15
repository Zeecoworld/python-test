import json


def get_new_json1():
    with open("data/data_1.json") as json_file:
        json_data = json.load(json_file)
        json_attribute = json_data["message"]
        final_result = json_attribute.values()
        final = {}
        for val in final_result:
            for count, val in enumerate(final_result , start=1):
                final_json = { 
                    f"key_{count}": {
                    "type": f"{type(val).__name__}",
                    "tag": "",
                    "description": "",
                    "required": False}, 
                }
                final.update(final_json)
                with open("schema/result1.json","w") as file:
                    json.dump(final,file)
                    

get_new_json1()
                
                

