# BaseException: root of all exceptions.
# simplified hierarchy:
# BaseException
# │
# ├── SystemExit
# ├── KeyboardInterrupt
# ├── GeneratorExit
# │
# └── Exception
#      │
#      ├── ArithmeticError
#      │     ├── ZeroDivisionError
#      │     ├── OverflowError
#      │     └── FloatingPointError
#      │
#      ├── LookupError
#      │     ├── IndexError
#      │     └── KeyError
#      │
#      ├── ValueError
#      ├── TypeError
#      ├── NameError
#      ├── AttributeError
#      ├── FileNotFoundError
#      ├── ImportError
#      ├── RuntimeError
#      └── ...


# example :
# try:
#     my_list = [1, 2, 3]
#     print(my_list[10])

# except LookupError:
#     print("Lookup Error")
# output : LookupError

# this is an index error (out of range)
# IndexError is child of Lookup Error.

# exception catching :
# specific to general.(correct order)

# let say : 
# except ZeroDivisionError:
#     ...
# 
# except ArithmeticError:
#     ...
# 
# except Exception:
#     ...

# The general handler prevents the specific one from ever running.

# common buil-in exceptions:
#    Exception              When It Happens         
#    --------------------  ----------------------- 
#    ValueError             Right type, wrong value 
#    TypeError              Wrong data type         
#    IndexError             Invalid list index      
#    KeyError               Dictionary key missing  
#    NameError              Variable not defined    
#    AttributeError         Object has no attribute 
#    ImportError            Import failed           
#    ModuleNotFoundError    Module missing          
#    FileNotFoundError      File doesn't exist      
#    PermissionError        No permission           
#    RuntimeError           Generic runtime problem 
#    MemoryError            Out of memory           
#    RecursionError         Too much recursion      


# Best Practices

#  Catch the most specific exception possible.
#  Keep except Exception: as the last handler.
#  Never place a parent exception before its child.
#  Use custom exceptions for business rules.
#  Read traceback messages—they tell you the exact exception type.



# example:

def divide_numbers():
    try:
        number=int(input("Enter a number : "))
        result = 100/number
        print(f"Result : {result}")

    except ZeroDivisionError:
        print("u cannot divide by 0")
    except ArithmeticError:
        print("An arthematic error occured.")
    except ValueError:
        print("Enter valid value")
    except Exception as e:
        print("unknown error occured.", e)
    finally:
        print("program finished.")

divide_numbers()