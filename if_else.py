# decision making: always evaluates to True or False.

# example:
# age = 40
# print(age<32)
# output : False.

# if statment:
# The if statement executes a block only if the condition is True.
# age = 22
# if age>=18:
#     print("eligible for voting .")
# indentations are very important here.
# note : Python uses indentation instead of braces.
# best practice is to use four spaces for each level of indentation.

# if else: 
# if one condition is False and another condition to be processed we use if else.

# syntax:
# if condition:
#     statement
# else:
#     statement

# example:
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor.")


#               flow diagram:
#                Age >= 18?
#                     |
#               +-----+-----+
#               |           |
#              Yes          No
#               |           |
#            Adult        Minor

# example 2) :
# number = 10
# 
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# If condition becomes True, block of code is  executes.
# If False, block of code is skipped.

# advantage: 
# 1): readable(almost descriptive.)
#Disadvantage:
# 1): Every condition introduces branching. 
# 2): Too many branches make code harder to follow.

# values that are considered false in python are :
False
None
0
0.0
''
[]
()
{}
set()
# rest everything is True.

# if []:
#     print("Hello")
# nothing prints.

# name = ""
# if name:
#     print("Valid")   print nothing because ""(empty string) is false.


# elif : when there are multiple conditions we use elif(else if):

# syntax: 
# if condition:
#     statement

# elif condition:
#     statement

# elif condition:
#     statement

# else:
#     statement

# example:
#  balance = 250000
# if balance >= 1000000:
#     print("Platinum Customer")
# elif balance >= 500000:
#     print("Gold Customer")
# elif balance >= 100000:
#     print("Silver Customer")
# else:
#     print("Standard Customer")

# note : wherever the condition is True python stops further checking.(this is main reason of using elif in python.)

# x = 100
# if x > 50:
#     print("A")
# elif x > 20:
#     print("B")
# output : A
# in this example both conditions are true but but the second condtion is not executed.





