def convert_seconds(seconds):
    '''
    Calculate the number of hours, minutes, and seconds

    :param seconds: The number of seconds to convert
    :return: The tuple containing the number of hours, minutes,
    and seconds
    '''
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = ((seconds % 3600) % 60)
    return hours, minutes, remaining_seconds

# Calling the function
result = convert_seconds(89568578)
print('Hours: {0}, Minutes: {1}, Seconds: {2}'.format(
    result[0], result[1], result[2]))