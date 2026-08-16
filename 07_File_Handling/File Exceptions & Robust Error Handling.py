# from pathlib import Path

# try:

#     file = Path(r"07_File_Handling\file_pointers_context_managers.py")
#     data = file.read_text()
#     print(data)

# except FileNotFoundError:
#     print("file not found.")



#               FILE OPERATION
#                     ↓
#               "Could this fail?"
#                     ↓
#                   try
#                     ↓
#               Perform operation
#                     ↓
#           ┌─────────┴─────────┐
#           ↓                   ↓
#        Success              Failure
#           ↓                   ↓
#         else                except
#           ↓                   ↓
#       Continue          Handle problem
#           └─────────┬─────────┘
#                     ↓
#                  finally
#                     ↓
#               Cleanup / finish


# catch exceptions:
# try:
#     file = open("employees.csv", "r")
# except FileNotFoundError:
#     print("The file was not found.")


# common file exceptions:
# file not found error:
# open("missing file.csv")

# permissionError:
# os refuses access.
# this is when u try to access a file  os does not allow it.

# IsDirectoryError:
# u expect file but path points to directory.

# NotADirectoryError:
# A path component that should be a directory isn't one.

# UnicodeDecodeError
# Python tries to decode text using an incompatible encoding.
# Path("data.txt").read_text(encoding="utf-8")

# json.JSONDecodeError
# Invalid JSON structure.
# import json
# json.loads('{"name": "Ali"')



# try:
#     data = Path("employees.csv").read_text()
# except FileNotFoundError:
#     print("Input file is missing.")
# except PermissionError:
#     print("You don't have permission to access the file.")
# except UnicodeDecodeError:
#     print("The file encoding is not supported.")



# exception ordering matters.


# exception hierarchy:
# BaseException
#     │
#     └── Exception
#           │
#           ├── OSError
#           │    ├── FileNotFoundError
#           │    ├── PermissionError
#           │    ├── IsADirectoryError
#           │    └── NotADirectoryError
#           │
#           ├── ValueError
#           │
#           ├── TypeError
#           │
#           └── ...







