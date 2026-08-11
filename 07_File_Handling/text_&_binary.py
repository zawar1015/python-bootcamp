#                        │   Python Memory / App   │
#                        └────────────┬────────────┘
#                                     │
#            ┌────────────────────────┴────────────────────────┐
#            │                                                 │
#    [ Text Mode: 'r'/'w' ]                           [ Binary Mode: 'rb'/'wb' ]
#            │                                                 │
#    1. Decode / Encode Bytes                         1. Raw Bytes directly
#       (e.g., UTF-8, ASCII)                             (No encoding/decoding)
#            │                                                 │
#    2. Newline Translation                           2. No Translation
#       (\r\n <---> \n)                                  (\r\n stays \r\n)
#            │                                                 │
#            └────────────────────────┬────────────────────────┘
#                                     │
#                        ┌────────────▼────────────┐
#                        │     OS / Disk File      │
#                        └─────────────────────────┘


# The distinction between Text Mode (default) and Binary Mode ('b') isn't just a label.
# it completely changes how Python’s I/O engine processes data in memory and communicates with the underlying Operating System.

# Characters
#    ↓
# Encoding
#    ↓
# Bytes
#    ↓
# Binary data
#    ↓
# File on disk


# storage level representation:
# At the storage level, information is represented as bytes.
# example
# A
# conceptually:
# "A"
#  ↓
# Encoding
#  ↓
# Byte representation
#  ↓
# Storage

# text files:
# .txt
# .csv
# .json
# .py
# .sql
# .md

# Binary files
# Contain arbitrary bytes representing data in a format interpreted by a particular program.
# examples:
# .jpg
# .png
# .pdf
# .xlsx
# .zip
# .exe

# text files need encoding however binary files does not encoding.


# read text:
# "r" -> read
# with open("data.txt", "r", encoding="utf-8") as file:
#     data = file.read()
# returns string
# print(type(data))
# <class 'str'>

# read binary :
# "rb"-> read binary
# with open("data.bin", "rb") as file:
#     data = file.read()
# returns bytes.
# print(type(data))
# <class 'bytes'>

# fundamental difference:
# Text mode
#     ↓
# str

# Binary mode
#     ↓
# bytes

# bytes: consists of 8 bits.
# string vs byte.
# text = "Hello" , type(str)
# data = b"Hello", type(bytes) [b: tells Python this is a bytes literal.]


# reverse operation:
# Bytes
#   ↓
# Decoding
#   ↓
# Python String


# Encoding Example:
# text = "Hello"
# data = text.encode("utf-8")
# print(data)
# output: b'Hello'
# print(type(data)): <class 'bytes'>

# decoding:
# data = b"Hello"
# text = data.decode("utf-8")
# print(text)
# output: hello

# conceptually: 
# encode()
#     str
#      ↓
#    bytes

# decode()
#    bytes
#      ↓
#     str

# there are different encodings:
# some are:
# UTF-8
# UTF-16
# ASCII
# Latin-1 / ISO-8859-1

# ASCII vs UTF-8:
# ASCII represents a limited set of characters.
# UTF-8 can represent a much broader range of Unicode characters.

# Opening a text file:
# with open("anyfile.txt","r",encoding="utf-8") as file:
#     content = file.read()

# python working when we run above code:
# Opens the file.
# Reads bytes from the underlying storage.
# Decodes those bytes using the specified encoding.
# Gives you Python str objects.

# conceptually:
# Disk
#  ↓
# Bytes
#  ↓
# UTF-8 decoder
#  ↓
# str
#  ↓
# Python program


#  opening a binary file:
# with open("binary_file.jpg","rb") as file:
#     data = file.read()

# here python gives u bytes as stored.
# conceptually:
# Disk
#  ↓
# Bytes
#  ↓
# Python bytes object

# image an example of binary data:
# its not  a string , its structured binary data.
# example:
# JPEG
#  ↓
# Binary structure
#  ↓
# Image metadata
#  ↓
# Compressed image data


# reading an image vs bytes:
# with open("07_File_Handling\data\moon.jpg","rb") as file:
#     image_data = file.read()
# print(type(image_data))
# print(len(image_data))
# output: <class 'bytes'>
# length: 213721


# binary writing:
# data = b'Hello'
# with open("data.bin","wb") as file:
#     file.write(data)

# print(data)
# file.write(): above expect bytes-like data.will fail if we pass string.

# text vs binary summary:
#  Feature             : Text        :   Binary                      
#  ------------------- : ---------   :   --------------------------- 
#  Example             : .txt      :   .jpg                      
#  Mode                :  r         :   rb                        
#  Data type           : str       :   bytes                     
#  Encoding            : Yes         :   No text decoding            
#  Newline translation : May occur   :   No text newline translation 
#  Typical use         : Text        :   Images/PDFs/archives        


# t mode : 
# technically python has "rt" read text mode. but "r" already means read text by default.
# so "r" and "rt" as simialar and "w" and "wt".


# binary mode:
# rb  → read binary
# wb  → write binary
# ab  → append binary
# rb+ → read/write binary


# copying a binary file:
# example:
# with open("original.jpg", "rb") as source:
#     data = source.read()

# with open("copy.jpg", "wb") as destination:
#     destination.write(data)

# conceptually:
# original.jpg
#      ↓
#     rb
#      ↓
#    bytes
#      ↓
#     wb
#      ↓
#  copy.jpg

# better to copy in chunks:
# data = source.read(): let say this file is 5GB
# reading it all at once can consume enormous memory
# instead:
# with open("original.jpg", "rb") as source:
#     with open("copy.jpg", "wb") as destination:

#         while True:
#             chunk = source.read(4096)

#             if not chunk:
#                 break

#             destination.write(chunk)

# using chunk workflow:
# 4096 bytes
#    ↓
# write
#    ↓
# 4096 bytes
#    ↓
# write


# file signature/ Magic Bytes:
# Are special bytes stored at the beginning of a file that identify the file's actual format, regardless of its extension.
# with open("07_File_Handling\data\moon.jpg","rb") as file:
#     header = file.read(8)

# print(header)
# file signatures 

# file signature uses:
# Verify file type
# Detect corrupted files
# Prevent fake file extensions
# Recover lost file extensions
# Improve security checks

# file extension isn`t everything:
# report.jpg: will be a valid jpg formate.
# it may contain something completely different.

# validation:
# Filename
# +
# Extension
# +
# MIME type
# +
# File signature


# text file processing:
# with open("07_File_Handling\data\sales_report.txt","r",encoding="utf-8") as file:
#     lines = file.readlines()
# data = [line.strip() for line in lines]
# print(data)


# Encoding error:
# encoding="utf-8"
# If the byte sequence isn't valid under UTF-8, Python may raise:
# UnicodeDecodeError

# best approach:
# Identify source
#      ↓
# Determine encoding
#      ↓
# Use correct encoding
#      ↓
# Validate resulting text


# conceptually:
# What type of data?
#        │
#        ├── Text
#        │    ↓
#        │  encoding?
#        │    ↓
#        │  open(..., encoding="utf-8")
#        │
#        └── Binary
#             ↓
#           rb / wb


# summary:
#                   FILE
#                    │
#           ┌────────┴────────┐
#           │                 │
#         TEXT              BINARY
#           │                 │
#         bytes              bytes
#           │                 │
#       decoding              │
#           ↓                 │
#          str                │
#           │                 │
#       Python text      Python bytes



# practice :
# code and decode.
# text = "allauddin"
# bianary =text.encode("utf-8")
# print(f"Binary : {bianary}")
# string= bianary.decode("utf-8")
# print(f"String : {string}")


# practice : 
# copy and past image :
# source_file= r"C:\Users\zawar\Downloads\Read_write_chunk.jpg"
# destination_file = r"07_File_Handling\data\Read_write_chunk.jpg"

# with open(source_file,"rb") as source:
#     data = source.read()

# with open(destination_file,"wb") as destination_directory:
#     destination_directory.write(data)

# with open(source_file, "rb") as source:
#     with open(destination_file, "wb") as destination:

#         while True:
#             chunk = source.read(4096)

#             if not chunk:
#                 break

#             destination.write(chunk)

# print("image copied successfully.")


# practice :
# read sales.txt , convert to integer and perform some operations.

sales =[]

with open("07_File_Handling\data\sales.txt","r") as file:
    for line in file:
        try:
            sales.append(int(line.strip()))
        except ValueError:
            print("invalid data skipped!",line.strip())


if sales:
    print("Total : ",sum(sales))
    print("Average : ",sum(sales)/len(sales))
    print("Maximum : ",max(sales))
    print("Minimum : ",min(sales))








