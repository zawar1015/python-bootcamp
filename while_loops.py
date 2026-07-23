# while loops : runs as long as the condition is True.

# syntax: 
# while condition:
#     statements

# flow of while loop:
#       Condition
#         ↓
#       True
#         ↓
#       Execute Code
#         ↓
#       Condition Again
#         ↓
#       False
#         ↓
#       Exit Loop


# example:
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

# output:
# 1
# 2
# 3
# 4
# 5


# infinire loop:
# If the condition never becomes False.
# while True:
#     print("Running")
# this never stops.

# loop control statements: stops the loop immediately.

# break:
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# output:
# 0
# 1
# 2
# 3
# 4

# continue: skips the current iteration
# for i in range(6):
#     if i==3:
#         continue
#     print(i)
# output:
# 0
# 1
# 2
# 4
# 5

# Avoids deeply nested conditions.
# Too many continues can make logic harder to follow.


# pass:
# A placeholder used when you'll add code later.
# Useful while writing incomplete code.
# example 1) :
# for x in range(5):
#     pass
# example 2) :
# if True:
#     pass


# while vs pass :
#            while	                     :            for
# Runs until a condition becomes False	 :   Runs over an iterable(known)
# Best when iterations are unknown       :	 Best when iterations are known
# Can become infinite                    : 	 Usually finite
# Used for menus, login systems, games   :	 Used for datasets, files, lists


