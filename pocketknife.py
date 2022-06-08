import json
def is_json(myjson):
    try:
        json.loads(myjson)
    except Exception as e:
        return False
    return True

def print_json_structure(ejson):
    for key in ejson:
        print(key)
        if(is_json(ejson[key])):
            for key2 in ejson[key]:
                print(" - ", key2)
        elif(isinstance(ejson[key], list)):
            print("[ ")
            for x in range(0, len(ejson[key][key2])):
                print("     ", ejson[key][key2][x])
        elif(isinstance(ejson[key], dict)):
            for key2 in ejson[key]:
                print(" - ", key2)
        else:
            print(type(ejson[key]))
