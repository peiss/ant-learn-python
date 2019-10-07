
data = {
    "a":12,
    "b":12.34,
    "c":None,
    "d":True,
    "e":False,
    "f":[1,2,"abc"],
    12:"abc"
}

import json

json_str = json.dumps(data)

print(json_str)
print(type(json_str))

with open("output.json", "w") as fout:
    fout.write(json_str)