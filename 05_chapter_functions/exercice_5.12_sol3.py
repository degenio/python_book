def calculate_postage(weight: float, destination: str) -> float:
    '''
    Calculate the amount to be paid for postage of a letter

    :param weight: Weight of the letter
    :param destination: Destination of the letter
    :return: The postage amount
    '''
    if weight <= 0 or weight > 50:
        amount = 999
    elif weight <= 30:
        # Validate the destination
        if destination == 'usa':
            amount = 2.71
        else:
            amount = 1.07
    else:  # Weight between 30 and 50
        if destination == 'usa':
            amount = 3.88
        else:
            amount = 1.30

    return amount


def display_amount(amount):
    '''
    Display the postage amount

    :param amount: Amount to be displayed
    :return: None
    '''
    if amount == 999:
        print('Sending not possible')
    else:
        print('The amount is: {0:5.2f}'.format(amount))


def main():
    weight = float(input('Enter the weight between 0 and 50 grams: '))
    destination = input('Enter the destination: ')
    postage_amount = calculate_postage(weight, destination)
    display_amount(postage_amount)
    print("Thank you for using the postal service")


if __name__ == '__main__':
    main()
