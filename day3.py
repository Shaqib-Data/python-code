                      # strings

# Single-quoted string
a = 'Hello, Python!'
print(a)

# Double-quoted string
b = "Hello, World!"
print(b)

# Triple-quoted string (useful for multi-line strings)
c = '''This is
a multi-line
string.'''
print(c)

# string indexing

text = "Python"
print(text[0])
print(text[1])
print(text[-1])
print(text[-2])

# string slicing

text = "Hello, Python!"
print(text[0:5])   
print(text[:5])    
print(text[7:])    
print(text[::2])   
print(text[-6:-1]) 

# step parameter

text = "Python Programming"
print(text[::2])   
print(text[::-1]) 

                   # string methods and functions

# changing case

text = "hello world"
print(text.upper())  
print(text.lower())  
print(text.title())  
print(text.capitalize())  

# removing whitespace

text = "   Hello, World!   "
print(text.strip())  
print(text.lstrip()) 
print(text.rstrip()) 

# finding and replacing

text = "Python is fun"
print(text.find("is"))   
print(text.replace("fun", "awesome")) 

# splitting and joining

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  

new_text = " - ".join(fruits)
print(new_text)

# checking string properties

text = "Python"
print(text.isalpha())  
print(text.isnumeric())  
print(text.isalnum())  

              # Useful Built-in String Functions

#len() - Get Length of a String
text = "Hello, Python!"
print(len(text))  

# ord() and chr() - Character Encoding
print(ord('A'))  
print(chr(65))   

               #String Formatting and f-Strings

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")


