#                 File System
#                      │
#           ┌──────────┼──────────┐
#           ↓          ↓          ↓
#       pathlib       os       shutil
#           │          │          │
#        Paths       OS-level   High-level
#                   operations   file operations



# before pathlib , python programers commonly worked with paths using strings and os.path


# example:
# import os

# path = os.path.join("data", "sales", "2026", "sales.csv")



# path operations:
#  ├── parent
#  ├── name
#  ├── suffix
#  ├── exists()
#  ├── is_file()
#  ├── is_dir() etc

# Python introduced pathlib to provide an object-oriented and more readable way of working with filesystem paths.

# pathlib: concerened with Paths and filesystem navigation.
# object oriented approach.
# replace os.path(string)
# key class types:
# concrete path
# pure path.
# example:

# from pathlib import Path

# path = Path("data/sales.csv")




#  Task,                                    os.path Syntax                      pathlib Equivalent
#  Get current working directory           os.getcwd()                         Path.cwd()
#  Get home directory                      "os.path.expanduser(""~"")"         Path.home()
#  Join paths                              "os.path.join(a, b)"                "Path(a) / b or Path(a, b)"
#  Check file existence                    os.path.exists(path)                p.exists()
#  Check if file/directory                 os.path.isfile(path)                p.is_file() / p.is_dir()
#  Get file name                           os.path.basename(path)              p.name
#  Get stem (no extension)                 os.path.splitext(b)[0]              p.stem
#  Get file extension                       os.path.splitext(b)[1]              p.suffix
#  Get parent directory                    os.path.dirname(path)               p.parent
#  Get absolute path                       os.path.abspath(path                 p.resolve()


# key idea :
# open() works mainly with content of file:
# pathlib, os, and shutil help Python work with the file system.


#  pathlib.Path can be Use to :
# ) 1 : Create directories.
# ) 2 : Check whether files/folders exist.
# ) 3 : Identify files versus directories.
# ) 4 : Navigate directory structures.
# ) 5 : Create, rename, copy, and delete files.


# example:

# client_data/
# │
# ├── sales.csv
# ├── customers.csv
# ├── employees.xlsx
# ├── report.pdf
# ├── old_report.pdf
# ├── image1.png
# ├── image2.png
# └── backup/

# this is a directory and has to organized.

# one solution is manually .
# professional solution is :

# through code : 
# client_data/
# │
# ├── CSV/
# │   ├── sales.csv
# │   └── customers.csv
# │
# ├── Excel/
# │   └── employees.xlsx
# │
# ├── PDF/
# │   ├── report.pdf
# │   └── old_report.pdf
# │
# └── Images/
#     ├── image1.png
#     └── image2.png

# this is file automation.



# C:\
# └── Users
#     └── Zawar
#         └── Documents
#             └── Python
#                 └── data.csv

# The location of data.csv is its path.



# absolute vs relative path:
# absolute: An absolute path describes the complete location.
# example: 
# C:\Users\Zawar\Documents\data.csv
# path = r"C:\Users\Zawar\Documents\data.csv"
# The r means raw string.
# This is useful because Windows paths contain backslashes.

# Relative path
# A relative path is based on the current working directory.



# pathlib: 
# python has several ways to work with paths:
# historically programers commonly used:
# os.path but modern python provide pathlib


# example:

# from pathlib import Path
# path = Path("data/student.csv")
# print(path)
# output: data\student.csv(is simply a string)
# while Path("data/sales.csv") is a Path object designed specifically for filesystem operations.


# creating a path:
# from pathlib import Path
# file_path = Path("data") / "sales.csv"
# print(file_path)

# notice: Path("data") / "sales.csv"
# Python handles the appropriate path separator for the operating system.
# this is advantage of pathlib

# path properties:

# from pathlib import Path
# path = Path("data/sales.csv")
# print(path.name)
# print(path.suffix)
# print(path.stem)
# print(path.parent)

# checking wether something exists:

# from pathlib import Path

# path = Path("data/sales.csv")

# if path.exists():
#     print("File exists")
# else:
#     print("File does not exist")


# file vs directory:

# from pathlib import Path

# raasta = Path("data/sales.csv")

# print(raasta.is_file())
# print(raasta.is_dir())


# from pathlib import Path

# path = Path("data")

# if path.is_dir():
#     print("This is a directory")


# file = Path("data/sales.csv")

# if file.is_file():
#     print("This is a file")

# from pathlib import Path

# folder = Path("reports")
# folder.mkdir(exist_ok=True)

# if folder doesn't exist → create it
# if folder already exists → don't complain
# extremely useful in automation.

# from pathlib import Path

# path = Path("project/data/processed/csv")
# path.mkdir(parents=True,exist_ok=True)
# parent = True(create missing parent directories)

# listing files in directory:
# from pathlib import Path
# folder = Path("07_File_Handling\data")
# for item in folder.iterdir():
#     print(item)


# files only:
# from pathlib import Path

# folder = Path("07_File_Handling\data")
# for item in folder.iterdir():
#     if item.is_file():
#         print(item)
# directories wouldnot be included here.

# directories:

# from pathlib import Path

# folder = Path('07_File_Handling')

# for item in folder.iterdir():
#     if item.is_dir():
#         print(item)
# print directores only

# finding specific file types:
# glob(): most usefull method.


# from pathlib import Path

# folder = Path('07_File_Handling\data')

# for item in folder.glob('*.csv'):
#     print(item)
#     print(type(item))
# output: 
# 07_File_Handling\data\student.csv
# <class 'pathlib.WindowsPath'>

# example: 

# from pathlib import Path

# folder = Path("07_File_Handling\data")
# total_files= 0

# for item in folder.glob('*.txt'):
#     print(item)
#     total_files+=1

# print((total_files)) 
# 
#


# recursive search: 
# folder.glob("*.csv"):search for csv type files in immediate directory
# folder.rglog("*.csv"):search inside nested directories as well.



# reading file using Path:
# with open("07_File_Handling\csv_json.py") as file:
#     content = file.read()
#     # print(content)
#     print(type(content))

# # Path can also provide convenient method:
# from pathlib import Path

# path = Path("07_File_Handling\csv_json.py")
# content = path.read_text()
# # print(content)
# print(type(content))

# renaming file:

# from pathlib import Path

# old_name= Path(r"07_File_Handling\pathlib_os_&_.py")
# new_name= Path(r"07_File_Handling\pathlib_os_&_234.py")
# old_name.rename(new_name)




# shutil:shell utilities.

# copying a file:


# import shutil

# shutil.copy(r"07_File_Handling\data\string.txt", r"07_File_Handling\data\sales.txt")




# copy with path:
# from pathlib import Path
# import shutil

# source = Path(r"07_File_Handling\data\sales_report.txt")
# destination = Path(r"07_File_Handling\data\sales.txt")

# shutil.copy(source,destination)


# moving files with shutil (same as copy)
# shutil.move

# copy a directory:

# import shutil

# shutil.copytree("07_File_Handling\data","C:\Users\zawar\OneDrive\Desktop")




# deleting file:

# from pathlib import Path

# file = Path(r"C:\Users\zawar\OneDrive\Desktop\except.txt.txt")

# if file.exists():
#     file.unlink()


# import shutil

# shutil.rmtree(r"D:\delete")

# import os
# print("directory : ",os.getcwd())
# output: directory :  D:\data_science\python-bootcamp

# change working directory:

# import os

# os.chdir(r"07_File_Handling\data")



# os.listdir():

# import os 

# files = os.listdir("07_File_Handling\data")
# for item in files:
#     print(item)


# why using os when we have pathlib:
# bz we may encounter:
# old code
# tutorials
# Stack Overflow solutions
# libraries
# enterprise systems


# comparision:


# Task                     :   `pathlib`  `os`          `shutil` 
# ---------------------    :   ---------  ----          -------- 
# Represent paths          :   ✅          ✅             —        
# Check existence          :   ✅          ✅             —        
# File/directory checks    :   ✅          ✅             —        
# Create directory         :   ✅          ✅             —        
# List directory           :   ✅          ✅             —        
# Copy file                :   —            —             ✅        
# Move file                :   ✅           —            ✅        
# Copy directory tree      :   —            —            ✅        
# Delete file              :   ✅          ✅             —        
# Delete directory tree    :   —            —             ✅        



