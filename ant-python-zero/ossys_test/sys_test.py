import sys

for row in sys.argv:
    print(row)
print(sys.argv)

print("#"*100)
for row in sys.path:
    print(row)

print("#"*100)
sys.exit(0)