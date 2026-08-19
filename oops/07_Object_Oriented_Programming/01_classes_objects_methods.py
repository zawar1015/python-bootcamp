# Object-Oriented Programming (OOP) is a programming paradigm that organizes software around objects containing data and behavior.




# example:

# car :
# data and states:
# brand
# model
# color
# speed
# fuel

# Behavior:
# start()
# stop()
# accelerate()
# brake()

# conceptually:
    #              CAR
    #               |
    #     ---------------------
    #     |                   |
    #   DATA              BEHAVIOR
    #     |                   |
    #   brand               start()
    #   model               stop()
    #   color               accelerate()
    #   speed               brake()



# A class is a blueprint/template that defines the data and behavior that objects created from it can have.

# class:

# class car:
#     pass

# class created but no objects of the class not created yet.


# class vs object:
# A class describes what an object should look like and what it should be able to do.
# An object is an actual instance created from a class.

# conceptually:
# Class
#   ↓
# Blueprint

# Object
#   ↓
# Actual thing

# creating an object:

# class Car:
#     pass


# car1 = Car()
# creates an object.
# car1 is  an instance of Car.
# car():Python creates an object associated with the Car class and returns a reference to that object.

# visualize:
# Car class
#     │
#     │ creates
#     ↓
# ┌─────────────┐
# │   car1      │
# │   object    │
# └─────────────┘

# Object Identity:

# identity of class  is  unique  during its lifetime.
#  identity distinguishes an object from all other objects in a system.
# ensures that an object remains distinct and recognizable, even if it shares the exact same data (state) and methods (behavior) as another object.


# elements of object:
# State: The current data or values stored in the object's attributes.
# Behavior: The actions or methods that the object can perform.
# Identity: The unique handle that makes the object unique in memory

# identity working:
# Memory-Bound: Object identity is handled implicitly by the programming runtime or compiler. It is usually tied directly to the object's unique memory address.
# Independent of State: An object retains its unique identity even if its internal variables or definitions change completely over time.
# No User Key Needed: Unlike databases that rely on primary keys (value-based identity), OO systems assign a built-in identifier automatically without requiring any user-supplied fields.

# identity vs equality:


# Concept           What it means                             How it evaluates
# Identity          Two references point to the exact          obj1 == obj2 (Checks if they are the same instance).
#                   same memory location.                      
# Equality          Two distinct objects happen to hold        obj1.equals(obj2) (Checks if their states match).
#                   the same data values.     
# 


# example:
# class Car:
#     pass


# car1 = Car()
# car2 = Car()

# print(id(car1))
# print(id(car2))

# multiple objects from one class:
# class Student:
#     pass

# student1 = Student()
# student2 = Student()
# student3 = Student()
# All three objects have the same class but can eventually contain different data.

# attributes:
# An attribute is data associated with an object or class.

# example: 
# name
# age
# marks
# department


# class Student:
#     pass


# student1 = Student()

# student1.name = "Ali"
# student1.age = 21
# student1.marks = 85

# print(student1.name)
# print(student1.age)
# print(student1.marks)

# object state: Object state is the collection of data/attribute values that describe an object's current condition.

# student1
#    │
#    ├── name → "Ali"
#    ├── age → 21
#    └── marks → 85



# methods: method is a function defined inside a class that usually represents behavior associated with its objects.

class Student:
    def display(self):
        print("allaudddin")


# display(): is method.
# self is the conventional name for the parameter that refers to the current object when an instance method is called.
# self : not a python keyword.
# example:
# class Student:

#     def display(self):
#         print("Student")

# # when:
# student1 = Student()
# student1.display()
# Python conceptually performs something like:
# Student.display(student1)
# therefore silf refers to self inside that method call.

# technically we can write:
# class Student:

#     def display(current_object):
#         print(current_object)

# class Student:

#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.marks)

# student1 = Student()

# student1.name = "Ali"
# student1.age = 21
# student1.marks = 85

# student1.display()
# object behavior:
# Object behavior describes the operations an object can perform through its methods

# Student
# │
# ├── State
# │   ├── name
# │   ├── age
# │   └── marks
# │
# └── Behavior
#     ├── study()
#     └── attend_class()

# instance method:
# An instance method is a class method designed to operate on a particular object instance and normally receives self.


# model:
#              CLASS
#                │
#       ┌────────┴────────┐
#       │                 │
#     DATA             BEHAVIOR
#   attributes          methods
#       │                 │
#       └────────┬────────┘
#                │
#                ↓
#             OBJECT


# example : 

# class Car:

#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year  = year


#     def display_info(self):
#         print(f"Brand : {self.brand}")
#         print(f"Model : {self.model}")
#         print(f"Year : {self.year}")
#         print("---"*15)




# car1 = Car("Toyota","Corolla",2020)
# car2 = Car("Honda","Civic",2022)
# car3 = Car("Tesla","Model-3",2024)

# car1.display_info()
# car2.display_info()
# car3.display_info()



# class BankAccount:
#     def __init__(self,account_holder,balance):
#         self.account_holder = account_holder
#         self.balance = balance


#     def display(self):
#         print(f"Account holder : {self.account_holder}")
#         print(f"Balance : {self.balance}")
#         print("--"*15)


# account1= BankAccount("ali",3099893)
# account2= BankAccount("allauddin",90)

# account1.display()
# account2.display()


# class Product:
#     def __init__(self,name,price,category):
#         self.name =name
#         self.price = price
#         self.category = category

#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"Price : {self.price}")
#         print(f"Category : {self.category}")
#         print("--"*13)

# laptop = Product("HP","89333","unn-hnn")
# book = Product("any noval","23","unn-hnn")
# cake = Product("bd-cake","83","food")

# laptop.display()
# book.display()
# cake.display()



# student managment system.

class Student:

    def __init__(self,name,age,roll_number,department,marks):
        self.name= name
        self.age = age
        self.roll_number  = roll_number
        self.department = department
        self.marks = marks


    def display_nfo(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll_num : {self.roll_number}")
        print(f"Department : {self.department}")
        print(f"Marks : {self.marks}")
        print("--"*20)




    def study(self):
        print(f"{self.name}  is studying.")
        print("--"*15)

    def attend_class(self):
        print(f"{self.name} is attending class.")
        print("--"*15)



student1 = Student("ali",23,90,"cs",70)
student2 = Student("zawar",20,48,"cs",90)
student3 = Student("noor",27,70,"cs",70)

student1.display_nfo()
student2.display_nfo()
student3.display_nfo()

student1.study()
student2.study()
student3.study()

student1.attend_class()
student2.attend_class()
student3.attend_class()

        


        
        
        