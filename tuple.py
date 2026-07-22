# tuple is immutabel list.
# () used as a symbol instead of [] for list.
# when we donot want to change data accidentially , we use tuples.

# coordinates = (25.3,18.9)
# coordinates[0]= 80 # raise an error.
# print(coordinates)

# x = (5)
# print(type(x)) # here its data type is int because a tuple with sigle value is int basically.
# y = (5,)
# print(type(y))# now if we add "," then its type is tuple.

# accessing tuple items :
# same accessing as list.

# tuple slicing:
# same as list.

# tuple immutability advantages:
# data safety.
# easier debugging as data is constant.
# example :
# if there is a funtion which reciews tuple as "config = ("localhost", 5432)" , nobody can accidentially modify it

# hashable :
# point = (10,20)
# my_dict = {
#     point: "Location"
# }
# it works.

# what it we use list.
# point = [10,20]
# my_dict = {
#     point: "Location"
# }
# it doesnot work.

# consequence :
# immutable objects can safely be used as :
# for dictionary key.
# as set element.

# note: 1) : list is mutable.
#       2) : tuple is immutable.
#       3) : key of dictionary is immutable.
#       4) : so tuple can be used as dictionary key.

# tuple immutability is shalllow.
# It protects the references, not necessarily the nested objects.

# time complixity :
# index accessing : O(1)
# membership check: O(n)
# slicing         : O(k) where k is number os copied elements.



# tuples do contain some mutable objects.
# tuple itself is immutable , but if there are some lists inside the tuple , those lists can be change.

