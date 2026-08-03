# function: A function is a named sequence of instructions stored in memory that performs one specific task whenever it is called.

# Anatomy of a Function
# def greet(name):
#    return f"Hello {name}"

# lets disect it.
# def : key word telling python that i am creating a function.
# gree: function name.
# name:parameter placeholder.
# : syntax of function and starts of functioin.
# now calling it .
# greet("ali")
# here we pass ali to name(which is parameter.

# parameter vs argument.
# def add(x, y):
# here x and y are parameters.
# arjument:
# add(5,10) : 5 and 10 are are arguments and are passed to parameter placeholder.
# parameter: variable.
# Argument: actual value.


# internal working of function calling.
# def square(x):
#     return x*x
# print(square(5))
# here python creates memory framework as :x =5.
# calculates : 5*5 = 25.
# return : 25
# then it destroys the frame becaue the function is ended.
# lets say:
# def test():
#     a = 10
# print(a)
# here it fails to print anything because the print is outside of function local scop.

# x = 10
# def change():
#     x = 20
# change()
# print(x)
# this will print 10 ,  the function didnot change the value of x from 10 to 20 because x = 20, because the x= 20 is inside the function that cannot access the variable outside the function, and when we print x it point to x which is global not local inside funciton/


#The Life Cycle of a Function
# Every function goes through the same stages.
#         Define
#           ↓
#         Store
#           ↓
#         Call
#           ↓
#         Execute
#           ↓
#         Return
#           ↓
#         Finish

# Function Call
# When Python enters a function
# it temporarily leaves the current location.
# After the function finishes
# it comes back.

# functioin call example.

# Imagine reading a book.
# Page 10 says
# "See Appendix A."
# You stop reading page 10.
# Go to Appendix A.
# Read it.
# Come back to page 10.
# Continue reading.
# Functions behave exactly like this.

# stack: 
# A stack in Python is a linear data structure that follows the LIFO (Last In, First Out) principle. This means the last element added is the first one to be removed.
# Think of a stack like a pile of plates:
# You place a new plate on the top.
# You remove the top plate first.
# Common Stack Operations:
# 1) : Push: Add an item to the top.
# 2) : Pop: Remove and return the top item.
# 3) : Peek (Top): View the top item without removing it.
# 4) : isEmpty: Check if the stack is empty.

# stack = []
#  Push elements
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack)  # [10, 20, 30]
#  Peek : print top one.
# print(stack[-1])  # 30
#  Pop: remove top one and return it.
# item = stack.pop()
# print(item)   # 30
# print(stack)  # [10, 20]

# def A():
#     print("A")
# def B():
#     A()
# B()

# execution:
#       Main Program
#        ↓
#       B()
#        ↓
#       A()
#        ↓
#       Print A
#        ↓
#       Return to B
#        ↓
#       Return to Main

# this function or program start execution from function B which internally calls A(). A() prints A() then it return to B, then it return to main.

# call stack:
# Top
# A()
# B()
# Main
# Bottom

# when A fineshes:
# Top
# B()
# Main

# when B fineshes.
# Top
# Main
# This push-and-pop behavior is fundamental to how function calls work.


# some more about stack frames:
#  Each function call gets its own stack frame.

#  Think of a stack frame as a temporary workspace.
#  Example:
#  def add(a, b):
#      c = a + b
#      return c

#  When  function is called:
#  add(5, 3)
#  Python creates a new frame:
#  Function Frame: 
#  a = 5
#  b = 3
#  c = 8

#  When the function returns:
#  The entire frame disappears.
#  The local variables (a, b, c) no longer exist.


# scop is very important as :
# consider:
# def demo():
#     x = 10
# demo()
# print(x)

# This results in:  NameError  because x only existed inside demo()'s stack frame.
# Once the function finished, that frame was destroyed.
# This is why scope is so important.

# note: 
#  A function is stored when it is defined.
#  It only runs when it is called.
#  Python jumps into the function and returns afterward.
#  Every call creates a new stack frame.
#  Local variables live only inside their function's frame.
#  The call stack manages nested function calls using the LIFO principle.



# the function has two worlds .
# 1) : the caller.
# 2) : the funtion.

# Arguments (types:):
# Arguments

# Python supports several ways to pass information.
#           Arguments:
#              │
#              
#              ├── Positional
#              
#              ├── Keyword
#              
#              ├── Default
#              
#              ├── Variable-Length
#              
#              │      ├── *args
#              
#              │      └── **kwargs
#              
#              └── Keyword-Only / Positional-Only


# positional arguments.

# python mathes values by position.
#    def introduce(name, age):
#        print(name)
#        print(age)
#    
#    introduce("Zawar", 22)  
#    Position 1    
#    ↓    
#    name    
#    ↓    
#    "Zawar"   

#    Position 2  
#    ↓
#    age
#    ↓
#    22

# if we reverse the values 22 and zawar , it will print 22 in place of name and zawar inplace of name .
# this is incorrect logic.

#  Keyword Argument:
#  Instead of relying on position,
#  you explicitly tell Python where each value belongs.
#  def introduce(name, age):
#      print(name)
#      print(age)
#  introduce(age=22, name="Zawar")

# here python ignores position.

# default argument:
# some tims we assign value to parameter inside function and donnot ask argument for value.
# this  is default argument.
# but if we pass value to the same parameter , it will print the fresh value not the default value.
# default value will be printed if we dont assign value to it during call.

# Variable-Length Arguments (*args):

# if want to pass variable number of values to function . we use args.

# Example:
# def total(*numbers):
#    print(numbers)

# no matter how much numbers we  pass , those will be printed.

# why args are used:
# let say we want to add 2 numbers and we want to add them , we write functoin , we call that funtion , assign values , and their sum is printed.
# now we want to add 3 then 4 , then  5.
# to write code for them separately is time consuming.
# thats why we use args.
# we write one funtion with args .
# now we can add any number of values with the same funciton.



# Variable-Length Keyword Arguments (**kwargs):
# now if the information has labels and we want to print them.

# create_profile(
#     name="Ali",
#     age=25,
#     city="Peshawar"
# )


#  Instead of defining every possible parameter,
#  we use **kwargs.

# def profile(**details):
#     print(details)
# call:
# profile(
#     name="Ali",
#     age=25,
#     city="Peshawar"
# )

# Python packs all keyword arguments into a dictionary.


# combining Everything.
# def example(a, b, *args, c=10, **kwargs):
#    ...

# combining order :

#  Positional
#   ↓
#  *args
#   ↓
#  Default / Keyword
#   ↓
#  **kwargs



# calculate_total(*numbers) → Returns the sum of any number of values.

# def sum(*numbers):
#     print(numbers)
# sum(1,2,3,4,5)

# student_info(name, age, department="Data Science")


# def student_info(name,age,department):
#     print(name,"\n",age,"\n",department)

# student_info("zawar", 20,department="Data Science")

# create_profile(**details) → Prints every key-value pair neatly.

# def profile(**info):
#     print("\n-------------------")
#     for key,value in info.items():
#         print(f"{key}    :     {value}"
# )

# profile(
#     name      = "alauddin",
#     age       = 900,
#     deprtment = "cs&it",
#     hobby     = "creating troubles for students",
#     city      = "landi kotal",
#     uni       = "UET"
#find_max(*numbers) → Returns the largest number.

# def max_number(*numbers):
#     if not numbers:
#         return "provide numbers."
#     return max(numbers)

# print(max_number(1,2,3,4,5,6,34,7))
# print(max_number())



# generate_report(title, author="Unknown", **options) → Prints the title, author, and all additional options.

# def report(title,author,**additional):
    # print("====== Report ======")
    # print(f"{title} \n  {author}")
    # if additional:
        # print("====== Additional ======")
        # for key , value in additional.items():
            # print(f"{key}  :  {value}")
# 
# 
# report(
    # "Python Crash Course, 3rd Edition: A Hands-On, Project-Based Introduction to Programming",
    # author="Eric Matthes",
    # pages=552,
    # category="Computer Science / Programming",
    # published_year=2023,
    # language="English",
    # publisher="No Starch Press",
    # isbn="9781718502703",
    # edition="3rd",
    # format="Paperback"
# )





    

