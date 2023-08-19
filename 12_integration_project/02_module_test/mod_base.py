risk = ['Increased', 'Low', 'Increased', 'High', 'Very High', 'Extremely High']
classification = ['Underweight', 'Normal weight', 'Overweight', 'Obesity class I', 'Obesity class II', 'Obesity class III']

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
# Calculate BMI using the formula
bmi = weight / (height ** 2)
print("Your BMI is: {0:7.2f}".format(bmi))
# Determine risk and classification
if bmi < 18.5:
    index = 0
elif bmi < 25:
    index = 1
elif bmi < 30:
    index = 2
elif bmi < 35:
    index = 3
elif bmi < 40:
    index = 4
else:
    index = 5

print('Classification: {}'.format(classification[index]))
print('Risk: {}'.format(risk[index]))
