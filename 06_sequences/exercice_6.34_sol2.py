# Version 1 - Using string slicing
# Palindrome in a sentence instead of a word

def validate_palindrome_phrase(phrase):
    # Consider only letters and digits using isalnum()
    phrase = ''.join([x for x in phrase.strip().lower() if x.isalnum()])
    print(phrase)
    return phrase == phrase[::-1]

def main():
    sentence = input('Enter a sentence: ')
    result = validate_palindrome_phrase(sentence.strip().lower())
    print('{}is a palindrome sentence.'.format("It " if result else "It is not "))

if __name__ == '__main__':
    main()
