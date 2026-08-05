# else : It executes only if the code inside the try block runs successfully without raising any exceptions.
# why we use else  separate from try:
# goal of try block is to isolate code which is expected to raise an error.
# if we add else block code to try  , it may raise some issues which are not intended.


# try : runs alway. holds code that might trigger an error.
# except: execute only if an exception occure in try.
# else : execute when try block execute without raising an error.


# flow visualization:
#           try
#            │
#            ▼
#    Exception Occurred?
#       │          │
#      Yes         No
#       │          │
#       ▼          ▼
#    except      else
#       │          │
#       └────┬─────┘
#            ▼
#      Continue Program


# example :
# 1) : 
# try:
#     number = int(input("enter a number : "))
#     result = 100/number
# except (ValueError,ZeroDivisionError):
#     print("enter valid integer other than zero .")

# else:
#     print(f"result : {result}")

# in above code i used two exceptions combinely cz they have identical response.



# internal working:
#   Enter try
#     ↓
#   Execute Line 1
#     ↓
#   Execute Line 2
#     ↓
#   Any Exception?
#   if YES
#     ↓
#   Jump to except
#   if NO
#     ↓
#   Run else

# import pandas as pd
# try:
#     df = pd.read_csv("sales.csv")
# except FileNotFoundError:
#     print("Dataset not found.")
# else:
#     print("Dataset loaded successfully.")
#     print(df.head())

# data set not found (output)



# 