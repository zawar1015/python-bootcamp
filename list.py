# python collections:
# A):list : 
#  1: stores multiple values in one  variable.
#  2: lists are mutable.
#  3: lists are ordered.
#  4: allow duplicates.
#  5: Dynamic size.
#  6: flexable.
#  7: 



# friends = ["ali","ahmads","lakpiece","kaakar","taashfain"]
# print(friends)


# marks = [90,80,70]
# strings= ["ali","ahmads","lakpiece","kaakar","taashfain"]
# mixed = ["ali","ahmads","lakpiece","kaakar",67,"taashfain",90,80,70]

# accessing elements in list :
# python starts indexing from 0 and last index is -1.
# print("   ------list------   ")
# print(marks)
# print(strings)
# print(mixed)


# first element:
# print(marks[0])
# print(strings[0])
# print(mixed[0])

# last element:
# print(marks[-1])
# print(strings[-1])
# print(mixed[-1])


# List Slicing
# syntax :
# list[start:stop:step]
# start : starting index (inclusive)
# stop : ending index (excluded)
# step : jump size.

# calculate length of slice :
# stop - start .
# marks = [90,80,70,60,50,40]
# print(marks[1:4])

# first N elements :
# marks = [90,80,70,60,50,40]
# print(marks[:4])
# last N elements :
# print(marks[2:])
# will print from 70 to 40 because the slicing start from 2 whcih is index of 70 and after collon there is nothing which means will pirnt all the remaing.

# copy entire list : 
# copy_list = marks[:]
# print(copy_list)

# print every second element:
# print(marks[::2])

# reverse a list :
# print(marks[::-1])
# print all elements of a list in order of last to first.

# negative indexing:
# print(marks[-3:])
# this will print 60,50,40.

# slicing create a new list .
# a= [1,2,3]
# b=a[:]
# print(a is b)
# this will print false becase a and b are different list and point to different addressess.


# advantages  :
# 1: safe.
# 2: origional list remain unchanged if we create new list using slicing.
# disadvantages : 
# 1: uses extra space.


# slicing vs reference assignment:
# reference:
# a= [1,2,3]
# b=a  # both variables points to same 
# b.append(4)
# print(a)
# slicing copy:
# a= [1,2,3]
# b=a[:]
# b.append(4)
# print(a)
# difference between b=a and b=a[:].
# b=a create reference , any change in b will be same for  a. but incase of b=a[:] anychange in b will not effect a.
# b=a[:] create new list.


# shallow copy :
# a= [[1,2],[3,4]]
# b=a[:]
# b[0].append(99)
# print(a)
# slicing perform a shallow copy.
# only the outer list is copied.
# nested objects are still shared. 

# consequence:
# fast copy.
# nested data can still effect the origional.


# changing items:
# strings= ["ali","ahmads","lakpiece","kaakar","taashfain"]
# strings[0] = "madoo"
# print(strings)

# adding items :
# add items to the list at end .
# strings.append("yasir comrade")
# print(strings)

# insert into list:
# add anything to list at specific index:
# strings.insert(1,"saba  roja da ")
# print(strings)

# extend list 1 to list 2:
# list_1 = [1,2]
# list_2 = [3,4]
# list_1.extend(list_2)
# print(list_1)


# removing items.
# 1) remove:
strings= ["ali","ahmads","lakpiece","kaakar","taashfain"]
# strings.remove("ali")
# print(strings)
# remove itme by its name.
# 2) pop:
# strings.pop(2)
# print(strings)
# pop remove  item by its index.
# del strings[0]
# print(strings)
# pop and del have a little differnce , pop return the removed item del does not return it,
# del can delete a slice or complete list vicevesa pop can remove a sigle index.
# pop is used when value is needed later and del is used when we donot need that data later.



# useful list functions:
# print(len(strings))
marks = [65,45,34,5,43,90]
# marks.sort()
# print(marks)
# marks.reverse()
# print(marks)

# count 
# print(marks.count(90))
# show the count or repetitin of specific data in a list.

# max and min:
# print the highest and lowest integer or value in given list.
# print(max(marks))
# print(min(marks))

# sum of all list:
# print(sum(marks))

# example :
# sales = [12000,15000,18000,22000]
# print(sum(sales))
# print(max(sales))
# print(min(sales))








