# Version 1: Basic solution
input_file = open("hours.csv")
for line in input_file:
    code, name, day1, day2, day3, day4, day5 = line.split()

    # Average
    hours = float(day1) + float(day2) + float(day3) + \
             float(day4) + float(day5)

    print(name, "Code:", code, " worked:", \
          hours, "hours with an average of:", hours / 5, "/ day")
input_file.close()

# Version 2
input_file = open("hours.csv")
for line in input_file:
    data = line.split()
    # Average
    hours = float(data[2]) + float(data[3]) + float(data[4]) + \
             float(data[5]) + float(data[6])
    print('{0:<10s} Code: {1:<3s}  worked: {2:7.2f} hours with an average of {3:7.2f} / day'.format(data[1], data[0], hours, hours / 5))
input_file.close()

# Version 3: Slicing and list comprehension
with open("hours.csv") as input_file:
    for line in input_file:
        data = line.split()
        # Average
        hours = sum([float(x) for x in data[2:7]])
        print('{0:<10s} Code: {1:<3s}  worked: {2:7.2f} hours with an average of {3:7.2f} / day'.format(data[1], data[0], hours, hours / 5))
