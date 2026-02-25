
#### 0. Declaring Function

def myfunction():
    print("This is my first function")

myfunction()
myfunction()


###########################################################################################################################################

### 1. Function to add 2 numbers

print ("\n")

print("### Function to add 2 numbers")

print("==========================")

def addition(a,b):
    add = a + b 
    return add

a = int(input("First Number:" ))
b = int(input("Second Number:" ))

print( addition(a,b))


###
#Take aways: 
#1. no need to define the variable at the right side with input ()
#2. always call the function based on argumnets at the bottom and then apply print, int etc over that.
#3. Thumb rule/Primary Responsibility: Define the function, then inside it perform the operation and then return. Then at the bottom call the function.
#4. When defining a function uisng def, there will be : at the last.
###

print("\n")
print("\n")


########################################################################################################################################

##### 2. By using the below approach any module(collection of functions) can be imported across the python code any where")

import function1 as basic_function

basic_function  ## calling the original function called functions1.py



#Takeaways:
#1. No closing Bracket after basic_function
#2. Any python program is bydefault a module. 
#3. We can import entire python file as a module or also a one particular function from the python file. (basic_calc.addition())


#########################################################################################################################################


#### 3. Collection of modules is called Packages/Library/SDK
# talking to AWS api, we use boto3 module. 

#### 4. virtual environmnet:
#1. For logical separation
#2. Intsall-> pip install virtualenv ;; create folder -> python -m venv project-abc;; activate -> source project-anc/bin/activate
