#Solution for problem 10.9 with custom exception handling
class EmployeeDuplicateError(Exception):
    def __init__(self, emp):
        self.emp = emp

    def __str__(self):
        return self.emp


class Employee:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def __eq__(self, other):
        return self.last_name == other.last_name and self.first_name == other.first_name

    def __str__(self):
        return 'Last Name: {}, First Name: {}, Age: {}'.format(self.last_name, self.first_name, self.age)


class EmployeeList:
    def __init__(self):
        self.registry = []

    def validate_employee(self, emp):
        for existing_emp in self.registry:
            if emp == existing_emp:
                return True
        return False

    def add_employee(self, emp):
        if self.validate_employee(emp):
            raise EmployeeDuplicateError(emp)
        else:
            self.registry.append(emp)

    def display_employees(self):
        for emp in self.registry:
            print(emp)


if __name__ == '__main__':
    emp1 = Employee('FlouFlou', 'Alain', 25)
    emp2 = Employee('FlouClair', 'Abdel', 34)
    emp3 = Employee('FlouFlou', 'Alain', 22)
    
    # Adding employees
    employee_list = EmployeeList()
    try:
        employee_list.add_employee(emp1)
    except EmployeeDuplicateError as e:
        print('Duplicate: Last Name: {}, First Name: {}, Age: {}'.format(e.emp.last_name, e.emp.first_name, e.emp.age))

    try:
        employee_list.add_employee(emp2)
    except EmployeeDuplicateError as e:
        print('Duplicate: Last Name: {}, First Name: {}, Age: {}'.format(e.emp.last_name, e.emp.first_name, e.emp.age))

    try:
        employee_list.add_employee(emp3)
    except EmployeeDuplicateError as e:
        print('Duplicate: Last Name: {}, First Name: {}, Age: {}'.format(e.emp.last_name, e.emp.first_name, e.emp.age))
    
    # Displaying employees
    employee_list.display_employees()
