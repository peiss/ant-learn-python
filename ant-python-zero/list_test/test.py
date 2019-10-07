# example 1
result = []
for i in range(10):
    if i%2==0:
        result.append(i*i)
print(result)

result2 = [i*i for i in range(10) if i%2==0]
print(result2)

# example 2
data = [1,2,3,4]
result3 = "\t".join([str(x) for x in data])
print(result3)

# example 3
fin = open("test.txt")
ids = [str(line).split("\t")[0] for line in fin if len(line.strip())>0]
print(ids)
fin.close()