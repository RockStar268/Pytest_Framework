a = 10
b = 1
def while_loop(a, b):
    while a > 0 and b < 10:
        print(str(a) + " " + str(b))
        print("===")
        a = a - 1
        b = b + 1
    else:
        print("Ready with loop")

while_loop(10, 1)
