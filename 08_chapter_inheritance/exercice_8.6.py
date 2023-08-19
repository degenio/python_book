OVERTIME_HOURS = 35
OVERTIME_RATE = 1.5
TAX_RATE = 0.20

class Employee:
    """Initializer"""

    def __init__(self, last_name, first_name, code):
        self.last_name = last_name
        self.first_name = first_name
        self.code = code

    def __str__(self):
        return "Last Name: {:<10s} First Name: {:<10s} " \
               "Code: {:<10s}" \
            .format(self.last_name, self.first_name, self.code)

class PartTimeEmployee(Employee):
    def __init__(self, last_name, first_name, code, hours, rate):
        super().__init__(last_name, first_name, code)
        self.hours = hours
        self.rate = rate

    def __str__(self):
        return super().__str__() + ", Worked Hours: {:7.2f} Hourly Rate: {:7.2f} " \
            .format(self.hours, self.rate)

    def calculate_salary(self):
        if self.hours <= OVERTIME_HOURS:
            salary = self.hours * self.rate
        else:
            salary = (self.hours - OVERTIME_HOURS) * OVERTIME_RATE * self.rate + OVERTIME_HOURS * self.rate
        # Tax deduction
        return salary * (1 - TAX_RATE)

class FullTimeEmployee(Employee):
    def __init__(self, last_name, first_name, code, salary):
        super().__init__(last_name, first_name, code)
        self.salary = salary

    def __str__(self):
        return super().__str__() + ", Salary: {:7.2f} " \
            .format(self.salary)

    def calculate_salary(self):
        return self.salary * (1 - TAX_RATE)

def main():
    """Instantiate objects"""
    last_name = input('Enter last name:')
    first_name = input('Enter first name:')
    code = input('Enter code:')
    status = int(input('Enter status by choosing 1 or 2\n1. Full-time\n2. Part-time:\n'))
    # Enter other data based on the status
    if status == 1:
        salary = float(input('Enter salary:'))
        emp_obj = FullTimeEmployee(last_name=last_name, first_name=first_name, code=code, salary=salary)
    else:
        hours = float(input("Enter number of hours:"))
        rate = float(input("Enter hourly rate:"))
        emp_obj = PartTimeEmployee(last_name=last_name, first_name=first_name, code=code, hours=hours, rate=rate)

    # Calculate salary
    print(emp_obj.calculate_salary())

if __name__ == '__main__':
    main()
