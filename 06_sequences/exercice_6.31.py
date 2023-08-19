def input_values(value_count, prompt):
    values_list = []
    for i in range(0, value_count):
        values_list.append(int(input(prompt)))
    return values_list


def determine_consecutive(liste):
    # Check for consecutive values
    if len(liste) == 0:
        print('Calculation not possible')
        return None
    else:
        for i in range(1, len(liste)):
            if liste[i] != liste[i - 1] + 1:
                return False
    return True


def main():
    list_1 = input_values(3, 'Enter an integer value: ')
    print('Elements in the list: {}'.format(list_1))
    # Determine if consecutive
    flag = determine_consecutive(list_1)
    # Display the result
    print('List: {}'.format(flag))
    #Display result
    if flag:
        print('Consecutive')
    else:
        print('Not consecutive')


if __name__ == '__main__':
    main()
