def validate_anagram_words(word_1, word_2):
    # Check length
    if len(word_1) != len(word_2):
        return False

    # Build dictionary for word 1
    dict_1 = {}
    for i, c in enumerate(word_1):
        dict_1[i] = c
    # Build dictionary for word 2
    dict_2 = {}
    for i, c in enumerate(word_2):
        dict_2[i] = c

    # Check for anagram
    for k in dict_1.keys():
        for m, n in dict_2.items():
            if dict_1[k] == n:
                dict_2.pop(m)
                break

    # Check length of dict_2: anything other than 0 indicates it's not an anagram
    return len(dict_2) == 0

def main():
    word_1 = input('Enter the first word: ')
    word_2 = input('Enter the second word: ')
    result = validate_anagram_words(word_1.strip().lower(), word_2.strip().lower())
    print('The two words {} anagrams.'.format("are " if result else "are not "))

if __name__ == '__main__':
    main()
