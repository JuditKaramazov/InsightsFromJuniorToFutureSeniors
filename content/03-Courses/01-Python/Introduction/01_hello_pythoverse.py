############################################
# 01. Introduction to PythoVerse
############################################

"""
Welcome to PythoVerse and the world of Python programming! 
This brief course will guide you through the fundamentals 
of Python - step by step. Let's get started!
"""

############################################

# Welcome message
print("Hello PythoVerse Learners!")
print("Welcome to the world of Python programming.")

# Single-line comment
# This is a single-line comment in Python. Comments are ignored by the Python interpreter.
# They are useful for adding notes or explanations within your code.

############################################

# Multi-line comment
"""
This is a multi-line comment in Python. 
You can use triple quotes (''' or three double ones, just like I did above) to create multi-line comments.
Multi-line comments are often used for docstrings (documentation strings) and larger explanations.
"""

############################################

# Data type examples
# In Python, data types represent different kinds of values that can be used in a program.
# Here are some examples:

# String data type
name = "John Doe"  # A sequence of characters
print("Name:", name)
print("Data type:", type(name))
# Explanation: Strings are used to represent text data in Python.

# Integer data type
age = 25  # A whole number
print("Age:", age)
print("Data type:", type(age))
# Explanation: Integers are used to represent whole numbers in Python.

# Float data type
height = 1.75  # A decimal number
print("Height:", height)
print("Data type:", type(height))
# Explanation: Floats are used to represent decimal numbers in Python.

# Complex data type
complex_number = 3 + 1j  # A number with a real and imaginary part
print("Complex Number:", complex_number)
print("Data type:", type(complex_number))
# Explanation: Complex numbers are used to represent numbers with a real and imaginary part in Python.

# Boolean data type
is_python_fun = True  # A value representing true or false
print("Is Python fun?", is_python_fun)
print("Data type:", type(is_python_fun))
# Explanation: Booleans are used to represent true or false values in Python.

# NoneType data type
result = print("My string")  # A special value representing absence of value
print("Result:", result)
print("Data type:", type(result))
# Explanation: NoneType is used to represent the absence of a value in Python.

############################################

# Type() function.
# Would you want to check what's the data type of certain elements?
# Try to print it by inserting the data inside of type() parenthesis, then.
print(type("I am a string"))    # Outputs: <class 'str'>
print(type(5))                  # Outputs: <class 'int'>
print(type(1.5))                # Outputs: <class 'float'>
print(type(3 + 1j))             # Outputs: <class 'complex'>
print(type(True))               # Outputs: <class 'bool'>
print(type(print("My string"))) # Outputs: <class 'NoneType'>

############################################

# That's a wrap-up! If these concepts still feel somehow odd, do not worry about it.
# Also, and for clarity purposes, remember that you can follow fantastic videos and examples here:
# https://www.youtube.com/watch?v=qwAFL1597eM
# Happy coding!

############################################
