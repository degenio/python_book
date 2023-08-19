# Display the month in full without using a list
option = int(input('Enter the desired month (1-12): '))

if option == 1:
    month = 'January'
elif option == 2:
    month = 'February'
elif option == 3:
    month = 'March'
elif option == 4:
    month = 'April'
elif option == 5:
    month = 'May'
elif option == 6:
    month = 'June'
elif option == 7:
    month = 'July'
elif option == 8:
    month = 'August'
elif option == 9:
    month = 'September'
elif option == 10:
    month = 'October'
elif option == 11:
    month = 'November'
elif option == 12:
    month = 'December'
else:
    month = 'invalid'

print('The chosen month is: {}'.format(month))
