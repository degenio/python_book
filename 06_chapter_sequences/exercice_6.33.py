import random

def generate_lotto_sequence(length, number_range):
    lotto_sequence = set()
    while len(lotto_sequence) <= length:
        lotto_sequence.add(random.randrange(number_range))
    return lotto_sequence

def main():
    length = 6
    number_range = 49
    result = generate_lotto_sequence(length, number_range)
    print('The lotto sequence is: {} '.format(result))

if __name__ == '__main__':
    main()
