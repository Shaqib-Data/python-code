                  # introduction 

print("Hello, World!")
print("Welcome to python")
print("day 1 introduction complete")

                  # python fundamentals

# variables

name = "Alice"
age = 25
height = 5.6

# data types

age = 25
print(age)
print(type(age))

cgpa = 7.12
print(cgpa)
print(type(cgpa))

name = "shaqib"
print(name)
print(type(name))

# typecasting

# Convert string to integer
num_str = "10"
num_int = int(num_str)
print(num_int)  

# Convert integer to string
num = 25
num_str = str(num)
print(num_str)  

# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(pi_int)   

# taking user input

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old.")

# Comments, Escape Sequences & Print Statement

# This is a single-line comment
'''
This is a
multi-line comment
'''

#Common escape sequences:
# \n: Newline
# \t: Tab
# \\: Backslash
# \": Double quote
# \': Single quote

print("Hello\nWorld!")
print("This is a tab\tcharacter.")

# print statement
print("Hello", "World", sep=", ", end="!\n")

# operators

#Arithmetic Operators:
print(10 + 5)   
print(10 ** 2)  

#Comparison Operators:
print(10 > 5)  
print(10 == 5)  

#Logical Operators:
print(True and False)  
print(True or False)  
print(not True)       

#Assignment Operators:
x = 10
x += 5  
print(x)  

#Membership Operators:
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  

#Identity Operators:
x = 10
y = 10
print(x is y)  



