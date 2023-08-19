####### Solution 1 #######
# Loop until 999 is entered
number = int(input('1. Enter a value. Enter 999 to stop: '))
total = 0
counter = 0

while number != 999:
    total += number
    counter += 1
    number = int(input('1. Enter a value. Enter 999 to stop: '))

average = total / counter
print('Sum is: {} and the average is: {}'.format(total, average))


####### Solution 2 with rounding to 2 decimal places #######
# Loop until 999 is entered
number = int(input('2. Enter a value. Enter 999 to stop: '))
total = 0
counter = 0

while number != 999:
    total += number
    counter += 1
    number = int(input('2. Enter a value. Enter 999 to stop: '))

average = total / counter
print('Sum is: {} and the average is: {}'.format(round(total, 2), round(average, 2)))


####### Solution 3 with total of positive numbers and count of zeros #######
# Loop until 999 is entered
number = int(input('3. Enter a value. Enter 999 to stop: '))
total = 0
counter = 0
positive_sum = 0
zero_count = 0

while number != 999:
    total += number
    counter += 1
    if number == 0:
        zero_count += 1
    elif number > 0:
        positive_sum += number

    number = int(input('3. Enter a value. Enter 999 to stop: '))

average = total / counter
print('Sum is: {} and the average is: {}'.format(round(total, 2), round(average, 2)))
print('Sum of positive numbers: {}'.format(positive_sum))
print('Number of occurrences of zero: {}'.format(zero_count))
