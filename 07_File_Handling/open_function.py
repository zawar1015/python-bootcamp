# opening a file : 
# Opening a file refers to getting the file ready either for reading or for writing.
# This can be done using the open() function.
# This function returns a file object and takes two arguments.
# one that accepts the file name.
# another that accepts mode of file.


# Syntax of open() Function:
# File_object = open("File_Name", "Access_Mode")

#  Parameters: 
#  File_Name: This is the name of the file you want to open.
#  Access_Mode: This specifies the mode in which the file will be opened.

# modes of file opening :
#  Mode   :     Purpose 
#  --     :     ------- 
#  r      :     Read    
#  w      :     Write   
#  a      :     Append  
#  x      :     Create  
  


# default mode : 
# if mode is not provided as:
# open("students.txt")
#  then python assumes:
# open("students.txt","r")

# open()
#   ↓
# File Object
#   ↓
# read()
# write()
# seek()
# tell()
# close()


# encoding : 
# syntax: 
# open("students.txt", "r", encoding="utf-8")
# utf-8: character encoding system.
# it determines how characters are represented as bytes.

# need of encoding : 
# human understand characters
# computer understand bytes.
# encoding provides map for representing characters as bytes.

# conceptually : 
#  Human Characters
#         ↓
#     Encoding
#         ↓
#       Bytes
#         ↓
#       Storage

# when reading: 
#  Storage
#     ↓
#  Bytes
#     ↓
#  Decode using encoding
#     ↓
#  Python string


# utf-8 : most common encoding .

# handle errors : 

# with open(
#     "students.txt",
#     "r",
#     encoding="utf-8",
#     errors="ignore"
# ) as file:
#     data = file.read()

# possiible values include:
# strict: default behavior: raise an error if invalid data is encountered.
# ignore : skip problematic characters.
# replace: replace problematic characters with replacement character.


# new line:
# The newline parameter controls how newline characters are handled.
# This becomes particularly important when working with:

# CSV files
# files created on different operating systems
# Windows/Linux compatibility

# example: open("data.csv", "r", newline="", encoding="utf-8")

# using with

# with open("data/students.txt", "r", encoding="utf-8") as file:
#     data = file.read()

# The with statement ensures the file is properly closed when the block finishes, including when an exception occurs.



# file object methods: 
#  file.read()
#  file.readline()
#  file.readlines()
#  file.write()
#  file.writelines()
#  file.seek()
#  file.tell()
#  file.close()



# handling missing file with exception handling:

try:
    with open("missing.txt", "r", encoding="utf-8") as file:
        data = file.read()

except FileNotFoundError:
    print("The requested file was not found.")



# flow:
# Python Code
#      │
#      ▼
# open("students.txt")
#      │
#      ▼
# Operating System
#      │
#      ▼
# Locate File
#      │
#      ▼
# Establish File Handle
#      │
#      ▼
# Python File Object
#      │
#      ▼
# read/write operations


# file descriptor vs file object:
# At the operating-system level, an open file is associated with a file descriptor on systems such as Linux and Windows.

# Conceptually:
# Your Python code
#        ↓
# Python file object
#        ↓
# OS-level resource
#        ↓
# File on storage


# buffering: 
# The open() function also supports buffering.
# Example:
# open("data.txt", "r", buffering=1)
# Buffering : Python may temporarily hold data in memory before actually reading/writing it to the underlying resource.
# buffering can improve performence by reducing the number of low level operations.
# buffering is relevent when we work with : 

# very large files
# streaming
# high-performance applications
# logs
# network-like streams

# visulization of encoding + buffering + file object:
#              Your Python Code
#                     │
#                     ▼
#               File Object
#                     │
#           ┌─────────┴─────────┐
#           ▼                   ▼
#       Encoding             Buffering
#           │                   │
#           └─────────┬─────────┘
#                     ▼
#               OS / Storage


# example: 
file = open(
    "07_File_Handling/data/students.txt",
    "r",
    encoding="utf-8"
)

print("Name:", file.name)
print("Mode:", file.mode)
print("Closed:", file.closed)

content = file.read()

print("\nContent:")
print(content)

file.close()

print("\nClosed:", file.closed)