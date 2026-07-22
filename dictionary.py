# dictionary: an object which store multiple data in pairs of keys-value.

# student = {
#     "name": "Ali",
#     "age": 20,
#     "cgpa": 3.7
# }
# print(student)

# suppose we have list.
# student = ["Ali", 20, 3.7]
# indexing is not obvious.

# student["name"]
# meaning is clear from above dic.


# accessing values:
# student = {
#     "name": "Ali",
#     "age": 20
# }

# print(student["name"])
# in dictionary we access value by its key.

# accessing in list was fast was not descriptive.
# accessing in dictionary is more readable.

# adding items:
# same sytax is adding new key and updating an existing key.

# student = {}

# student["name"] = "Ali"
# student["age"] = 20
# print(student)
# student["reg_number"] ="24pwbcs1066"
# print(student)

# update:
# student["name"] = "gymnast alaaoodin "
# print(student)
# disadvantage of the syntax that adding and updating is same is that accidential overwrites are easy.

# note : dic keys are unique.


# adding multiple items with update()

# student = {
#     "name": "Ali"
# }

# student.update({
#     "age": 20,
#     "city": "Lahore"
# })
# print(student)
# student.update({
#     "uni" : "UET"
# })
# print(student)


# update() vs indevidual assignment.
# individual assignment:
# student["name"] = "zawar"
# print(student)
# easy and efficient for individual addition or update.

# update():
# convenient for multiple addition or multiple update.


# adding nested data.
# student["marks"] = [90, 80, 70]
# print(student)
# to add nested data to dic we pass list to key.

# consequence:
#  1) Dictionary values can be:
#  2) Strings
#  3) Numbers
#  4) Lists
#  5) Tuples
#  6) Dictionaries
#  7) Objects
#  8) Almost anything.


# set default:
# suppose:
# student = {
#     "name": "Ali"
# }
# student.setdefault("city","unknown")
# print(student)

# # now try to update name:
# student.setdefault("name","ahmad")
# print(student)
# did not change.

# normal assignment can be overwrite .
# setdefault is used when u want to preserve existing data.


# time complixity of adding  new key and updating existing key = O(1).

# note : python dictionaries use  hashtable.
#Python computes the hash of the key and jumps directly to the storage location.


# removing key value pair in dic: remove by its key.
# student = {
#     "name": "Ali",
#     "age": 20
# }
# del student["age"]
# print(student)

# advantage:
# simple and fast.
# clear intention: delete this key.

# disadvantage:
# if key does not exist.
# it will give KeyError.

# in list we were using pop whith the index , here we use pop with key.
# the rest is same , pop returns the removed value but not del.

# pop item(): removes the last inserted key-value pair.

# student = {
#     "name": "Ali",
#     "age": 20
# }
# print(student.popitem())
# popitem() is useful when we treat dictionary like stack.

# clear():  removes everything.
# clear(): is very fast and clean but data is lost.

# we can delete the entire dictionary dic as :
# student = {
#     "name": "Ali"
# }
# del student


# difference between clear and del:
# with clear() the dictionary is complety empty everything is deleted but the dictionary exits .
# with del : dic itself is deleted.

# time complecity:
# del              :  O(1)
# pop              :  O(1)
# membership check :  O(1)
# clear dictionary :  O(n)

# acenario:
# student = {
#     "name": "Ali"
# }
# print(student.pop("name"))
# print(student)

# first print is ALi , although its poped but its value is returned .
# for second it prints {}.


# usefull methods .

# get 
student = {
    "name": "Ali",
    "age": 20
}
# print(student.get("name"))
# missing key.
# print(student.get("city"))
# none : showing no error , not raising any exception.
# using []:
# print(student["city"]) key value error.

#get() consequunce:
# 1) safer access.
# 2) avoid crashes.
# disadvantages :
# missing keys can silently go unnoticed.



# keys :
# return all keys.
# print(student.keys()) 
# consequunce:
# advantage
# memory efficient.
# no copying.
# disadvantage
# beginners expect a list.



# values()
# return all values:
# print(student.values())

# checking if a value exists or not.
# print("Ali" in student.values()) # True , here in is used which is membership operator.

# items() : return key-value pairs.
# print(student.items())

# iteration.
# for key, value in student.items():
#     print(key, value)

# update()
# student.update({
#     "age": 21,
#     "city": "Lahore"
# })
# print(student)

# advantage:
# 1) : bulk update.
# disadvantages:
# 1) :can overwrite existing column.






