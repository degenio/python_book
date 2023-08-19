# Conversion between kilograms and pounds
weight = float(input('Enter the weight to convert: '))
option = int(input('Enter option 1 or 2: \n1. Convert kilograms to pounds\n2. Convert pounds to kilograms\n'))

if option == 1:
    converted_weight = weight * 2.20462
    print('The weight in pounds is: {:.2f}'.format(converted_weight))
elif option == 2:
    converted_weight = weight / 2.20462
    print('The weight in kilograms is: {:.2f}'.format(converted_weight))
else:
    print('The chosen option is invalid')
