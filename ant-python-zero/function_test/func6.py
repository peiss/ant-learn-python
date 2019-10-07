
x = 123
def func():
    global x
    x = 100
    print(x)


func()
print(x)