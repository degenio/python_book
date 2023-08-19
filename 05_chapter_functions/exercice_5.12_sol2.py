def calculate_postage(weight: float, destination: str) -> float:
    '''
    Calculate the amount to be paid for postage of a letter

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
    weight = float(input('Enter the weight between 0 and 50 grams: '))
    if weight <= 0 or weight > 50:
        print("The weight exceeds the mailing limits")
    else:
        destination = input('Enter the destination: ')
        postage_amount = calculate_postage(weight, destination)
        display_amount(postage_amount)
    print("Thank you for using the postal service")


if __name__ == '__main__':
    main()
