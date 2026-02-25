import sys
import sys

def addition(a,b):
    s=a+b
    return s


def sub(a,b):
    s=a-b
    return s


def mul(a,b):
    s=a*b
    return s

a = int(sys.argv[1])
o = sys.argv[2]
b = int(sys.argv[3])


if o == "add":
    print("The addition is:" , addition(a,b))

elif o == "minus":
    print("The subtraction is: ", sub(a,b))


elif o == "multiply":
    print("The multiplication is:", mul(a,b))

else:
    print("Plase give the valid operation")
