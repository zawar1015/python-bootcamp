# nested try except:A nested try...except block is when you place one try...except structure inside another.
# (in either the try, except, else, or finally block of the outer one).
# This is useful when you have a multi-step operation where each step might fail for different reasons.


# When an exception occurs in the inner block, Python handles it in stages:

# Python checks if the inner except handles that specific exception.
# If it does, the inner except runs, and execution continues smoothly outside the inner block.
# If the inner except does not handle it, the exception bubbles up to the outer except blocks to see if any of them can handle it.


# syntax : 
# try:
#     try:

# example:

# try:
#     print("Outer Try")

#     try:
#         print(10 / 0)

#     except ZeroDivisionError:
#         print("Inner Exception Handled")

# except:
#     print("Outer Exception")


# visual Flow:

#    Outer Try
#         │
#         ▼
#     Inner Try
#         │
#         ▼
#     Exception?
#         │
#         ▼
#    Inner except found?
#         │
#     ┌───┴────┐
#     │        │
#    Yes       No
#     │        │
#     ▼        ▼
#   Handle   Send to Outer Try


# exception Propagation:
# Exception propagation is the process by which an exception travels (or propagates) up the function call stack until it is handled by an except block. 
# If no except block handles it, the program terminates and Python prints a traceback.


# Exception Propagation Works:

#   main()
#      │
#      ▼
#   function_a()
#      │
#      ▼
#   function_b()
#      │
#      ▼
#   function_c()

#  If an exception occurs inside function_c():
#  Python first looks for an except block inside function_c().
#  If none exists, the exception moves to function_b().
#  If function_b() doesn't handle it, it moves to function_a().
#  Finally, it reaches main().
#  If nobody handles it, the program crashes.
#  This movement of the exception is called exception propagation.


# example : 
# def divide():
#     print("Inside divide()")
#     result = 10 / 0      # ZeroDivisionError
#     print(result)

# def calculate():
#     print("Inside calculate()")
#     divide()

# def main():
#     try:
#         calculate()
#     except ZeroDivisionError:
#         print("Cannot divide by zero.")

# main()

# output:
# Inside calculate()
# Inside divide()
# Cannot divide by zero.

# flow:
#  divide()
#      │
#      ▼
#  ZeroDivisionError
#      │
#      ▼
#  calculate()   (not handled)
#      │
#      ▼
#  main()        (handled here)


# example : suppose inner try didnt handle the exception:
# try:
#     try:
#         print(10/0)
#     except ValueError:
#         print("inner")
# except ZeroDivisionError:
#     print("outer")


# internal searching order:

#     Current try
#        ↓
#     Current except
#        ↓
#     Parent try
#        ↓
#     Parent except
#        ↓
#     Next Parent
#        ↓
#     Program Ends


# multiple  nested Levels:
# try:

#     try:

#         try:
#             print(10 / 0)

#         except ZeroDivisionError:
#             print("Level 3")

#     except:
#         print("Level 2")

# except:
#     print("Level 1")



# file processing:
# try:

#     file = open("students.txt")

#     try:
#         data = file.read()
#         print(data)

#     except UnicodeDecodeError:
#         print("Encoding problem.")

#     finally:
#         file.close()

# except FileNotFoundError:
#     print("File not found.")



# example :
# try:
#     print("application opening")
#     try:
#         number = int(input("Enter a number."))
#         print(100/number)

#     except ValueError:
#         print("Enter a valid number.")
#     except ZeroDivisionError:
#         print("number cannot be divide by zero.")

# except Exception as e:
#     print("unexpected application error.")

# finally:
#     print("Application closed.")



