def calculate_change(total_amount, amount_given):
    '''
    Calculate the change to be given in denominations of banknotes
    
    :param total_amount: The total amount to be paid
    :param amount_given: The amount given by the customer
    :return: A tuple of banknote denominations to be given in $20, $10, $5, and $1 bills
    '''
    change = amount_given - total_amount
    twenties = change // 20
    tens = (change % 20) // 10
    fives = (change % 10) // 5
    ones = change - twenties * 20 - tens * 10 - fives * 5
    return twenties, tens, fives, ones

# Call the function
change_given = calculate_change(95, 98)
print('Twenties: {0}, Tens: {1}, Fives: {2}, Ones: {3}'.format(
    change_given[0], change_given[1], change_given[2], change_given[3]))
