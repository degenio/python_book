student_name = input('Enter student name: ')
midterm_exam = float(input('Enter midterm grade: '))
final_exam = float(input('Enter final exam grade: '))
student_average = 0.4 * midterm_exam + 0.6 * final_exam
print('Student name: {} Average: {:.2f}'.format(student_name, student_average))
