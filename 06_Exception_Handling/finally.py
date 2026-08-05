# finallyL  is the part of exception handling that always executes, whether:
# an exception occurs or not,
# the exception is caught or not,
# a return statement is executed,
# a break or continue happens.

# In Python's exception handling, the finally block is the ultimate cleanup crew.
# finally contain code that is guaranteed to run eather exception was raised,cought or completely ignored.


# Basic Syntax:
# try:
#     # risky code
# except Exception:
#     # handle error
# finally:
#     # always runs

# try:
#     print("Inside try")
# except ValueError:
#     print("Inside except")
# finally:
#     print("Inside finally")

# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("number cannot be divide by zero.")
# finally:
#     print("will always run")

# behaviour of finally in different scenarios.

# Scenario              Does try run?    Does except run?   Does else run?   Does finally run?
# No errors occur           Yes          No                   Yes              Yes
# Expected error occurs     Yes          Yes                  No               Yes
# Unhandled error occurs    Yes          No                   No               Yes (runs before crashing)
# return statement hit      Yes          Depends              Depends          Yes (runs before returning)

# note : code inside finaaly will execute even if try or except contain return .

# def check_value(x):
#     try:
#         if x > 0:
#             return "Positive"
#         return "Negative or Zero"
#     finally:
#         print("I run BEFORE the function actually returns!")

# print(check_value(5))


# try:
#     file = open("data.txt")
#     data = file.read()
# except FileNotFoundError:
#     print("File not found")
# finally:
#     file.close()


# try:
#     print(10 / 0)
# finally:
#     print("Cleanup")
# output:
# Cleanup
# Traceback...
# ZeroDivisionError

# Exception occurred.
# finally executed.
# Exception continued upward because nobody caught it.


# def demo():
#     try:
#         return 10
#     finally:
#         print("Finally executed")

# print(demo())
# output:
# Finally executed
# 10

# Even though return happened, finally ran first.

# Python internally behaves like:
# store return value
#   ↓
# run finally
#   ↓
# return stored value


# def demo():
#     try:
#         return 10
#     finally:
#         return 20

# print(demo())
# Output: 20
# The return in finally overrides the earlier return.


# Exception in try + Return in finally:
# def demo():
#     try:
#         raise ValueError("Error")
#     finally:
#         return "Done"
# print(demo())
# Output: Done
# No exception is shown.
# The return in finally suppresses the exception.


# Exception in finally:
# try:
#     print("Try block")
# finally:
#     raise RuntimeError("Error in finally")
# Output:
# Try block
# RuntimeError: Error in finally
# The exception from finally replaces the normal flow.


#  Multiple Excepts + Finally:
# try:
#     age = int(input("Age: "))
#     if age < 0:
#         raise ValueError("Negative age")
# except ValueError as e:
#     print("ValueError:", e)
# except TypeError as e:
#     print("TypeError:", e)
# finally:
#     print("Validation finished")
# no matter what the user enters.
# finally will execute.
# output: Validation finished