phrase = input('Enter a sentence: ')
length = len(phrase)
print('The number of characters is: {}'.format(length))

# Count the occurrences of the letter 'a'
counter_a = 0
for char in phrase:
    if char == 'a':
        counter_a += 1
print('The character "{}" appears {} times'.format('a', counter_a))

# Count the occurrences of the letter 'a' or 'A'
counter_a_or_A = 0
for char in phrase:
    if char in ['a', 'A']:
        counter_a_or_A += 1
print('The character "{}" or "{}" appears {} times'.format('a', 'A', counter_a_or_A))
