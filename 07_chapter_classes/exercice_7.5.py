# Class Student
class Student:
    """Initializer"""
    def __init__(self, last_name, first_name, gender, address, student_code, final_grade):
        self.last_name = last_name
        self.first_name = first_name
        self.gender = gender
        self.address = address
        self.student_code = student_code
        self.final_grade = final_grade

    def __str__(self):
        return "Student  last name: {:<10} first name: {:<10} " \
               "gender: {:<7} address: {:<20} code: {:<8} " \
               "final grade: {:<8}".format(self.last_name, self.first_name, self.gender,
                                           self.address, self.student_code, self.final_grade)

    def do_homework(self):
        print("I am a diligent student")


def main():
    """Instantiate objects"""
    obj1 = Student(first_name="Alain", last_name="Flouflou", gender="M", address="14 Park Street",
                   student_code="118907",
                   final_grade=78)
    print(obj1)

    # Call the method do_homework
    obj1.do_homework()


if __name__ == '__main__':
    main()