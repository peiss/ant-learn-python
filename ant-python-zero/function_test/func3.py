
def func(a,b,c=111):
    print(f"{a}, {b}, {c}")


func(1,2,3)
func(1,2)

func(a=123, b=456, c=789)
func(b=456, a=123, c=789)