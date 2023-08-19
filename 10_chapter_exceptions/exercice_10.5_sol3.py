"""Multiplication of two numbers with exception handling and loop"""
flag = True
while flag:
    try:
        number_1 = float(input('Enter number 1:'))
        number_2 = float(input('Enter number 2:'))
    except ValueError as e:
        print('The value entered is not a number!')
    else:
        result = number_1 * number_2
        print('The product of {} and {} is: {}'.format(number_1, number_2, result))
        flag = False
