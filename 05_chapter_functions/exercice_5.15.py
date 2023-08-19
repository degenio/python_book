from random import randint

LETTER_SIZE = 4
NUMBER_SIZE = 4
ASCII_START = 65
ASCII_END = 90
num = 0

def generate_code():
    global num
    code = ''
    if num == 9999:
        num = 0
    num += 1
    # Generate letters
    for i in range(0, LETTER_SIZE):
        # Generate a random number to get an uppercase letter
        number = randint(ASCII_START, ASCII_END)
        code += chr(number)

    # Form the code by padding if necessary
    return code + str(num).zfill(NUMBER_SIZE)

# Call the function
code1 = generate_code()
code2 = generate_code()

# Display the code
print('The code is: {}'.format(code1))
print('The code is: {}'.format(code2))
