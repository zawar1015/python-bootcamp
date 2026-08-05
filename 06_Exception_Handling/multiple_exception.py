# first approach:
# try:
#     number = int(input("Enter a number: "))
#     print(100 / number)

# except ValueError:
#     print("Please enter numbers only.")

# except ZeroDivisionError:
#     print("Number cannot be zero.")

# note : 
# two exceptions are possible in program , 
# 1) : if u enter string instead of number , in this case python will catch valueError.
# 2) : ZeroDivisionError: if u enter 0  except will catch ZeroDivisionError.


# if "abc" is entered: workflow is :
#    Enter try
#        │
#        ▼
#    int("abc")
#        │
#        ▼
#    ValueError
#        │
#        ▼
#    Check first except
#        │
#    Matches
#        │
#        ▼
#    Execute it


# now suppose 0 is enter

#   Enter try
#       │
#       ▼
#   int("abc")
#       │
#       ▼
#   ValueError
#       │
#       ▼
#   Check first except
#       │
#   Matches
#       │
#       ▼
#   Execute it

# python checks except block from to bottom.
# only one except block can runs.


# Catching multiple Exceptions together.
# except (ValueError, TypeError): tuple of exception classes.
#     print("Invalid input")
# we can use combine exceptions if the response is identical.

# below two exceptions cannot be combine becase they are completely different problems.
# except (FileNotFoundError, ZeroDivisionError):
#     print("Something went wrong.")


# practice codes:
# 1) : 
# try: 
#     age = int(input("enter age : "))
#     print(100/age)
# except ValueError:
#     print("enter numeric value.")
# except ZeroDivisionError:
#     print("number cannot be divide by zero.")

# 2) : 
# numbers = [10,20,30]
# try:
#     index = int(input("enter index : "))
#     print(numbers[index])
# except ValueError:
#     print("enter numerical value.")
# except IndexError:
#     print("index out of range.")


# 3) :
# import pandas as pd
# try:
#     df= pd.read_csv("sales.csv")
#     print(df["profit"].mean())
# except FileNotFoundError:
#     print("file not found .")
# except KeyError:
#     print("column not found")
    

