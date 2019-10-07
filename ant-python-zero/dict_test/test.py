
"""
result[course][max/min/sum/count]
result["语文"]["max"] = 99
result["语文"]["min"] = 75
result["语文"]["sum"] = 800
result["语文"]["count"] = 10
result["数学"]["max"] = 10
result["数学"]["min"] = 10
result["数学"]["sum"] = 10
result["数学"]["count"] = 10
"""
result = {}

with open("input.txt") as fin:
    for line in fin:
        line = line.strip()
        fields = line.split("\t")
        name, course, grade = fields
        if course not in result:
            result[course] = {}
            result[course]["max"] = 0
            result[course]["min"] = 999
            result[course]["sum"] = 0
            result[course]["count"] = 0

        grade = int(grade)
        if grade > result[course]["max"]:
            result[course]["max"] = grade
        elif grade < result[course]["min"]:
            result[course]["min"] = grade
        result[course]["sum"] += grade
        result[course]["count"] += 1

for key, value in result.items():
    print(key, value)

    out_fields = [
        key,
        value["max"],
        value["min"],
        value["sum"]/value["count"]
    ]
    print(out_fields)