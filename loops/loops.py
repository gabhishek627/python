

### for loop syntax: 

for i in range(10):
    print("Hello! there!")



#### declare a list using for loop:

colors = ["yellow", "red", "pink"]

for i in colors:
    print(i)



### While loop: used whenever there is no idea how many times the loop will be executed.
# use case: 1. print ("deleted") till all the files in particular folder is deleted 
# 2. while kubectl get deploy , print("pod name: ")



## Loop Control Statements/Manipulation:

# break -> used to termintate a loop 

numbers = [1,2,3,4,5]
for number in numbers:
    if number == 3:
        break
    print (number)     #### O/p: 1 & 2 only



# continue -> used to skip the current iteration of loop and proceed for next task. i.e. bypass certailcertain iteration


numbers1 = [1,2,3,4,5]
for number in numbers1:
    if number == 3:
        continue
    print(number)       #### O/P :  1 2 4 5 
