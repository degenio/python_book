# Determine the total of even numbers needed to reach a given number
a = int(input('Enter a:'))
total = 0
i = 1
while total < a:
    print(2 * i)
    total += 2 * i
    i += 1

print('We need the first {} even numbers'.format(i - 1))