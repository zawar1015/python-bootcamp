# CSV and JSON are standard plain-text formats for storing and exchanging data.
# csv: comma separatedd value.
# example:
# name,age,department
# Ali,21,Data Science
# Ahmed,22,Computer Science
# Sara,20,Artificial Intelligence

# conceptually:
# Rows
#  ↓
# Records

# Columns
#  ↓
# Fields


#  A CSV resembles a spreadsheet table:
#  
#  name	     age	department
#  Ali	     21	    Data Science
#  Ahmed     22	    Computer Science
#  Sara	     20	    Artificial Intelligence

#  Feature             CSV (Comma-Separated Values)                          JSON (JavaScript Object Notation)
#  Structure           Tabular (2D Grid / Rows & Columns)                   Hierarchical (Nested Trees / Key-Value Pairs)
#  Data Types          Strings only (Types must be inferred)                "Strings, Numbers, Booleans, Lists, Objects, null"
#  Complexity          "Simple, flat data"                                  "Complex, nested,       or relational data"
#  Human Readability   "Easy in spreadsheet tools (Excel, Sheets)",          Easy for structured web/developer payloads
#  File Size           "Smaller (Low overhead, no field keys repeated)"     Larger (Keys repeated for every record)


# CSV files can contain:
# commas
# quotes
# newlines
# special characters

# example :
# name,city,comment
# Ali,Lahore,"Excellent student, very hardworking"
# 
# mpte: The comma inside the quoted comment doesn't represent a new column.


# Python's csv Module:
# import csv
# common Tools:
# csv.reader()
# csv.writer()
# csv.DictReader()
# csv.DictWriter()

# Reading a CSV:
# Suppose:
# students.csv: contain:
# name,age,department
# Ali,21,Data Science
# Ahmed,22,Computer Science
# Sara,20,AI

# reading from csv:

# import csv

# with open("07_File_Handling\data\student.csv","r",encoding="utf-8", newline="") as file:
#     reader = csv.reader(file)

#     for row in reader:
#         print(row)

# ['name', 'age', 'department']
# ['Ali', '21', 'Data Science']
# ['Ahmed', '22', 'Computer Science']
# ['Sara', '20', 'AI']

# note: 21 is returned as string not integer.
# CSV is fundamentally text.

# newline:
# recommended while opening csv.
# allow csv module to handle newline characters correctly, particullarly across plateforms.


# best practice: with open("file.csv", newline="", encoding="utf-8") as file:


# header row:
# Most CSV datasets have a header:
# name,age,department(this is not actual data , its meta data.)


# import csv

# with open("07_File_Handling\data\student.csv","r",encoding="utf-8", newline="") as file:
#     reader = csv.reader(file)

#     header = next(reader) next(reader) retrieves the first row.

#     print(header)
#     for row in reader:
#         print(row)


# DictReader:

# import csv

# with open("07_File_Handling\data\student.csv","r",newline="",encoding="utf-8") as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row["name"])
#         print(row["age"])
#         print(row["department"])


# dictReader : more descriptve.
# if the order of columns changes still it works.



# writing csv:
# syntax:
# csv.write()


# import csv

# with open("07_File_Handling\data\student.csv","a",newline="",encoding="utf-8") as file:

#     writer = csv.writer(file)


#     # writer.writerow(["name","age","department"])

#     writer.writerow(["waqas",22,"ai"])
#     writer.writerow(["zain",30,"kadoo"])
#     writer.writerow(["awais",13,"cs"])
#     writer.writerow(["allauddin",30,"ai"])
#     writer.writerow(["albert",78,"ai"])



# multiple writing:

# import csv
# rows =[
#     ["zahid",34,"electrical"],
#     ["noor",23,"electrical"],
#     ["anas",23,"cs"]
# ]

# with open("07_File_Handling\data\student.csv","a",newline="",encoding="utf-8") as file:

#     writer = csv.writer(file)

#     writer.writerows(rows)


# dictionary based:

# students =[
#     {
#         "name" : "ali",
#         "age"  : "21",
#         "department": "cs"
#     },
#     {
#         "name" : "sheik",
#         "age"  : "32",
#         "department" : 'ai'
#     }
# ]


# import csv

# fieldnames =["name","age","department"]

# with open("07_File_Handling\data\student.csv","a",newline="",encoding="utf-8") as file:

#     writer = csv.DictWriter(
#         file,
#         fieldnames= fieldnames
#     )



#     writer.writerows(students)



# csv qouting:

# suppose:
# row =[
#     "ali",
#     "rawalpindi,pakistan",
#     "datascience"
# 
# writer.writerow(row)
# A proper CSV writer handles this:



# Manual Approach:
# data = [
#     ["Ali", 21],
#     ["Ahmed", 22]
# ]

# for row in data:
#     line = ",".join(map(str, row))

# This can work for extremely simple data.

# But real CSV files can contain:

# commas
# quotes
# newlines
# empty values
# special characters



# json: JavaScript Object Notation

# APIs
# Web applications
# configuration files
# data exchange
# automation
# machine learning services

# syntax:
# {
#     "name": "Ali",
#     "age": 21,
#     "department": "Data Science"
# }

# json look like python dictionaries:

# python:
# student = {
#     "name": "Ali",
#     "age": 21,
#     "department": "Data Science"
# }
# python dictionary.

# json:
# {
#     "name": "Ali",
#     "age": 21,
#     "department": "Data Science"
# }
# json: serialized text/data representation
# Serialized text is the process of converting complex data structures, objects, or memory states into a sequential string of text characters or bytes.
#  This format lets you easily save data to a file or send it across a computer network.


# Python's json Module:
# import json

# important functions:
# json.load()
# json.loads()
# json.dump()
# json.dumps()


# load() vs loads():

# load
#  ↓
# from file

# loads
#  ↓
# from string

# example : 
# json.load(file)
# json.loads(text) reads json from string.


# dump() vs dumps():
# dump
#  ↓
# to file

# dumps
#  ↓
# to string


# write json to file:
# syntax: json.dump(data, file)

# convert Python data into a JSON string:
# json.dumps(data)

# reading json from a file:
# suppose:
# student.json : contain:
# {
#     "name": "Ali",
#     "age": 21,
#     "department": "Data Science"
# }


# import json 

# with open("07_File_Handling\data\student.json","r", encoding="utf-8") as file:
#     student = json.load(file)

#     print(student)

# output: 
#{'name': 'Ali', 'age': 21, 'department': 'Data Science'}
# python has converted json object to python dictionary.



# JSON → Python:
# conversion called deserialization.


# conceptually:
# JSON
#  ↓
# json.load()
#  ↓
# Python object

# example : 
# JSON object → dict
# JSON array → list
# JSON string → str
# JSON number → int/float
# JSON true → True
# JSON false → False
# JSON null → None



# Python → JSON:


# student = {
#     "name"   : "haseeb",
#     "age"    : 32,
#     "skills" : ["python","ML","power bi"]
# }
# import json

# with open("07_File_Handling\data\student.json","w",encoding="utf-8") as file:

#     json.dump(student,file,indent=4)


# dumps():

# suppose:
# import json
# data = {
#     "name": "Ali",
#     "age": 21
# }
# json_text = json.dumps(data)
# print(type(json_text))
# output: <class 'str'>

# json.dumps() doesn't give you a dictionary.
# It gives you a JSON-formatted string.


# import json 

# json_text = '{"name": "Ali", "age": 21}'

# data = json.loads(json_text)

# print(data)  : output: {'name': 'Ali', 'age': 21}
# print(type(data)) returns: <class 'dict'>


# conceptually: 
# FILE → Python       json.load()

# STRING → Python     json.loads()

# Python → FILE       json.dump()

# Python → STRING     json.dumps()

# Nested JSON:
#example: 
# import json
# data = {
#     "name": "Ali",
#     "age": 21,
#     "skills": [
#         "Python",
#         "SQL",
#         "Power BI"
#     ],
#     "address": {
#         "city": "Rawalpindi",
#         "country": "Pakistan"
#     }
# }


# print(data["address"]["country"])



# json arrays:
# JSON arrays correspond roughly to Python lists.

import json

# json_array = [
#     {
#         "name": "Ali",
#         "age": 21
#     },
#     {
#         "name": "Sara",
#         "age": 20
#     }
# ]

# with open("07_File_Handling\data\student.json","w",encoding="utf-8") as file:

#     json.dump(json_array,file,indent=4)


with open("07_File_Handling\data\student.json","r",encoding="utf-8") as file:
    json_array = json.load(file)
    for array in json_array:
        print(json_array["name"])
        print(json_array["age"])

    print(json_array)


# output: [{'name': 'Ali', 'age': 21}, {'name': 'Sara', 'age': 20}]

# JSON array
#    ↓
# Python list
#     ↓
# Python dictionaries


# processing json records:




































