#Solution for problem 10.9 without exception handling
class Employee:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age

    def __str__(self):
        return 'Last Name: {}, First Name: {}, Age: {}'.format(self.last_name, self.first_name, self.age)


class EmployeeList:
    def __init__(self):
        self.registry = []

    def add_employee(self, emp):
        self.registry.append(emp)

    def display_employees(self):
        for emp in self.registry:
            print(emp)


if __name__ == '__main__':
    emp1 = Employee('FlouFlou', 'Alain', 25)
    emp2 = Employee('FlouClair', 'Abdel', 34)
    emp3 = Employee('Annie', 'FlouFlou', 22)
    
    # Adding employees
    employee_list = EmployeeList()
    employee_list.add_employee(emp1)
    employee_list.add_employee(emp2)
    employee_list.add_employee(emp3)
    
    # Displaying employees
    employee_list.display_employees()
