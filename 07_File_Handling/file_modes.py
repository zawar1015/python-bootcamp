# file mode : refers to the setting or access state assigned to a file when it is opened or managed by an operating system.

# File Access Modes:the file mode determines what actions (read, write, append) are permitted and how the data is handled.

#   Mode            Symbol        Behavior
#   Read            'r'         Opens the file for reading only (default). Fails if the file does not exist.
#   Write           'w'         Opens the file for writing. Overwrites existing content or creates a new file.
#   Append          'a'         Opens the file for writing without overwriting; appends new data to the end.
#   Binary          'b'         "Treats file contents as raw bytes rather than plain text (e.g., 'rb', 'wb')."
#   Exclusive       'x'         Creates a new file and opens it for writing; fails if the file already exists.


# file permission: In Unix-like systems, file mode refers to a bitmask that dictates access permissions (read, write, execute) across three user scopes: the file Owner, the assigned Group, and Others.

# syntax: 
#open("students.txt","r") the second argument is mode , it tells python what operation u intend to perform.

# main modes are:
# r -> read
# w -> write
# a -> append
# x -> create

# there are also combinations: 
# r+
# w+
# a+

# binary versions:
#  rb
#  wb
#  ab
#  rb+
#  wb+
#  ab+

# four fundamental modes: 

# Mode     Read     Write      Creates if missing  Deletes existing content 
# ----     ---     ----        -----------------   -----------------------: 
# r        ✅       ❌              ❌                   ❌ 
# w        ❌       ✅              ✅                ⚠️ Yes 
# a        ❌       ✅              ✅                   ❌ 
# x        ❌       ✅              ✅                   ❌ 

# example: 
# with open("students.txt", "r", encoding="utf-8") as file:
#     content = file.read()
#     print(content)


# write mode "w":
#open("students.txt","w"):
# open file for writing , if there is no such file create it.
# if file already exists : the existing content is troncated.
# write mode can be dangerous .
# suppose u already contain data in file such as ali, ahmad, allauddin coas
# and u exesute : 
# with open("students.txt", "w", encoding="utf-8") as file:
#     file.write("Zawar")
# now there is only zawar in file the data which was already there is trancated.

# append:
# syntax: 
# open("students.txt", "a")
# Open the file for writing, but preserve existing content and add new data at the end.
# suppose:
# with open("students.txt", "a", encoding="utf-8") as file:
#     file.write("\n imran heehee")
# now this new data is added to file with the existing one at the end.
# this creates file if necessary.


# x -> exclusive creation.
# if file already exists : this gives error  (FileExistsError)


# difference between x and w is : 
# w : trancate|overwrite old data .
# x : if file exists : raise error.

# r+ -> read and write : 
# for this one file must exists.
# unlike w, r+ does not automatically erase file.


# r+ example : 
# with open("example.txt", "r+", encoding="utf-8") as file:
#     content = file.read()
#     print(content)

# W+ -> write and read : 
# trancate file .
# this is dangerous if u want to preserve existing data.


# a+ -> append and read: reading and appending.
# open("students.txt", "a+")

# creates the file if missing
# preserves existing data
# allows reading
# writes at the end


# binary mode : 
# b: to work with binary data.

# example:
# rb
# wb
# ab
# rb+
# wb+
# ab+

# rb -> read binary 
# used for files such as : 
#  images
#  PDFs
#  audio
#  video
#  serialized bianary data

# example :
# with open("photo.jpg", "rb") as file:
#     data = file.read()
# print(type(data))
# output: <class 'bytes'>

# note: 
# text mode -> str
# binary mode -> bytes


# wb -> write binary:
# this write bytes rather than text.

# example:
# with open("photo.jpg", "rb") as source:
#     data = source.read()
# with open("photo_copy.jpg", "wb") as destination:
#     destination.write(data)

# ap -> append binary:
# opens a binary file for appending.


# text vs binary 
# text return string
# binary returns bytes

# visualize:
#  Text mode
#      ↓
#  Characters
#      ↓
#  str


#  Binary mode
#      ↓
#  Raw bytes
#      ↓
#  bytes


# mode map:


#                       READ     WRITE    CREATE    TRUNCATE
#   ----------------------------------------------------------
#   r                    ✅        ❌        ❌          ❌
#   w                    ❌        ✅        ✅          ✅
#   a                    ❌        ✅        ✅          ❌
#   x                    ❌        ✅        ✅          ❌
#   ----------------------------------------------------------
#   r+                   ✅        ✅        ❌          ❌
#   w+                   ✅        ✅        ✅          ✅
#   a+                   ✅        ✅        ✅          ❌

# for bytes :
# rb
# wb
# ab
# rb+
# wb+
# ab+

# The underlying behavior remains conceptually the same, but the data is handled as bytes



# practice :



import os 
file_name = "07_File_Handling\data\students.txt"

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add student")
    print("2. View students")
    print("3. Append student")
    print("4. Create new record file")
    print("5. Exit")


    choice = input("\n Enter ur choice : ")


    if choice == "1":
        student_name = input("enter student`s  name : ")
        student_age = input("input age : ")
        department = input("enter department : ")

        with open(file_name,"r+") as file:
            file.write(f"{student_name} ,{student_age},{department}\n")
        print("student record saved.")


    elif choice == "2":
        try:
            with open(file_name,"r") as file:
                data = file.read()

                if data: 
                    print("\n ---- students record ----")
                    print(data)

                else:
                    print("file is empty.")

        except FileNotFoundError:
            print("record file not found.")

    elif choice == "3":
        student_name = input("enter name : ")
        student_id = input("enter age : ")
        department = input("enter department : ")


        with open(file_name, "a") as file: 
            file.write(f"{student_name},{student_age},{department}\n")
        print("students appended  da kamyaby sara kho alladdin bss.")


    elif choice == "4":
        try:  
            with open(file_name,"x") as file:
                print("new record file created.")

        except FileExistsError:
            print("file already exists.")

    elif choice == "5":
        print("exiting program ...")
        break


    else:
        print("invalid choice , Try again")



