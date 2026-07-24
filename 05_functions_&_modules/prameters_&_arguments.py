# A parameter is a variable declared in the function definition that receives data when the function is called.
# An argument is the actual value passed into the function.

# Example:
# when python see:
# def greet(name):
#     print(name)
# greet("zawar")

# name is parameter.
# zawar is argument.

# parameter : local variable. exist only during function call.
# Parameters were invented to make functions reusable.
# Without parameters, a function could only work with fixed data. Parameters allow the same function to work with different inputs.
# Reusable
# Independent
# Easy to test
# Easy to understand
# Thread-safe in many situations because each call has its own local variables
# Parameters were invented to make functions reusable and independent of specific data
# They allow the same function to operate on different inputs instead of hard-coded values or global variables.
# Each function call gets its own local parameters inside a new stack frame.
# improves modularity, readability, testing, and maintainability while avoiding hidden dependencies.


# note:function defines what to do; parameters define what data to do it with.



# Use meaningful parameter names
# Keep the number of parameters reasonable
# One function should solve one problem# 
# Write reusable functions
# Avoid unnecessary duplication.


# code:
# Greeting a user by name.
# def greet(name):
#     print(f"hello!  {name}")

# greet("allauddin bangash")

# print("\n------------------------------")

# calculating the square of a number.
# def square(number):
#     answer = number*number
#     print(answer)
# square(90)
# output : 8100

# Calculating the area of a rectangle.

# def rec_area(length,width):
#     area = length*width
#     print(area)
# rec_area(23,89)
# output: 2047

# Finding the larger of two numbers.

# def find_large(num1,num2):
#     if num1>num2:
#         print(num1)
#     elif num2==num1:
#         print("both numbers are equal.")
#     else:
#         print(num2)
# find_large(19,1)


# Printing student information (name, age, department)
# def student_info(name,age,department):
#     print(name,age,department)
# student_info("zawar",21,"cs")






 

