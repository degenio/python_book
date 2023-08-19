def input_values(value_count, prompt):
    values_list = []
    for i in range(0, value_count):
        values_list.append(float(input(prompt)))
    return values_list


def calculate_list_product(list1, list2):
    # Check the lengths of the two lists
    if len(list1) != len(list2):
        print('Calculation not possible')
        return None
    else:
        return [x * y for x, y in zip(list1, list2)]


def calculate_list_sum(list1, list2):
    # Check the lengths of the two lists
    if len(list1) != len(list2) or len(list1) == 0:
        print('Calculation not possible')
        return None
    else:
        return [x + y for x, y in zip(list1, list2)]


def main():
    list_1 = input_values(5, 'Enter a real value: ')
    print('Elements in the list: {}'.format(list_1))
    list_2 = input_values(5, 'Enter a real value: ')
    print('Elements in the list: {}'.format(list_2))
    # List with each element being the sum
    list_sum = calculate_list_sum(list_1, list_2)
    # Display the result
    print('List with each element being the sum: {}'.format(list_sum))
    # List with each element being the product
    list_product = calculate_list_product(list_1, list_2)
    # Display the result
    print('List with each element being the product: {}'.format(list_product))


if __name__ == '__main__':
    main()

 
