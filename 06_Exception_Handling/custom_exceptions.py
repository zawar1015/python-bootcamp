# custom exception:
# custom exception (or user-defined exception) is a standard class that inherits from Python’s built-in Exception class (or one of its subclasses).
# They are used when Python’s built-in errors (like ValueError or TypeError) are too generic to accurately describe a problem specific to your application's domain logic
# Inheriting a custom exception:
# creating a new error class by extending a language's base exception class or an existing custom exception.
# This lets you group:
# related errors under common base name.
# pass custom messages to parent class.
# add specific fields for debbuging.
# catch broad categoried of errors with single handler.

# how custom exception work in python:
# inherit from built in Exception class.


# basic sytax :
# class AppError(Exception):
#     pass

# class DatabaseError(AppError):
#     pass

# creating custom Exception: is simply creating a class that inherits from Exception.
# as above.

# lets break above syntax:
# 1) : class : creates a new class.
# 2) : AppError: name of my exception.
# 3) : (Exception): inheritance.this telss python that this class acts like an exception.
# 4) : the class has no additional behaviour yet.

# example:

# class InvalidAgeError(Exception):
#     pass

# age = int(input("Enter age : "))
# if age<= 0: 
#     raise InvalidAgeError("Age cannot be negative nor zero.")

# print("valid age")

# note :  exception name far more descriptive than ValueError.

# catching custom exception:

# class InvalidAgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age."))

#     if age <= 0:
#         raise InvalidAgeError("Age cannot be negative not zero.")
# except InvalidAgeError as e:
#     print(e)


# use hierarchy:
# This allows consumers of your code to catch all errors from your application with a single block.
# catch specific errors when fine-grained control is needed.


# adding a constructor:
# To add a constructor to a custom exception in Python:
# you must override the __init__ method and call super().__init__() to ensure the base exception class initializes properly.


# class InvalidAgeError(Exception):

#     def __init__(self, age):
#         self.age = age
#         super().__init__(f"Invalid age: {age}")


# raise InvalidAgeError(-10)


# example: 
# class InsufficientBalanceError(Exception):
#     pass

# def withdraw(balance, amount):

#     if amount > balance:
#         raise InsufficientBalanceError(
#             "Balance is too low."
#         )

#     return balance - amount
# try:
#     balance = withdraw(5000, 7000)
# except InsufficientBalanceError as error:
#     print(error)

# API  example: 

# class InvalidTokenError(Exception):
#     pass

# if token != expected_token:
#     raise InvalidTokenError(
#         "Authentication failed."
#     )


#  Best Practices
#  End custom exception names with Error.
#  Inherit from Exception (or another suitable exception class).
#  Keep exception classes focused on one problem.
#  Write meaningful messages.
#  Use built-in exceptions when they already describe the problem we


