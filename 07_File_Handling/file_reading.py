# file reading: When you read a file, Python retrieves data from the file and makes it available to your program.
# means accessing and retrieving contents of a file.
# uses :
# processing logs.
# reading configuration files.
# handle datasets.


# conceptually: 
#  File on Disk
#       ↓
#  Operating System
#       ↓
#  Python File Object
#       ↓
#  Your Program
#       ↓
#  String / List / Bytes


# syntax : 
# with open("students.txt", "r", encoding="utf-8") as file:
#     data = file.read()
# data is now python str.


# Three main reading methods:
# file.read()
# file.readline()
# file.readlines()
# they are not interchangable.


#  Method	      Returns	          Reads
#  read()	      str	              Whole file / specified characters
#  readline()	  str	              One line
#  readlines()	  list[str]	          All lines

# forth one is : 
# for line in file: useful for large files:


# read(): read the entire file:
# example: 
#  with open("students.txt", "r", encoding="utf-8") as file:
#      data = file.read()  
#  print(data)

# what does read() return:
# with open("students.txt", "r", encoding="utf-8") as file:
#     data = file.read()

# print(type(data))
# <class 'str'>

# read(size): read can accept number.
# data = file.read(10)
# this will read upto 10 characters from current file position.

# read(size) matters:
# in large file let say 5 GB.
# if we read it as data = file.read(), will take alot memory and time.
# instead : if we:
# data = file.read(1024). read small portion of data and this idea is called chunked reading.

# usefull in : 
# ata engineering
# og processing
# TL
# arge datasets
# treaming systems

# file poiter: 
# When a file is opened, Python maintains a position indicating where the next read/write operation occurs.
# Python Data Science
# ^: the cursor is here at the moment.
# then we execute : file.read(6)
# the mointer moves:
#Python Data Science
#      ^ now next read will start from this position.




# tell():
# tell about curent position.
# example:
# with open("students.txt", "r", encoding="utf-8") as file:
#     print(file.tell())
#     file.read(5)
#     print(file.tell())

# reading twice:
# with open("students.txt", "r", encoding="utf-8") as file:
#     print(file.read())
#     print(file.read())
# it does not print the same data twice because by first read poiter moves to end and for second read there is nothing to read.


# visualize:
#  First read:
#  
#  [Ali
#   Ahmed
#   Sara]
#               ↑
#               EOF
#  
#  
#  Second read:
#  
#               ↑
#               EOF
#  
#  Nothing left to read.


# resetting the pointer:
# with open("students.txt", "r", encoding="utf-8") as file:

#     first = file.read()
#     print(first)

#     file.seek(0)

#     second = file.read()
#     print(second)

# now the file is read twice.
#



# read line : read single line.

# let say we have data : 
# Ali
# Ahmed
# Sara

# with open("students.txt", "r", encoding="utf-8") as file:
#     line = file.readline()
#     print(line)

# this will print only Ali

# for line in file : 
# powerful.

# visulize:
#  File
#   ↓
#  Read manageable amount
#   ↓
#  Process line
#   ↓
#  Next line
#   ↓
#  Process

# read() vs readlines() vs Iteration

#  Situation                         :   Best approach      
#  --------------------------------- :   ------------------ 
#  Small text file                   :   read()           
#  Need entire content as one string :   read()           
#  Need one specific next line       :   readline()       
#  Need all lines as a list          :   readlines()      
#  Large file                        :   for line in file 
#  Large file with chunk processing  :   read(size)       



# line.strip(): is a string method that removes all leading and trailing whitespace (spaces, tabs \t, and newlines \n) from a string. 
# It leaves the characters in the middle untouched.


# practice:

file_name = "07_File_Handling\data\students.txt"

total_students = 0
total_age = 0

department_count = {}

oldest_student = None
oldest_age = -1

youngest_student= None
youngest_age = 999

ai_students = []

try:
    with open(file_name,"r") as file:
        for line in file:
            line = line.strip()

            try:
                name,age, department = line.split(",")
                age = int(age)
                total_students+=1
                total_age+=age

                department_count[department]=(
                    department_count.get(department,0)+1
                )

                if age > oldest_age:
                    oldest_age = age
                    oldest_student= name

                if age < youngest_age:
                    youngest_age = age
                    youngest_student = name

                if department == "ai":
                    ai_students.append(name)

            except(ValueError,IndexError):
                print(f"invalid record skipped : {line}")


    print("\n ----------student data analyzer ---------")
    print("Total students : ", total_students)

    print("department counts : ")
    for department ,count in department_count.items():
        print(f"{department}:{count}")


    if total_students> 0:
        average_age = total_age/total_students
        print("\n Average age ", round(average_age,2))

        print("Oldest Student:", oldest_student, f"({oldest_age})")
        print("Youngest Student:", youngest_student, f"({youngest_age})")

    print("\n ai students")
    for student in ai_students:
        print(student)
        print("\n----------------------------")
except FileNotFoundError:
    print("file not found.")


                    
