weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
# Calculate BMI using the formula
bmi = weight / (height ** 2)
print("Your BMI is: {0:7.2f}".format(bmi))
