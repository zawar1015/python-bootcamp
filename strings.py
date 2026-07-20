# string : is a text .

# accessing characters in python.
# python counts from 0.
# last index is -1

# word = "python"
# print(word[0])
# this will print p.

# last character:
# print(word[-1])
# this will print n.

# string slicing:
# text = "datascience"
# print(text[0:4])
# this will print "data".

# print every second character.
# print(text[::2])

# usefull string methods .
# name ="zawar"
# print(name.upper())

# replace :

# text = "I love python."
# print(text.replace("java","C++"))
# print(text)

# student = "ahmdda kaan"
# print(student.find("kaan"))
# Find:The find() method searches for a substring inside a string and returns the index of its first occurrence.

# consequence: 
# find() return -1 instead of raising an exception because This is a design decision with tradeoffs.

# benefits : 
# mpossible to ignore failure
# bugs become obvious immediatel

# count 
# text = "python python SQL"
# print(text.count("python"))


# strip spaces 
# name = "   Ali   "
# print(name.strip())

# string concatination :
# one =  "computer"
# two = "science"
# print(one + " " + two)

# F string :
# professional python uses F string.
# instead of :
# print("my name is ", name)

# professional python uses:
# print(f"My name is {name}")


# example 

# customer  = "ali"
# profit    = 3444
# print(f"{customer} generated Rs.{profit}")



