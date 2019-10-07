
data = set()

with open("input.txt") as fin:
    for line in fin:
        line = line.strip()
        fields = line.split("\t")
        name = fields[0]
        data.add(name)

for name in data:
    print(name)