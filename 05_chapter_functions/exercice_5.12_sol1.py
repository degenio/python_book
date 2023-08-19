def calculate_postage(weight: float, destination: str) -> float:
    '''
    Determine the amount to pay for postage of a letter

    :param weight: Weight of the letter
    :param destination: Destination of the letter
    :return: The postage amount
    '''
    if destination == 'usa':
        if weight <= 30:
            amount = 2.71
        elif weight <= 50:
            amount = 3.88

    else:
        if weight <= 30:
            amount = 1.07
        elif weight <= 50:
            amount = 1.3
    return amount


def display_amount(amount):
    '''
    Display the postage amount

    :param amount: Amount to be displayed
    :return: None
    '''
    print('The amount is: {0:5.2f}'.format(amount))


def main():
    # Check the weight
    weight = 0
    while weight > 50 or weight <= 0:
        weight = float(input('Enter the weight between 0 and 50 grams: '))

    destination = input('Enter the destination: ')
    postage_amount = calculate_postage(weight, destination)
    display_amount(postage_amount)


if __name__ == '__main__':
    main()
