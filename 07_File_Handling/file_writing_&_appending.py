# Mode    OS File Flag                Behavior        Pointer Position         What Happens to Existing Content?
# 'w'     (Write),O_TRUNC            (Truncate)      Start (0)            "Erased instantly upon opening, even before calling .write()."
# 'a'     (Append),O_APPEND          (Append)        End (EOF)             Preserved. Writes are forced to the end of the file by the OS.



# internal Workflow:

#High-Level Python (User Space):
# Encoding: Python strings are Unicode. Before writing text mode, Python uses its default encoding (UTF-8) to encode the text into bytes. 
# Stream Wrapper: Python’s open() returns an I/O stream object (from the built-in io module).

# CPython Memory Buffer (User Space)
# Python maintains its own User Space Buffer in RAM to avoid expensive System Calls (syscalls). 
# Small .write() calls simply dump bytes into this internal memory buffer until it reaches capacity (typically 4KB or 8KB).

#  Operating System Page Cache (Kernel Space)
#  Once Python’s buffer fills up (or you call .flush()), Python executes an OS system call (e.g., write() on Unix/Linux or WriteFile() on Windows).
#  The OS takes these bytes and moves them into its Page Cache (RAM managed by the OS Kernel). 
#  At this point, Python considers the write "done," but the data is still in RAM!

# Storage Device (Physical Disk)
# The OS asynchronously flushes dirty pages from the Page Cache onto the actual disk/SSD using background processes (like pdflush or flush threads).
# If the power goes out before the OS flushes the Page Cache, data can be lost—even if Python completed its execution!


# Writing means transferring data from your Python program into a file stored on your computer.

# Python Program
#       │
#       ▼
#    Data in memory
#       │
#       ▼
#    File Object
#       │
#       ▼
# File stored on disk


# writing to file is important because the data stored is persistent then.
# if we dontn save data to a file , it will not exists when the program ends

# memory vs storage:
# RAM
# │
# ├── temporary
# ├── fast
# └── program variables
 
# Disk
# │
# ├── persistent
# ├── slower
# └── files


# the "w" mode : 
# example : 

# with open("data.txt","w",encoding="utf-8") as file:
#     file.write("hhhhhhhhhh")


# important part of "w":
#it overwrote the existing data , forexample the already has data so when we write data to file using w , it will trancate the old data and will the new one we add.


# mental model : 
#   Existing File
#   ─────────────
#   Hello
#   Python
#   Data Science   
#           ↓ "w"  
#   Existing content deleted   
#           ↓   
#   Machine Learning   

# note : purpose of w is to create fresh writable file.


# conceptually:
# open(file, "w")
#        │
#        ├── File exists?
#        │      ↓
#        │   Clear contents
#        │
#        └── File doesn't exist?
#               ↓
#           Create file

# write() Only Accepts Strings for Text Files:


# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write(100)
# this produce TypeError:

# age = 22

# with open("data.txt", "w", encoding="utf-8") as file:
#     file.write("Age: " + str(age))


# Writing a List with writelines():

# students = [
#     "Ali\n",
#     "Ahmed\n",
#     "Sara\n"
# ]

# with open("students.txt", "w", encoding="utf-8") as file:
#     file.writelines(students)

# writelines(): doesnot add new line.

# write vs writelines:

#   write()          	            :     writelines()
#   Writes one string	            :     Writes multiple strings
#   Takes a string	                :     Takes an iterable of strings
#   Doesn't add newline	            :     Doesn't add newline
#   Good for individual content	    :     Good for multiple lines





# append: 
# adding data to end of file without disturbing the existing data:


# example : 
# with open("application.log", "a", encoding="utf-8") as file:
#     file.write("User logged in\n")

#real life use:
# logs
# transaction histories
# activity records
# audit trails
# event tracking


# append always write to the end.

# Existing content
#         ↓
#         ↓
#        EOF
#         ↓
# New content

# append is very appropriate for sequential records.
# if we r using append to write to a file and a file does not exists , python creates it.


# example : 
# name = input("Enter student name: ")
# age = input("Enter age: ")
# department = input("Enter department: ")

# with open("students.txt", "a", encoding="utf-8") as file:
#     file.write(f"{name},{age},{department}\n")

# print("Student registered successfully.")


# practice : 

# with open("07_File_Handling\data\string.txt","w",encoding="utf-8") as file :
#     file.write("\n")
#     print("string.txt created.")



# try:
#     name       = input("Enter name : ")
#     age        = int(input("Enter ur age : "))
#     department = input("Enter department : ")
#     gpa        = float(input("Enter gpa : "))


#     with open("07_File_Handling\data\string.txt","a",encoding="utf-8") as file:
#         file.write(f"Name : {name} \n")
#         file.write(f"Age : {age} \n")
#         file.write(f"Department : {department} \n")
#         file.write(f"GPA : {gpa} \n")

#     print("added.")


# except ValueError:
#     print("age : integer and gpa : number")

# except PermissionError:
#     print("permission denied.")

# except OSError as e:
#     print(f"Eror : {e}")

# except Exception as e:
#     print("unknown error.")



# sales_report_generator.py

# from datetime import datetime

# try:
#     report_file = "07_File_Handling\data\sales_report.txt"

#     total_sales = 0
#     total_revenue = 0.0

#     num_products = int(input("Enter number of products sold: "))

#     if num_products <= 0:
#         raise ValueError("Number of products must be greater than 0.")

#     with open(report_file, "w") as file:

#         file.write("=" * 50 + "\n")
#         file.write("SALES REPORT\n")
#         file.write(f"Generated: {datetime.now()}\n")
#         file.write("=" * 50 + "\n\n")

#         for i in range(1, num_products + 1):

#             print(f"\nProduct {i}")

#             product_name = input("Product Name: ")

#             quantity = int(input("Quantity Sold: "))
#             if quantity < 0:
#                 raise ValueError("Quantity cannot be negative.")

#             price = float(input("Price Per Unit: "))
#             if price < 0:
#                 raise ValueError("Price cannot be negative.")

#             revenue = quantity * price

#             total_sales += quantity
#             total_revenue += revenue

#             file.write(
#                 f"{product_name:<20} "
#                 f"Qty: {quantity:<5} "
#                 f"Revenue: Rs.{revenue:.2f}\n"
#             )

#         file.write("\n" + "=" * 50 + "\n")
#         file.write(f"Total Units Sold : {total_sales}\n")
#         file.write(f"Total Revenue    : ${total_revenue:.2f}\n")
#         file.write("=" * 50 + "\n")

# except ValueError as e:
#     print(f"Input Error: {e}")

# except PermissionError:
#     print("Permission denied while writing the report.")

# except OSError as e:
#     print(f"File System Error: {e}")

# except Exception as e:
#     print(f"Unexpected Error: {e}")

# else:
#     print("\nSales report generated successfully!")

# finally:
#     print("Program finished.")



# practice 

# student registration system using append mode.
# Write 10 numbers to a file, one per line.
# Write a list of 10 names using writelines()
# Create a program that records every login:



# menu driven student tegisteration system :

file_name = "07_File_Handling\data\student_registeration.txt"


while True: 
    print("\n===== STUDENT REGISTRATION =====")
    print("1. Register Student")
    print("2. View Students")
    print("3. Total Registered Students")
    print("4. Exit")


    choice = input("enter ur choice : ")


    if choice == '1':
        try:
            name = input("Name : ").strip()

            age = int(input("Age : "))
            if age<0:
                raise ValueError("age must be positive.")


            department = input("Department : ").strip()


            with open(file_name,"a",encoding="utf-8") as file:
                file.write(f"{name},{age},{department}\n")

            print("student registered successfully.")


        except ValueError as e:
            print("error ", e)

        except Exception as e:
            print("unexpected error.")

    elif choice == "2":

        try:
            with open(file_name,"r",encoding="utf-8") as file:
                records = file.readlines()

                if len(records)  ==  0:
                    print("no students registered yet.")
                else:
                    print("---- Registered students ----")

                    for student in records:
                        print(student.strip())


        except FileNotFoundError:
            print("file not found.")

        except Exception as e:
            print("unexpected error" , e)


    elif choice  ==  "3":
        try:
            with open(file_name,"r") as file:
                total_students = 0

                for line in file:
                    if line.strip():
                        total_students+=1
                print(f"\n Registered students : {total_students}")

        except FileExistsError:
            print("file not found.")
        except Exception as e:
            print("unexpected arror", e)

    elif choice == "4":
        print("exiting program.")
        break

    else:
        print("invalid choice sellected.")

        

        

