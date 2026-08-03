# Mini Project

# Build a Student Registration System with functions that use:

# Positional arguments
# Keyword arguments
# Default arguments
# *args
# **kwargs


def register_student(name,id,department,status = "active", *courses,**student_info):
    print("=========== Register Student =============")
    print(f'{{"Name": "{name}", "ID": "{id}", "Department": "{department}"}}')




def add_courses(*courses):
    print("\nRegistered Courses:")
    if courses:
        for course in courses:
            print(f"- {course}")
    else:
        print("No courses selected.")


def student_details(**details):
    print("\nAdditional Details:")
    if details:
        for key, value in details.items():
            print(f"{key.capitalize()} : {value}")
    else:
        print("No additional details.")


register_student("Zawar Hussain", "DS-101", "Data Science")

add_courses(
    "Python Programming",
    "Machine Learning",
    "Database Systems",
    "Statistics"
)

student_details(
    age=21,
    gender="Male",
    city="Peshawar",
    email="hhhhhhhh@gmail.com",
    semester=3,
    cgpa=3.78
)