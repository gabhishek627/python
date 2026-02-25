
#### Task: update sever.conf file to extend "max_connection" from 200 to 500

# use withopen() inbuilt function, which automatically handles the file closure, ensuring cleanup  even if exception occur. 

# syntax: withopen("file" , "r") as file:  OR  ("file" , "w") as file: 

# steps: 1. read the lines in the file, 2. store the file into list/variable , 3. open file in write mode , 4. update max_connection

# Have to pass a new value, so define a function and pass a new value as an argument

def update_server_config(file_path,key,value):
    with open(file_path, "r") as file:
        lines = file.readlines()                       #####reading all the lines, readlines() is inbuilt function on file object 

    with open(file_path, "w") as file:
        for line in lines:
            if key in line: 
                file.write(key + "=" + value + "\n")
        
            else:
                file.write(line)


update_server_config("serabcver.conf","MAX_CONNCTIONS","1000")
