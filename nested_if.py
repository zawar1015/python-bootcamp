# nested if
# a condition inside another condition.

# syntax:
# if a:
#     if b:
#         if c:
#             if d:


# example 1) : 
# age = 25
# citizen = True

# if age >= 18:
#     if citizen:
#         print("Eligible to Vote")
#     else:
#         print("Citizenship Required")
# else:
#     print("Underage")


# logical operators in conditions:
# age = 24
# salary = 70000
# if age >= 18 and salary >= 50000:
#     print("Loan Approved")

# example 2) : 
# if marks >= 60:
#     print("Pass")
# elif marks >= 90:
#     print("Grade A")
# in this condition second condition is never reached.

# Advantage
# Represents hierarchical decisions.
# Disadvantage
# Can become unreadable.


# comparision operators inside if:
# if age > 18:
# if age >= 18:
# if age == 18:
# if age != 18:


# membership testing in conditions.
# if "age" in student:
# if "salary" in df.columns:

# identity testing in conditions.
# if x is None:
# Preferred over
# if x == None:

# logical operators with if: 
# if age > 18 and citizen:
# here logical operator is "and" used to combine multiple conditions.
# the code will be exucuted if both are true.


# use in data cleaning :
# if value is None:
#     value = 0

# time complexity:
# # condition evaluation.
# if x > 5:
# O(1)
# membership check :
# if x in list:
# O(n)
# if x in set:
# O(1)
# membership checking in set is  faster than list.


# two scenaria :

# Scenario 1
# if 1:
#     print("Hello")
# Output:  Hello  because 1 is truthy value.
# Scenario 2:
# if 0:
#    print("Hello")
# Output : Nothing because "0" is false value.

# difference between if-if-if and if-elif-elif:
# if-if-if: multiple blocks of code may execute.
# if-elif-elif: only one condition can run.

# short circuit evaluation:
#Python stops evaluating logical expressions once result is known.

# Why we use  x is None instead of if x == None
# Because None is a singleton object.
# Identity comparison is the intended design.


# use of if in : 

# Machine learning:

# Data analysis(Pandas):
# if df.isnull().sum().sum() > 0:(fill missing values.)
# Numpy:
# if np.mean(data) > threshold:(detect anomalies)
# ETL piplines:
# if file_exists:(read file)
# APIs:
# if response.status_code == 200:(process data)
# Deep Learning:
# if epoch_loss < best_loss:(save best model)
# Computer Vision:
# if confidence > 0.80:(detect object)
# NLP:
# if sentiment == "Positive":(recommended product.)

# Difference between if and elif:
# if starts a conditional block.
# elif checks another condition only if the previous ones were False.

# Difference between else and elif:
# else has no condition and runs if all previous conditions are False.
# lif has its own condition.