#Conversion from meters to feet and feet to meters
distance = float(input('Enter the distance to convert:'))
option = int(input('Enter option 1 or 2: \n1. Convert meters to feet\n2. Convert feet to meters\n'))
if option == 1:
    distance_converted = distance / 0.3048
    print('The distance in feet is:{0:7.2f}'.format(distance_converted))
elif option == 2:
    distance_converted = distance * 0.3048
    print('The distance in meters is:{0:7.2f}'.format(distance_converted))
else:
    print('Invalid option chosen')