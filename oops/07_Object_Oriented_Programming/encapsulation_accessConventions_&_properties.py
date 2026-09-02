# . Encapsulation
# Definition:
# Encapsulation is the practice of bundling data and the operations that work on that data together while controlling how internal state is accessed or modified.

# encapsulation:
# Outside world
#       ↓
# Controlled interface
#       ↓
# Object's internal state


# python attributes are public by default.


# example:
# class Student:
#     def __init__(self,name):
#         self.name = name


# student1 = Student("allauddin")
# student1.name = "ahmad"
# print(student1.name)

# Public attributes are appropriate when direct access is safe and simple.

# Python's Philosophy:
# Python generally relies heavily on:
# Convention and developer responsibility rather than strict access enforcement.
# Python gives you mechanisms for communicating:
# "Please don't touch this directly."
# rather than always preventing access at the language level.


# single underscore _:
# consider:
# class Employee:
#     def __init__(self,name,salary):
#         self.name= name
#         self._salary = salary

# _salary: intended for internal use.
# this is convention not a hard security boundary.
# we can still access employee._salary = 999, python wouldnot stop us.
# "This is an implementation detail. Don't normally interact with it directly."
# This becomes particularly useful in larger projects and libraries.


# double underscore:
# class Bankaccount:
#     def __init__(self,balance):
#         self.__balance = balance


# account = Bankaccount(9999)
# print(account.__balance)

# error: AttributeError: 'Bankaccount' object has no attribute '__balance'
# __attribute  ──>  _ClassName__attribute


# Python's double underscore does not mean:
# Absolutely impossible to access.
# Instead, it provides:
# name collision avoidance
# stronger indication of internal implementation
# protection against accidental overriding in subclasses


# name mangling: Name mangling is a programming trick where a compiler or interpreter changes a variable or function name into a new, unique token. This stops naming fights between different parts of code.

#  Syntax       :     Meaning                          
#  --------     :     -------------------------------- 
#  `name`       :     Public                           
#  `_name`      :     Internal/protected by convention 
#  `__name`     :     Name-mangled/private-like        



# old getter setter approach:
# class Employee:

#     def __init__(self, salary):
#         self._salary = salary

#     def get_salary(self):
#         return self._salary

#     def set_salary(self, salary):
#         if salary >= 0:
#             self._salary = salary



# employee = Employee(80000)

# print(employee.get_salary())

# employee.set_salary(90000)



# python gives something cleaner:
# @property
# The property mechanism lets us expose a method as if it were an attribute.

# class Employee:

#     def __init__(self, salary):
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary


# employee = Employee(80000)

# print(employee.salary)


# this method allow us to have a clean interface.

# External interface
#         ↓
# employee.salary
#         ↓
# @property
#         ↓
# _internal state



# property getter:
# method decorated with @property is getter.

# class Employee:

#     def __init__(self, salary):
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary


# employee = Employee(80000)
# print(employee.salary)



# Python effectively invokes the property getter.


# property setter:
# class Employee:

#     def __init__(self, salary):
#         self._salary = salary

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, value):
#         if value < 0:
#             raise ValueError("Salary cannot be negative")

#         self._salary = value

# employee = Employee(80000)
# employee.salary = 90000
# print(employee.salary)



# class BankAccount:


#     def __init__(self,owner,balance):
#         self.owner = owner
#         self._balance = balance

#     @property
#     def balance(self):
#         return self._balance


#     @balance.setter

#     def balance(self,value):
#         if value<0:
#             raise ValueError("Balance cannot be negative")

#         self._balance = value


# account = BankAccount("alauddin","8999")
# print(account.balance)
# print(account.owner)


# properties can compute values:

# property doesnot have to simply return an underlying variable.

# class Rectangle:

#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     @property
#     def area(self):
#         return self.length * self.width

# rectangle = Rectangle(10, 5)

# print(rectangle.area)



# encapsulation is not about hiding everything.
# it is about that : 
# "Which state should be directly accessible, and which state needs controlled access?"


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     # Property for owner
#     @property
#     def owner(self):
#         return self._owner

#     @owner.setter
#     def owner(self, value):
#         if not value.strip():
#             raise ValueError("Owner name cannot be empty.")
#         self._owner = value

#     # Property for balance
#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, value):
#         if value < 0:
#             raise ValueError("Balance cannot be negative.")
#         self._balance = value

#     # Deposit method
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be greater than zero.")
#         self._balance += amount
#         print(f"Deposited: ${amount}")

#     # Withdraw method
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be greater than zero.")

#         if amount > self._balance:
#             raise ValueError("Insufficient balance.")

#         self._balance -= amount
#         print(f"Withdrawn: ${amount}")

#     def display_balance(self):
#         print(f"Owner: {self._owner}")
#         print(f"Balance: ${self._balance}")


# account = BankAccount("Zawar", 1000)

# account.display_balance()

# account.deposit(500)
# account.display_balance()

# account.withdraw(300)
# account.display_balance()


