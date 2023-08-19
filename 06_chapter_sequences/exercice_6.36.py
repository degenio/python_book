# Version 1

def enter_postal_code(message):
    return input(message)

def validate_postal_code(code):
    # Check length
    if len(code) != 6:
        return 'Invalid code'
    else:
        letters_odd = [x for x in code[0:len(code):2] if not x.isdigit()]
        digits_even = [x for x in code[1:len(code):2] if x.isdigit()]
    return len(letters_odd) == 3 and len(digits_even) == 3 and code[0].upper() not in ["D", "F", "I", "O", "Q", "U", "W", "Z"]

def main():
    postal_code = enter_postal_code('Enter a Canadian postal code: ')
    result = validate_postal_code(postal_code)
    if result:
        print('True canadian postal code')
    else:
        print('Not a canadian postal code')

if __name__ == '__main__':
    main()
