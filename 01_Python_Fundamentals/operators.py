# operator  : An operator is a symbol that tells Python to perform an operation.


# Types of Operators:
# There are seven major categories.



# Arithmetic
# a = 45
# b = 12

# print(a+b) # add
# print(a-b) # subtract
# print(a*b) # multiplication
# print(a/b) # division : always returns float
# print(a//b)# floor division : ignors the decimal part
# print(a%b) # modulus : returns reminder
# print(a**2)# exponent : a power 2



# Assignment operator: Assignment operators are used to assign values to variables.
# assign "="
# add and assign "+="
# subtract and assign "-="
# multiply and assign "*="
# divide and assign "/="
# modulus and assign "%="
# exponent and assign "**="
# floor_divide and assign "//="
# bitwise and assign "&="
# bitwise OR and  assign "`="
# bitwise XOR and assign "^="
# leftshift and assign "<<="
# rightshift and assign ">>="
 
# salary = 223
# print(salary)
# salary +=200
# print(salary)
# salary-=100
# print(salary)
# salary*=100
# print(salary)
# salary/=100
# print(salary)
# salary%=100
# print(salary)
# salary**=100
# print(salary)
# salary//=100
# print(salary)



# Comparision  TRUE OR FALSE

# exactly equal to "=="
# not equal to "!="
# less than "<"
# lessthan or equal to "<="
# greaterthan ">"
# greater than or equal to ">="

# print(5 == 5)
# print(5 != 3)
# print(10 < 8)
# print(20 >= 20)
# print(15 <= 20)



# Logical Operators : use when checking multiple conditions

# 1: AND : return TRUE when both conditions are TRUE
# age = 25
# salary = 70000
# print(age > 18 and salary > 50000)

# 2: OR  : return TRUE when any of two  conditions is TRUE
# print(age > 18 or salary > 100000)

# 2: NOT : reverse the result
# is_student = True

# print(not is_student)

# NOTES: Short-Circuit Evaluation: Python stops evaluating as soon as it knows the final answer.
# It improves performance and avoids unnecessary or potentially dangerous computations.

# x = 5
# if x > 10 and (10 / 0) > 1:
#     print("Hello")

# x > 10 is False.
# Python never evaluates (10 / 0).
# No error occurs.
# Does not print "Hello"

# TRADEOFFS : 
# Faster execution.
# Prevents unnecessary computations.
# Can hide bugs if you expect the second expression to run.
# More variables = slightly more code.
# Better readability and easier debugging.


# real life example  of logical operator.
# loan approval:
# Age >18
# Income >30000
# Credit Score >700
# Python combines all of these using logical operators.

# precedence between AND and OR:
# and has higher precedence than or.



# Identity operator:
# Identity operators are used to check whether two variables refer to the same object in memory, not whether they have the same value.

# Returns True if both variables point to the same object.
# 1: is    : Returns True if both variables point to the same object.
# 2: is not: Returns True if both variables point to different objects.

# is vs "==":
# == checks value equality.
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a == b)
# it returns True because both valus are same and "==" checks equality .
# "is" checks object identity
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)
# it prints False because they have different identity , they are stored at diffent locaton in memory although their valus are same.
# a = [1, 2, 3]
# b = a
# print(a is b)
# it prints True because both variables point to the exact same object.

# Design Tradeoffs & Consequences:
# 1: Using == vs is :
# using "=="
# if user_input == expected_value:
#     print("Match")

# Consequence

# Compares contents/values.
# Usually what you want for strings, numbers, lists, etc.
# Slightly more work because Python compares values.
# using "is":
# if user_input is expected_value:
#    print("Match")

# Consequence:

# Compares memory addresses (object identity).
# Can produce unexpected results.
# Often a bug when used instead of ==.

# Note:  we use "is" when checking whether two references point to the same object, especially with None.
# None is a singleton object in Python.

# Tradeoffs of using "is" instead of "==":
# Advantage
# memory efficient.
# no duplicate object created.
# Disadvantage
# changes through one variable affect the other because a is b is True; both variables reference the same object.
# can create difficult-to-find bugs.


# Membership operator :
# Membership operators are used to check whether a value exists inside a sequence such as a string, list, tuple, set, or dictionary.
# 1 : in     : returns True if the value exists.
# 2 : not in : returns True if the value does not exists.

# in: 
# fruits = ["apple", "banana", "mango"]
# print("banana" in fruits)
# not in: 
# fruits = ["apple", "banana", "mango"]
# print("orange" not in fruits)

# in string:
# name = "Python"
# print("Py" in name)
# return True because "Py" exist in named variable.
# tuple:
# numbers = (1, 2, 3, 4)
# print(3 in numbers)
# return True because "3" exist in  above tuple.
# set : 
# numbers = {1, 2, 3, 4}
# print(3 in numbers)
# dictionary:
# student = {
#     "name": "Ali",
#     "age": 20
# }
# print("name" in student)
# For dictionaries, membership checks keys, not values.

# Design Tradeoffs & Consequences
# list vs set:
# 1: list:
# students = ["Ali", "Ahmed", "Sara"]
# print("Sara" in students)
# Python may need to check elements one by one.
# consequensis:
# Slower for large datasets.
# Time Complexity: O(n).
# set : 
# students = {"Ali", "Ahmed", "Sara"}
# print("Sara" in students)
# consequence
# much faster lookups.
# time Complexity: O(1) average case.
# note : set provides the fastest membership checks because it uses hashing.



# Bitwise Operator:             Name                             Example 
# Bitwise AND                    &                                a &  b
# Bitwise OR                     `                                 a|b
# Bitwise XOR                    ^                                 a^b
# Bitwise NOT                    ~                                 ~a
# Left shift                     <<                                a<<2
# Right shift                    >>                                a>>3


# consequences : 
# faster than many arithmetic operations at hardware level.
# used in low-level programming.
# common in operating systems, networking, embedded systems, and optimization problems.
# frequently used in coding interviews to test logical thinking.

# disadvantage
# less readable.
# modern Python interpreters optimize arithmetic well, so performance gains are usually negligible.



# print multiple values : 
# name = "zawar"
# age = 22
# print(name,age)

# using separator:
# print("python","SQL","Power BI", sep=" | ")

# end Parameter : 
# print("Hello", end=" ")
# print("World")

# taking user input : 

name = input("what is your name?")
age  = int(input("how old are u?"))
print("name               :    "+name)
print(f"age                :    {age}")
