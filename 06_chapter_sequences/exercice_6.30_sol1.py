# version 1

def input_values(value_count, message):
    lst = []
    for i in range(0, value_count):
        lst.append(float(input(message)))
    return lst

def calculate_list_product(list1, list2):
    # Check the length of both lists
    if len(list1) != len(list2) or len(list1) == 0:
        print('Calculation impossible')
        return None
    else:
        result = []
        for i in range(0, len(list1)):
            result.append(list1[i] * list2[i])
        return result

def calculate_list_sum(list1, list2):
    # Check the length of both lists
    if len(list1) != len(list2) or len(list1) == 0:
        print('Calculation impossible')
        return None
    else:
        result = []
        for i in range(0, len(list1)):
            result.append(list1[i] + list2[i])
        return result
        

def main():
    list_1 = input_values(5, 'Enter a real value:')
    print('Elements in the list:{}'.format(list_1))
    list_2 = input_values(5, 'Enter a real value:')
    print('Elements in the list:{}'.format(list_2))

    # List with each element as the sum
    list_sum = calculate_list_sum(list_1, list_2)
    # Display the result
    print('List with each element as the sum:{}'.format(list_sum))

    # List with each element as the product
    list_product = calculate_list_product(list_1, list_2)
    # Display the result
    print('List with each element as the product:{}'.format(list_product))


if __name__ == '__main__':
    main()