# Exception Handling:
# 1):Exception Handling allows a program to handle unexpected errors during execution in a controlled way.
# 2): instead of crashing abruptly It enables programs to :
#  a) :detect errors
#  b) :manage them properly
#  c) :continue execution wherever possible
# 3):Handles runtime errors such as invalid input
# 4):file not found
# 5):division by zero
# 6):type mismatches that occur during program execution.
# 7) Improves reliability.


# syntax :
#  try:   Runs the risky code that might cause an error.
#        # Code 
#  except SomeException:  Catches and handles the error if one occurs
#        # Code 
#  else:     Executes only if no exception occurs in try.
#       # Code 
#  finally:   Runs regardless of what happens useful for cleanup tasks like closing files
#      # Code 

# try:
#     n = 0
#     res = 100 / n
#     
# except ZeroDivisionError:
#     print("You can't divide by zero!")
#     
# except ValueError:
#     print("Enter a valid number!")
#     
# else:
#     print("Result is", res)
#     
# finally:
#     print("Execution complete.")


# catching exception.
# try:
#     # This will cause ValueError
#     x = int(0) 
#     inv = 1 / x   # Inverse calculation
    
# except ValueError:
#     print("Not Valid!")
    
# except ZeroDivisionError:
#     print("Zero has no inverse!")

# catching multiple exceptions.
# a = ["10", "twenty", 30]
# try:
#     # 'twenty' cannot be converted to int
#     total = int(a[0]) + int(a[1])  
    
# except (ValueError, TypeError) as e:
#     print("Error", e)
    
# except IndexError:
#     print("Index out of range.")

# catching all handlers and their risks:
# try:
#     # Risky operation: dividing string by number
#     res = "100" / 20 
    
# except ArithmeticError:
#     print("Arithmetic problem.")
    
# except:
#     print("Something went wrong!")


# Raise an Exception:
# We raise an exception using the raise keyword followed by an instance of the exception class that we want to trigger
# We can choose from built-in exceptions 
# define our own custom exceptions by inheriting from Python's built-in Exception class.

# Syntax:
# raise ExceptionType("Error message")

# Example:
# def set(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative.")
#     print(f"Age set to {age}")

# try:
#     set(-5)
# except ValueError as e:
#     print(e)


#      workflow:

#  Function execution
#          ↓
#  Invalid data found
#          ↓
#  raise exception
#          ↓
#  Immediately stop current flow
#          ↓
#  Search for matching except block

# internal happenings of exception handling of above example.

# when python sees.
# raise ValueError("Age cannot be negative.")
# it creates an exception object.
# error = ValueError("Age cannot be negative.")
# and throws it into Python's exception mechanism.
# Execution stops immediately.
# The next line
# print(f"Age set to {age}")  never runs.and enter into new block.


# try:
#     set(-5)
# here python says.
# "Run this code. If something goes wrong, don't crash immediately."
# inside function if age < 0: as it is True, Then, 
# raise ValueError(...), here exception is thrown, 
# Function exits instanly.
# control is returned to nearest matching except.
# Matching Except Block.
# except ValueError as e:
# Python checks:  Was the exception a ValueError? --> yes
# e = ValueError("Age cannot be negative.")
# Now e contains the exception object.



# visual execution flow:
#   try
#    │
#    ▼
#   set(-5)
#    │
#    ▼
#   age < 0 ?
#    │
#    ▼
#   True
#    │
#    ▼
#   raise ValueError(...)
#    │
#    ▼
#   Function stops
#    │
#    ▼
#   except ValueError as e
#    │
#    ▼
#   print(e)


# Error vs Exceptions:
# Error: Issues in the program logic such as SyntaxError, etc. It occurs at compile time.
# Exception: Problems that occur at runtime and can be managed using exception handling (e.g., invalid input, missing files).


# Common built-in Exceptions are:
# 1) : ZeroDivisionError : attempting to divide a number by zero.
# 2) : TypeError: applying an operation to an inappropriate data type.
# 3) : ValueError: function gets an argument of correct type but inappropriate value.
# 4) : IndexError: accessing a list index which is out of range.
# 5) : KeyError : accessing a dictionary key which does not exist.
# 6) : FileNotFoundError: opening a file that does not exists.
