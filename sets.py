# sets : stores unique values. unordered collection.


# numbers = {1,2,3,3,4,4,5}
# print(numbers)

# doesnot allow duplicate value , they disappear silently.

# unordered nature:
# numbers = {1,2,3,4}
# print(numbers)
# u may see output as {3,2,4,1}

#Consequence:
# u cannot target element by index.
# print(numbers[0]) will raise TypeError.

# note:
# 1) : lists are optimize for position.
# 2) : sets are optimize for membership.


# membership testing:
# print(3 in numbers) 
# time complexity for finding membership in list and set  using in keyword.
# eg_list = [2,3,4,89]
# print(3 in eg_list)
# time complexity is O(n) . scan every element.
# set :
# print(3 in numbers)
# time complexity is o(1). average case.

# note : frequent membership testing , sets are used.


# operations:
# add():
# numbers.add(10)
# print(numbers)

# adding duplicates.
# numbers.add(10)
# print(numbers) # no error. no duplicates allowed.
# update():
# numbers = {1,2,3}
# numbers.update([4,5,6])
# print(numbers)


# difference between add() and update():
# add()    : add one element at a time.
# update() : add multiple elements at a time.

# lists are not hashable so they cannot be added to sets .
# numbers.add([7,8])
# print(numbers)  TypeError.

# remove():
# numbers.remove(4)
# print(numbers)

# reomoving missing elements.
# numbers.remove(29) raise key error.

# discard():
# numbers.discard(10)
# print(numbers)
# missing values such as above 10 will go unnoticed.

# romove
# numbers.remove(10)
# print(numbers)
# raise key error.

# pop()
# numbers={1,2,3,4,5,6}
# numbers.pop()
# print(numbers)
# remove orbitrary or first element.

# clear()
# numbers.clear()   # remove all elements of set but set itself remain.
# print(numbers)
# output : set()

# del.
# del numbers
# print(numbers)
# delete entire variable.
# output: not defined.

# set operations.
# union: combine all unique elements.
# A = {1,2,3}
# B = {4,5}
#  print(A | B)
# print(A.union(B)) # uniion alternative.

# intersection: common elements.
# print(A & B)

# difference : elements in first set but not in second.
# print(A-B)

# symentic difference: elements in exactly one set. means those which are not common.
# print(A^B)]

# subset.
# print(A.issubset(B))
# output : True.

# superset:
# print(B.issuperset(A))
# output: True.

# disjoint: no common elements.
# print(A.isdisjoint(B))

# copy()
# a = {1,2,3}
# b= a
# b.add(4)
# print(a)
# both changes which is a problem.


# frozen set.
# normal set is mutable , it can be change , it means it cannot be use as dictionaru key,
# to use set as dictionary key we use frozen set as :
# numbers = {1,2,3}
# fs = frozenset([1,2,3])  immutable.
# now fs can be use as key of dic.
# data = {
#     fs: "value"
# }


# time complexity of different operations in sets.
# Operation     :	Complexity
#add()	        :     O(1)
#remove()	    :     O(1)
#discard()	    :     O(1)
#membership(in) :  	  O(1)
#union	        :     O(len(A)+len(B))
#intersection	:     O(min(A,B))
#copy	        :     O(n)


# loop with collections.
# list:
# students = ["Ali","Sara","Ahmed"]
# for student in students:
#     print(student)

# dic:
# student = {
#     "name":"Ali",
#     "age":22
# }
# for key, value in student.items():
#     print(key, value)



