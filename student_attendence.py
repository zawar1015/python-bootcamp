# student managment system.

t_students = int(input("Enter total number of students : "))
s_names = []
for student in range(t_students):
    name =input(f"Enter student {student +1}  name .") 
    s_names.append(name)


# search for student

# membership = input("enter student name to search membership.")
# if membership in s_names:
#     print("present")
# else:
#     print("absent")


present = []
absent  =[]
for name in s_names:
    attendence = input(f"is {name} Present (P) or Absent(a) : ").upper()

    if attendence == "P":
        present.append(name)
    elif attendence == "A":
        absent.append(name)
    else:
        print("invalid input")


# print Total student
print("\n-----Total students are.----")
for i in s_names:
    print(i)


print("\n-----Present students are.----")
# present students
for i in present:
    print(i)

print("\n-----Absent students are.----")
# absent students 
for i in absent:
    print(i)  


# Attendence percentage
total_students = len(s_names)
present_students = len(present)

attendance_percentage = (present_students / total_students) * 100

print("\n-----students attendence percentage .----")
print(f"Attendance Percentage: {attendance_percentage:.2f}%")

    





