# loops : repeatition  of code execution automatically.
# Defination: loop is a programming structure that executes the same block of code repeatedly until a condition becomes False or until every item in a collection has been processed.
# Without a loop:
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")

# With a loop:
# for i in range(5):
#   print("Hello")

# range()
# range() it doesn't store all values. 
# It generates them on demand.

# most commenly used with for.
# specifies the range or length or extent of the loop.
# different forms of range()
# 1): range(stop): we assign only stop value , starting number is 0 by default.
# 2): range(start, stop): we assign start and stop both values.
# 3): range(start, stop, step): we assign start, stop and incrimental steps also.
# 4): negative steps(start, stop ,-steps)
# example : 
# for i in range(2, 11, 2):
#     print(i)

# Output: 
# 2
# 4
# 6
# 8
# 10

# we use loops  for different purposes , some are given below.
# Data cleaning
# Feature engineering
# Automation
# API calls
# File processing
# Model evaluation(file reading)
# ETL pipelines
# Simulations


# loops avoids repetition .
# readable.
# can become slow on large data set.

# types of loops:
# 1):for: for loop is used when you already know what you want to iterate over.
# 2):while

# for loop:
# syntax:
# for variable in iterable:
#     statements

# internal design of for loop:
# when python sees:
# for x in data:
# what it does is:
# iterator = iter(data)
# while True:
#     x = next(iterator)
# until stopiteration occures.

# iterable objects: those objects which can offer values one by one.
# some are:
# 1) : list
# 2) : tuple
# 3) : string
# 4) : dict
# 5) : set
# 6) : range
# 7) : File
# 8) : NumPy Array
# 9) : Pandas DataFrame

# looping through iterables:
# 1) : string:

# name = "Python"
# for letter in name:
#     print(letter)
# output:
# P
# y
# t
# h
# o
# n

# 2) : list:
# fruits = ["Apple","Banana","Mango"]
# for fruit in fruits:
#     print(fruit)
# output:
# Apple
# Banana
# Mango

# 3) : Tuple:
# numbers = (10,20,30)
# for i in numbers:
#     print(i)
# output:
# 10
# 20
# 30

# 4) : Set:
# colors = {"Red","Blue","Green"}
# for color in colors:
#     print(color)
# output:
# Green
# Blue
# Red

# note : as u can see the order of set and output is different.
# so order is not guaranteed.

# 5) : Dictionary: Dictionary iteration returns: keys and not values
# student = {
#     "Name":"Ali",
#     "Marks":90
# }
# for key in student:
#     print(key)

# output:
# Name
# Marks

# same way values can also be printed.

# printing both keys and values:
# for key,value in student.items():
#     print(key,value)

# enumerate(): Used when you need both the index and the value.
# fruits = ["Apple","Banana","Orange"]
# for index, fruit in enumerate(fruits):
#     print(index, fruit)

# output:
# 0 Apple
# 1 Banana 
# 2 Orange

# zip(): Loop through multiple collections together.
# names = ["Ali","Sara","John"]
# marks = [90,95,88]
# for name,mark in zip(names,marks):
#     print(name,mark)

# output:
# Ali 90
# Sara 95
# John 88








