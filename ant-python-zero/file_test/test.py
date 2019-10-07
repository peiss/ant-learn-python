fin = open("input.txt")

min = 10000
max = 0
sumv = 0
count = 0
for line in fin:
    number = int(line.strip())
    if number<min:
        min = number
    elif number>max:
        max = number
    sumv += number
    count +=1

print("max value:",max)
print("min value:",min)
print("avg value:",sumv/count)

fout = open("output.txt","w")
fout.write("max value:"+str(max)+"\n")
fout.write("min value:"+str(min)+"\n")
fout.write("avg value:"+str(sumv/count)+"\n")

fin.close()
fout.close()