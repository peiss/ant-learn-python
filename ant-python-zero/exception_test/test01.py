
try:
    print("hello 01")
    #print(10/0)
    print("hello 02")
except ValueError as e:
    print("ValueError", e)
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
finally:
    print("finally")
print("hello 03")