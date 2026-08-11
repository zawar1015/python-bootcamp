# A file pointer (also called the stream position or cursor) is a byte-offset index maintained by the operating system and Python to track where the next read or write operation will take place inside an open file.

# key methods to control pointer in python.
# f.tell():
# Returns an integer representing the current byte offset of the pointer from the beginning of the file (0-indexed).

# f.seek(offset, whence=0):
# Moves the file pointer to a new location.
# offset: How many bytes to move.
# whence (optional): The reference point:
# 0 (default): Absolute position from the beginning of the file.
# 1: Relative position from the current pointer location.
# 2: Relative position from the end of the file.


# example : 
# Create a sample file
# with open("demo.txt", "w", encoding="utf-8") as f:
#     f.write("0123456789")  # Writes 10 bytes (0-9)

# # Open in read mode
# with open("demo.txt", "r", encoding="utf-8") as f:
#     print("Initial position:", f.tell())  # Output: 0
    
#     # Read first 4 bytes
#     data = f.read(4)
#     print("Read:", data)                  # Output: "0123"
#     print("Position after read:", f.tell()) # Output: 4
    
#     # Move pointer back to position 2
#     f.seek(2)
#     print("Position after seek(2):", f.tell()) # Output: 2
    
#     # Read 3 bytes from position 2
#     print("Read again:", f.read(3))      # Output: "234"


# File Pointer:
# Think of it like a cursor in a text editor.
# Suppose the file contains:
# conceptually :
# P y t h o n
# ^
# 0

# when python reads some characters the cursor move farward.
# the position of cursor is called file poiter or file position.


# example :
# with open("data.txt", "r", encoding="utf-8") as file:
#     print(file.read(5))

# suppose:
# data.txt contain: python programing.
# read(5) reads: pytho.
# the pointer moves to : 
# P y t h o n   P r o g r a m m i n g
#           ^
#           position 5

# if we now execute print(file.read(6)):
# python doesnot start from begining , it continues from position 5.


# tell: find current position of file pointer.
# example:

# with open("07_File_Handling\data\sales_report.txt","r", encoding="utf-8") as file:
#     read = file.read(400)
#     print(read)
#     print(file.tell())


# seek(): move to somewhere else:

# syntax: file.seek(position).

# with open("07_File_Handling\data\sales_report.txt","r", encoding="utf-8") as file:
#     read = file.read(400)
#     print(read)
#     print(file.tell())
#     file.seek(0)
#     print(file.read(400))
# above will print same output because the pointer is seeked to 0 again.

# conceptually: 
# Start
#  ↓
# read 5 characters
#  ↓
# pointer = 5
#  ↓
# seek(0)
#  ↓
# pointer = 0
#  ↓
# read again from beginning


# read and pointer:
# example : 
# with open("07_File_Handling\data\sales_report.txt","r", encoding="utf-8") as file:

#     print(file.tell())

#     file.read(3)

#     print(file.tell())

#     file.read(4)

#     print(file.tell())


# seek:
# example :
# file.seek(offset,whence) where whence determines the reference point.

# whence commone values:
# 0 → beginning
# 1 → current position
# 2 → end

# conceptually : 
# whence = 0
# START ───────────────►

# whence = 1
# CURRENT POSITION ────►

# whence = 2
# END ◄─────────────────


# file pointer uses:
# processing files incrementally
# rereading data
# navigating files
# handling binary files
# working with large files
# building custom file-processing systems
# reading specific sections of data


# closing a file :

# leaving file open unnecessarily can cause :
# resource leaks
# file locking issues
# excessive open-file usage
# incomplete writes
# unpredictable behavior in larger applications



# manual close(): not safe because the program may crash in between and it may not not reach to file.close().
# with statement: safe because it automatically clse the file.


# context manager:
# A context manager is an object that controls what happens when entering and leaving a block of code.

# __enter__() and __exit__():
# context manager use special methods:
# __enter__()
# __exit__()

# note: we cannot use the close file : it will raise valueError
