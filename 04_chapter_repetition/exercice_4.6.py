# Generate a random number
import random
unknown_number = random.randint(1, 100)

# Find the number
tries = 1
number = int(input('Guess the number:'))
while number != unknown_number:
    if number > unknown_number:
        print('Your number is greater!')
    else:
        print('Your number is smaller!')
    tries += 1
    number = int(input('Guess the number:'))

print('Congratulations! You found the number {} in {} attempts.'.format(unknown_number, tries))