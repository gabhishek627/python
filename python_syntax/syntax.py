### points to remember:

# 1.Python is case sensitive
# 2. Python statements do not end with a semicolon, but you can use one to separate two statements
# 3. All lines in a Python application must begin in the first column, unless the statement is in the body of a loop, conditional, function, or class definition.
#    • Python relies on indentation to determine the control flow structure of an application.
#    • As we introduce control structures, we will revisit the indentation rules.
#    • Line indentation is typically a multiple of four spaces.

#      You can continue a long statement by placing the \ character at the end of the line.
#          • When used in this fashion it is often referred to as the line continuation character.
#  
# 4. Statements continue onto the following line(s) when reaching the end of the line before the closing character for any of the following pairs of characters.
# () [] {}


# 5. We indicate the arguments to the print() function using commas, and Python ignores the additional white spaces. Although not recommended, Python allows any number of white space characters between the opening and closing parenthesis, which do not need to comply with indentation rules.



#Simple Output
 # We have demonstrated the print() function in several forms in previous examples. 
 #• This function takes zero or more arguments, separated by commas, and displays the data.
 # • The default behavior of the function is:
# – When there is more than one argument, print() displays each of the arguments separatedby a single space.

# – print() displays a new line after the last parameter.
 #   You can alter the default behavior by providing the following optional named arguments.
 #     • sep
 #        – Separator character to display between arguments.
 #     • end
 #        – Character to display after the last parameter.
 #     • file
 #        – File to output the arguments.

1. 
message ="This is a long string just to \
illustrate continuation across multiple lines"


result = 500 *2 + \
400*3

print(message)
print(result)


data = "This is just a string of text"
print("This is first argument","This is 2nd argument",data)



O/P:
This is a long string just to illustrate continuation across multiple lines
2200
This is first argument This is 2nd argument This is just a string of text


2. 
>>> response = input("Please enter some text:")
Please enter some text:hari
>>> response1 = input("Please enter sirname:")
Please enter sirname:sadu
>>> 
>>> print("The name of boy is", response, response1, sep=",")
The name of boy is,hari,sadu


3. 
The following example shows how the function returns a string even when the user introduces
numbers:
$ python3
Python 3.9.10 (main, Feb 9 2022, 00:00:00)
[GCC 11.2.1 20220127 (Red Hat 11.2.1-9)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> response = input("Please enter a number: ")
Please enter a number: 456
>>> print("The response of", response, "is of type", type(response))
The response of 456 is of type <class 'str'>
>>> exit()



4. 

