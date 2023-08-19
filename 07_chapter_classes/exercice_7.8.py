OVERTIME_HOURS = 35
OVERTIME_RATE = 1.5

class Employee:
    """Initializer"""
    def __init__(self, last_name, first_name, code, status, salary):
        self.last_name = last_name
        self.first_name = first_name
        self.code = code
        self.status = status
        self.salary = salary

    def __str__(self):
        return "Last Name:{:<10s} First Name: {:<10s} " \
               "Code: {:<10s} Status: {:<15s}, Salary:{:7.2f} " \
               .format(self.last_name, self.first_name, self.code, self.status, self.salary)

def main():
    """Instantiate object"""
    last_name = input('Enter the last name:')
    first_name = input('Enter the first name:')
    code = input('Enter the code:')
    status = int(input('Enter the status by choosing 1 or 2\n1. Full-time\n2. Part-time:\n'))
    # Enter the other data based on status
    if status == 1:
        salary = float(input('Enter the salary:'))
    else:
        hours = float(input("Enter the number of hours:"))
        rate = float(input("Enter the hourly rate:"))
        # Calculate the salary based on status
        if hours <= OVERTIME_HOURS:
            salary = hours * rate
        else:
            salary = (hours - OVERTIME_HOURS) * OVERTIME_RATE * rate + OVERTIME_HOURS * rate

    obj1 = Employee(last_name=last_name, first_name=first_name, code=code, salary=salary,
                    status='FULL-TIME' if status == 1 else 'PART-TIME')
    print(obj1)

if __name__ == '__main__':
    main()
