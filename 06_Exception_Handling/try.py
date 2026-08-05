# try: lets u write code that might raise an exception.
# Defination: The try block tells Python: "Execute this code normally, but if an exception occurs, don't terminate the program immediately. First check whether someone knows how to handle it."
# try does NOT prevent exceptions.


# best practices: 
# keep try block as small as possible
# include only code that may actually fail.
# dont use try to hide programing mistakes.
# use clear , focused exception handling.


# practice : 
# print("program started.")

# try:
#     print("inside try block")
#     print(10/0)
# print("program finished.")

# try does not work without except, compile error.


# 2:  ZeroDivisinError:
# Expected Exception: ZeroDivisionError
# Reason: Division by zero is not allowed.
# number = 10
# result = number / 0
# print(result)

# 3: ValueError:
# Expected Exception: ValueError
# Reason: "abc" cannot be converted into an integer.
# age = int("abc")
# print(age)

