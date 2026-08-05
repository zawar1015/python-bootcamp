# except :except is the keyword used to catch and handle exceptions so that program doesn't crash when an error occurs.

# basic syntax : 
# try:
#     # Code that might cause an error
#     number = int("not_a_number") 
# except ValueError:
#     # Code that runs ONLY if a ValueError happens
#     print("Oops! That couldn't be converted to an integer.")


# Common ways to use except:
# 1) catching specific exception(best practice)
# It's always best to specify which exact error you are expecting. This ensures you don't accidentally hide unrelated bugs.
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# 2) : Catching Multiple Exceptions:
# You can handle different types of errors with separate except blocks, or group them together in a tuple.
# Multiple blocks:
# try:
#     file = open("data.txt")
#     value = int(file.read())
# except FileNotFoundError:
#     print("The file doesn't exist.")
# except ValueError:
#     print("The file contents aren't a valid number.")

# Group together.
# try:
#     # Some risky code
#     pass
# except (FileNotFoundError, ValueError):
#     print("Either the file was missing or the value was invalid.")

# 3) Accessing the Error Message (as e):
# try:
#     items = [1, 2, 3]
#     print(items[10])
# except IndexError as e:
#     print(f"Caught an error: {e}")
#     Output: Caught an error: list index out of range


# execution flow with except.
# print("Program Started")
# try:
#     print("Inside try")
#     print(10 / 0)
#     print("This will never execute")
# except:
#     print("Exception handled")
# print("Program Finished")

# note : as u enter the  try monitoring started.
# for example ZeroDivisionError is raised.
# execution is stoped immediately , not completely but execution of the current block is stoped and execution of except block started.
# after the try except block python start normal execution.

# visual diagram of try-except.
#  Start
#     │
#     ▼
#  Enter try
#     │
#     ▼
#  Run Statement
#     │
#     ▼
#  Exception?
#   ┌───────┐
#   │  No   │────────────► Continue normally
#   └───────┘
#        │
#       Yes
#        │
#        ▼
#  Search except
#        │
#        ▼
#  Execute except
#        │
#        ▼
#  Continue Program

# practice 

print("=== Example 01 ===")

try:
    result=10/0
except ZeroDivisionError:
    print("a number cannot be divide by 0")

print()

print("=== Example 02 ===")

try:
    age = int(input("Enter age : "))
    print(f"ur age is {age}")
except ValueError:
    print("invalid input.")

print()