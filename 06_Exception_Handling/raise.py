# raise: raise is used to deliberately generate an exception.
# basic syntax:
# raise ExceptionType("Message")

# example:
# age validation:
# age = int(input("Enter ur age."))
# if age<0:
#     raise ValueError("age cannot be zero.")
# print(age)


# execution flow of real life use of using raise:
#    Input
#    
#    ↓
#    
#    Business Rule
#    
#    ↓
#    
#    Valid?
#    │
#    ├── Yes → Continue Program
#    │
#    └── No
#          │
#          ▼
#        raise
#          │
#          ▼
#    Exception Generated


# raise zerodivision error:
# def divide(a,b):
#     if b==0:
#         raise ZeroDivisionError("denominator cannot be zero.")
#     return a/b
# print(divide(10,0))


# combining raise with try:

# try:
#     age = int(input("Enter age : "))
#     if age < 0:
#         raise ValueError("age cannot be negative")
# except ValueError as error:
#     print(error)



# Best Practices

#  Validate inputs at the start of functions.
#  Use meaningful exception types.
#  Write clear, descriptive messages.
#  Raise exceptions for invalid states, not normal conditions.
#  Keep validation close to the code it protects.




# practice :

# def withdraw(balance,amount):
#     if amount<=0:
#         raise ValueError("withdrawl amount cannot be negative or zero.")
#     if amount>balance:
#         raise ValueError("withdrawl amount cannot be greater than balance")

#     return balance - amount


# try:
#     balance =10000
#     amount = int(input("Enter withdrawl amount :"))
#     balance= withdraw(balance,amount)
#     print(f"Remaining balance  Rs. {balance}" )
# except ValueError as e:
#     print("Transaction failed.")
# finally:
#     print("thanks")


def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than 0.")

    if weight <= 0:
        raise ValueError("Weight must be greater than 0.")

    bmi = weight / (height ** 2)
    return bmi


try:
    weight = float(input("Enter weight (kg): "))
    height = float(input("Enter height (m): "))

    bmi = calculate_bmi(weight, height)

    print(f"BMI: {bmi:.2f}")

except ValueError as e:
    print(f"Error: {e}")