# Version 1 - Using string slicing

def validate_palindrome_word(word):
    return word == word[::-1]

def main():
    word = input('Enter a word: ')
    result = validate_palindrome_word(word.strip().lower())
    print('{}is a palindrome word.'.format("It " if result else "It is not "))

if __name__ == '__main__':
    main()
