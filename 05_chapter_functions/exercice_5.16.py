REFUND_RATE = 0.85

def enter_information():
    last_name = input('Last Name: ')
    first_name = input('First Name: ')
    email = input('Email: ')
    amount_paid = float(input('Amount paid for the work: '))
    contribution = float(input('Your contribution: '))
    return last_name, first_name, email, amount_paid, contribution

def calculate_refund(details):
    return details[3] * REFUND_RATE - details[4]

def display_result(details, refund):
    print('Here are the details of the reimbursement request for your expenses:')
    print('Here are the amounts that concern you.')
    print('Amount of necessary work: {}'.format(details[3]))
    print('Your declared contribution: {}'.format(details[4]))
    print('Reimbursement you are entitled to: {}'.format(refund))

# Call functions
information = enter_information()
refund_amount = calculate_refund(information)
display_result(information, refund_amount)
