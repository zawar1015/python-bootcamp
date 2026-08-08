# file Handling : 
# File handling refers to the process of performing operations on a file, such as:
# 1) : creating file .
# 2) : opening .
# 3) : reading .
# 4) : writing .
# 5) : closing .

# through progrming interface.

# file handling manage data flow between a program and file stored on storage.
# ensure that the data is handled safely and efficiently.


# need of file handling : 
# 1) : Store data permanently, even after the program ends.
# 2) : Access external files like .txt, .csv, .json, etc.
# 3) : Process large files efficiently without using much memory.
# 4) : Automate tasks like reading configs or saving outputs.


# use of file handling .

# python programs store data temporarily.
# such as : 
# students = ["Ali", "Ahmed", "Sara"]

# while program is running : 
#         Program
#           ↓
#       students list
#           ↓
#          RAM

# when program terminates:
#      Program closes
#            ↓
#      RAM cleared
#            ↓
#      students disappear


# disappearing data is problem.

# Suppose you build a student registration system and add:
#  Ali
#  Ahmed
#  Sara

# if we store this data in variable and we close program,next time we start program there will be no data.
# file handling is persistent storage.

#    Python Program
#          ↓
#         File
#          ↓
#       Storage
#          ↓
#    Data remains after program closes


# RAM  vs Storage.

# RAM : temporary working memory.
# example :
# data = [1, 2, 3, 4, 5]
# program keeps this data in memory while running.

# storage : persistent storage.
# example : 
#  students.csv
#  sales.xlsx
#  customers.json
#  model.pkl
#  logs.txt

# these files remain while program terminates.


#  RAM
#  ↓
#  Working area
#  
#  Storage
#  ↓
#  Permanent data

# file : A file is a named collection of data stored on a storage device.
# example : 
# students.txt
# sales.csv
# employees.json
# report.pdf
# photo.jpg
# model.pkl

#file normally has :
# file name , followed by extension.
# extension tells which type of file it is.

# some examples are:

#   Extension	            Typical Use
# 1) : .txt	               Plain text
# 2) : .csv	               Tabular data
# 3) : .json	           Structured data
# 4) : .xlsx	           Excel workbook
# 5) : .pdf	               Documents
# 6) : .jpg	               Image
# 7) : .png	               Image
# 8) : .py	               Python source
# 9) : .sql	               SQL code
# 10) : .log	           Log files
# 11) : .pkl	           Serialized Python object

# note: The extension helps identify a file format, but the extension alone doesn't guarantee that the contents actually follow that format.

# Text Files vs Binary Files:

# Text Files:
# Contain data that can be represented as characters.
# examples: 
#  .txt
#  .csv
#  .json
#  .py
#  .sql
#  .log
#  .md

# data example: 
#  Name,Age,Department
#  Ali,22,Data Science
#  Sara,23,AI
# Python can read this as text.

# binary files:
# Binary files contain data represented as bytes.
# example:
# .jpg
# .png
# .pdf
# .mp3
# .mp4
# .exe
# .pkl 
# They aren't intended to be interpreted simply as normal human-readable text.

# conceptually : 

#  Text:
#  A → character
#  B → character
#  C → character
  
#  Binary:
#  10101010
#  00101101
#  11001010

# file lifecycle : 
# 1) :  Locate file
#         ↓
# 2) :  Open file
#         ↓
# 3) :  Read / Write
#         ↓
# 4) :  Process data
#         ↓
# 5) :  Close file

# example : 
# file = open("students.txt", "r")
# data = file.read()
# file.close()
# output: FileNotFoundError: because there is no such file yet in the directory.


# opening a file :
# python uses : 
# open() 

# basic syntax: 
# open(filename,mode)
# Open the file and return a file object configured for reading.


# fiel object:
#  file = open("students.txt", "r")
#  file isn't the actual contents.
#  It is a file object that provides an interface for interacting with the file.
 
#  students.txt
#        ↑
#        │
#  File Object
#        ↑
#        │
#  Python Program

# methods :
# file.read()
# file.readline()
# file.write()
# file.close()

# file modes : 
# The second argument to open() determines what you want to do.
# Mode	Meaning
# r  	Read
# w	    Write
# a  	Append
# x 	Create
# rb	Read binary
# wb	Write binary


# Absolute vs Relative Paths:
# Suppose your project looks like:

# python-bootcamp/
# │
# ├── 06_File_Handling/
# │   ├── reading_files.py
# │   └── students.txt

# From reading_files.py, you could use:
# open("students.txt")
# if the current working directory makes that path valid.
# This is a relative path.

# Absolute Path
# An absolute path describes the complete location
# C:\Users\Zawar\Documents\python-bootcamp\06_File_Handling\students.txt

# Absolute paths are explicit but often less portable.

# creating a file 

# file= open("allauddin.txt", "w")
#If the file doesn't exist, w can create it.

# reading a file:

# file  = open("allauddin.txt","r")
# data = file.read()
# print(data)
# file.close()

# flow:
#  Open
#   ↓
#  Read
#   ↓
#  Print
#   ↓
#  Close


# closing a file :
# opening a file creates a resource that your operating system manages
#  If your program continuously opens files without properly releasing them, you can run into:  
#  resource exhaustion
#  file locking problems
#  data corruption risks
#  unexpected behavior

# practice exercise:


#06_File_Handling/
#│
#├── 01_introduction.py
#│
#└── data/
#    └── students.txt

file = open("07_File_Handling/data/students.txt", "r")

print("File opened successfully.")

file.close()

# inspect the file object:
file = open("07_File_Handling/data/students.txt","r")
print(type(file))
file.close()

# inspect properties:
print("\n ---- Properties ----")
file = open("07_File_Handling/data/students.txt","r")
print(file.name)
print(file.mode)
print(file.closed)

file.close()
print(file.closed)

# mental model:
# open()
#   ↓
# File Object
#   ↓
# read/write
#   ↓
# close()

#  file.name: Returns the name of the file that was opened (in this case, "geek.txt").
#  file.mode: Tells us the mode in which the file was opened. Here, it’s 'r' which means read mode.
#  file.closed: Returns a boolean value- False when file is currently open otherwise True.



import os

file_path = input("Enter file path: ")

print("\n========== FILE INFORMATION ==========\n")

print("File Name:", os.path.basename(file_path))
print("File Path:", file_path)
print("File Exists:", os.path.exists(file_path))

if "." in os.path.basename(file_path):
    print("File Type:", file_path.split(".")[-1])
else:
    print("File Type: Unknown")

print("\n=======================================")


# file inspector concept is useful in : 
#  Dataset validation
#  File automation
#  Backup systems
#  ETL pipelines
#  CSV processing
#  Report generation
#  Document processing
#  Data migration
#  Batch processing