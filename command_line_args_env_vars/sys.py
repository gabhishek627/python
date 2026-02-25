
### addition of 2 numbers using command line argumnets by sys module, sys module is used to perform command line operations to read the value

## i.e. execute theprogram as follows: $ python sys.py 100 multiply 50

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




####
# 1. Env vars: used to hide the secret information that we pass thro' command line argumnets or input()
# 2. env ==> buil in environment variable
# 3. To create ==> export password = "abhishek"
# 4. To read, we have to use os module, that is inbuilt provided by python:
#import os
#.
#.
#.
#os.getenv("password")  ;; to print: print(os.getenv("password"))

# 5. Use case: inside CI/CD pipelines
