# Version 1 without functions
listing = []
# Input values
for i in range(0, 10):
    listing.append(float(input('Enter a real value: ')))

# Display the values
print('Elements in the list: {}'.format(listing))

# Calculate the average
average = sum(listing) / len(listing)
print('The average of the values is: {:7.2f}'.format(average))


# Version with functions

def input_values(number_of_values, message):
    lst = []
    for i in range(0, number_of_values):
        lst.append(float(input(message)))
    return lst

def calculate_average(lst):
    return sum(lst) / len(lst)

def main():
    # Input values
    listing = input_values(10, 'Enter a real value: ')

    # Display the values
    print('Elements in the list: {}'.format(listing))

    # Calculate the average
    average = calculate_average(listing)
    print('The average of the values is: {:7.2f}'.format(average))

if __name__ == '__main__':
    main()