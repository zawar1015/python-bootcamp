class DuplicateEmployeeError(Exception):
    pass

class InvalidSalaryError(Exception):
    pass

class DepartmentNotFoundError(Exception):
    pass

employees = {
    "EMP001": {
        "name": "Ali",
        "salary": 50000,
        "department": "IT"
    }
}

departments = ["IT", "HR", "Finance", "Marketing"]

MINIMUM_WAGE = 37000

def add_employee(emp_id,name,salary,department):

    if emp_id in employees:
        raise DuplicateEmployeeError(
            f"Employee ID '{emp_id}' already exists."

        )

    if salary < MINIMUM_WAGE:
        raise InvalidSalaryError(
            f"salary cannot be less than minimum wage '{MINIMUM_WAGE}'."

        )

    if department not in departments:
        raise DepartmentNotFoundError(
            f"Department '{department}' does not exists."

        )

        employees[emp_id] = {
        "name": name,
        "salary": salary,
        "department": department
    }

    print("Employee added successfully.")


# Handle Exceptions:

try:
    add_employee(
        "EMP002",
        "Ali",
        60000,
        "IT"
    )


except DuplicateEmployeeError as e:
    print("Duplicate Employee Error:", e)

except InvalidSalaryError as e:
    print("Salary Error:", e)

except DepartmentNotFoundError as e:
    print("Department Error:", e)

except Exception as e:
    print("Unexpected Error:", e)



    