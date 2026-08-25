# Instance Attributes
# An instance attribute is data that belongs to a particular object.


# class Student:


#     def __init__(self,name,marks):

#         self.name = name
#         self.marks = marks


# student1 = Student("ALi",90)
# student2 = Student("alladdin"12)



# student1
# ├── name = "Ali"
# └── marks = 85

# student2
# ├── name = "Ahmed"
# └── marks = 92

# name and marks are instance attributes.
# Because each object has its own values.

# they are called instant attribute because student1 is an instance of Student.
# Therefore:
#The name belonging to this particular instance.



# class attribute:
# class Student:

#     university = "ABC University"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


# university: is a class attribute.
# It belongs to the class rather than being individually created for every object.

# conceptually:
# Student CLASS
# │
# ├── university = "ABC University"
# │
# ├──── student1
# │     ├── name = Ali
# │     └── marks = 85
# │
# └──── student2
#       ├── name = Ahmed
#       └── marks = 92

# Here both students can access the same class attribute.

# Accessing a Class Attribute
# You can access it through the class:
# print(Student.university)
# student1 = Student("ALi",90)
# student2 = Student("alladdin",12)


# You can also access it through an object:
# print(student1.university)
# print(student2.university)


# conceptually:
# student1
#    ↓
# Does student1 have "university"?
#    ↓
# No
#    ↓
# Search Student class
#    ↓
# Found "university"
#    ↓
# Return it
# This is called attribute lookup.

# attribute loookup become extremely important in:
# inheritance
# method resolution order
# properties
# descriptors
# advanced Python internals

# note: Python first looks at the object's attributes and then looks at the class when necessary.


# Instance vs Class Attribute

# class Student:

#     university = "ABC University"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


#  Attribute     Type                  Belongs to         
#  ------------  ------------------    ------------------ 
#  `university`  Class attribute       `Student` class    
#  `name`        Instance attribute    Individual student 
#  `marks`       Instance attribute    Individual student 


# so student1.name and student2.name could be differnt.
# but student1.university and student2.university can use same class-level value.

# we use class attribute when a value logically belongs to the class as a whole.
# examples:

# Company name
# Tax rate
# Default configuration
# Species
# University name
# Maximum allowed connections
# Application version

# class Employee:

#     company = "ABC Technologies"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# The company is shared by employees.


# Dangerous Class Attribute
# Example:
# class Employee:

#     company = "ABC Technologies"

# employee1 = Employee()
# employee2 = Employee()

# Both access: Employee.company
# but if we do:
# employee1.company = "XYZ Technologies"
# we have not changed the class attribute.
# we've created a new instance attribute on employee1.
# This is subtle and very important.


# actual happenings:
# initially:
# Student Class
# └── company = "ABC Technologies"

# employee1
# └── no company attribute

# employee2
# └── no company attribute


# after: employee1.company = "XYZ Technologies"
# Student Class
# └── company = "ABC Technologies"

# employee1
# └── company = "XYZ Technologies"

# employee2
# └── no company attribute

# noe if we print : print(employee1.company)
# returns:
# XYZ Technologies
# print(employee2.company)

# This is because employee1 now has its own attribute.


# Changing the Class Attribute
# Employee.company = "XYZ Technologies"
# Now all objects that don't have their own company attribute will see:

# employee1.company = ...  changes/creates an instance attribute.
# Employee.company = ...   changes the class attribute.


# Mutable Class Attributes:
# class Student:

#     subjects = []

#     def __init__(self, name):
#         self.name = name

# student1 = Student("Ali")
# student2 = Student("Ahmed")

# student1.subjects.append("Python")

# here we append suject to mutable attribute in class using student1 but this will be availible to both student1 and student2


# now if:
# class Student:

#     def __init__(self, name):
#         self.name = name
#         self.subjects = []


# student1 = Student("Ali")
# student2 = Student("Ahmed")

# student1.subjects.append("Python")

# here student2 will now get subjects.


# Instance Methods:
# class BankAccount:

#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount


# deposit() is an instance method.
# It operates on a particular object's state.


#               CLASS
#                 │
#        ┌────────┼────────┐
#        ↓        ↓        ↓
#    Instance    Class    Static
#     Method     Method   Method
#       │          │         │
#      self       cls      neither



# Class Methods
# A class method is a method that operates primarily on the class itself rather than a particular instance.

# example:
# class Employee:

#     company = "ABC Technologies"

#     @classmethod
#     def change_company(cls, new_name): # cls refers to class as self refers to instance
#         cls.company = new_name


# cls.company means:
# The company attribute belonging to the class.

# Calling a Class Method:
# Employee.change_company("UET")
# print(Employee.company)

# You could technically write:
# def change_company(new_name):
#     Employee.company = new_name
# But a class method keeps the behavior logically associated with the class.
# It also becomes especially useful with inheritance.





# Example — Factory Method:
# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary


# Normally:

# employee = Employee("Ali", 80000)

# But perhaps data comes from a string:

# Ali,80000

# We can create a class method:


# class Employee:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     @classmethod
#     def from_string(cls, data):
#         name, salary = data.split(",")
#         return cls(name, int(salary))



# employee = Employee.from_string("Ali,80000")

# This is called a factory method.
# It provides an alternative way to construct an object.

# cls() Instead of Employee()

# Notice:

# return cls(name, int(salary))

# instead of:

# return Employee(name, int(salary))

# This becomes important with inheritance.

# If a subclass calls the inherited class method, cls can refer to that subclass.

# So cls() supports more flexible object construction.


# Static Methods
# A static method is a method placed inside a class because it is logically related to the class, but it doesn't need:
# self
# cls


# syntax:
# class MathHelper:

#     @staticmethod
#     def add(a, b):
#         return a + b

# Put a Static Method Inside a Class:
# Because the function logically belongs to that concept.

# class Employee:

#     @staticmethod
#     def is_valid_salary(salary):
#         return salary >= 0



# class Employee:

#     company = "ABC Technologies"

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     # Instance method
#     def display_info(self):
#         print(self.name)
#         print(self.salary)

#     # Class method
#     @classmethod
#     def change_company(cls, new_name):
#         cls.company = new_name

#     # Static method
#     @staticmethod
#     def is_valid_salary(salary):
#         return salary >= 0




# Does it need instance state?
#        │
#       YES
#        ↓
#  instance method

#        NO
#        ↓
# Does it need class state?
#        │
#       YES
#        ↓
#  class method

#        NO
#        ↓
#  static method



class BankAccount: 
    bank_name = "hbl"


    def __init__(self,owner,balance,account_number):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number




    def deposit(self,amount):
        if BankAccount.is_valid_amount(amount):
            self.balance+=amount
            print(f"deposited : {amount}")
        else:
            print(f"doposited invalid amount!")


    def withdraw(self,amount):
        if not BankAccount.is_valid_amount(amount):
            print("invalid withdrawl amount!")
        else:
            self.balance-=amount
            print(f"withdrawn : {amount}")


    def display_balance(self):
        print(f"owner : {self.owner}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance : {self.balance}")
        print(f"Bank Name:{BankAccount.bank_name}")


    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name


    @staticmethod
    def is_valid_amount(amount):
        return amount >0



account1= BankAccount("Ali",5000,"ACC101")
account2 = BankAccount("Allauddin",3999,"ACC102")

account1.display_balance()
account1.deposit(9000)
account1.withdraw(300)
account1.display_balance()


BankAccount.change_bank_name("ubl")
