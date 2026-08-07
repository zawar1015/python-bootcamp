# An exception object is a specific instance of an exception class (such as ValueError, KeyError, or a custom class) that Python creates at the exact moment an error occurs during runtime.
# When an error is triggered, Python creates this object in memory, populates it with details about what went wrong, and "raises" it up through your code until it is either caught by an except block or crashes the program.


# Capturing the Exception Object (as e):
# To inspect an exception object, you capture it using the as keyword in an except block.
# Exception objects are standard class instances, they contain built-in attributes and methods that provide details about the runtime failure.

# example: 
# try:
#     number = int("abc")

# except ValueError as error:
#     print(error)
# here error is not just text its object.
# type(error): <class 'ValueError'>

# visulaization: 
#             Exception Object
#  
#   ┌─────────────────────────────┐
#   │ Type → ValueError           │
#   │ Message → Invalid Input     │
#   │ Args → ("Invalid Input", )  │
#   └─────────────────────────────┘

# as keyword:
# syntax: except ExceptionType as variable:

# example:
# try:
#     number = int("abc")

# except ValueError as error:
#     print(error)

# printing object:
# try:
#     int("abc")

# except ValueError as error:
#     print(error)
# output: invalid literal for int() with base 10: 'abc'.

# using repr():
# try:
#     int("abc")

# except ValueError as error:
#     print(repr(error))
# output: try: ValueError("invalid literal for int() with base 10: 'abc'")
# repr() shows the object representation instead of only the message.

# exception Attributes:
# .args
# try:
#    raise ValueError("Age cannot be negative.")
#
#except ValueError as error:
#    print(error.args)
# ('Age cannot be negative.',)
# notice : .args return tuple.

# multiple arguments:
# try:
#     raise ValueError("Age Error", 25)
# 
# except ValueError as error:
#     print(error.args)
# output: ('Age Error', 25)
# exception can store more than one variable.


# accessing individual arguments:
try:
    raise ValueError("Age Error", 25)

except ValueError as error:
    print(error.args[0])
    print(error.args[1])

# output: 
# Age Error
# 25

# Exception object flow:
#  Raise Exception
#    ↓
#  Create Exception Object
#    ↓
#  Store Information
#    ↓
#  except as error
#    ↓
#  Inspect Object
#    ↓
#  Take Action


# remaining topics:
#   5.12 Logging
#   5.13 Debugging & Tracebacks
#   5.14 Exception Handling Best Practices
#   5.15 Data Science Error Handling
#   5.16 Capstone Project