import json
with open("output.json") as fin:
    json_str = fin.read()

    print(json_str)
    print(type(json_str))

    py_obj = json.loads(json_str)

    print(py_obj)
    print(type(py_obj))