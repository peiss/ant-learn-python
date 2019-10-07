try:
    print("hello 01")
    print(10 / 0)
    print("hello 02")
except ZeroDivisionError as e:
    print("ZeroDivisionError", e)
except Exception as e:
    print("exception", e)
finally:
    print("finally")

print("hello 03")
