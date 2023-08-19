def get_input(message):
    '''
    Returns a value entered by the user
    
    :param message: The message to display to the user
    :return: The value entered by the user
    '''
    return input(message)

# Calling the function
result = get_input("Enter a value:")
print(result)