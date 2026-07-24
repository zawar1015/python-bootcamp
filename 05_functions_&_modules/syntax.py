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