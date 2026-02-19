
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





