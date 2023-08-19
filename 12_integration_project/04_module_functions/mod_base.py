# BMI Calculation
classification = ["Underweight", "Normal weight", "Overweight", "Obesity class I", "Obesity class II", "Obesity class III"]
risk = ["Increased", "Low", "Increased", "High", "Very High", "Extremely High"]

def input_value(prompt, error_prompt):
    value = float(input(prompt))
    while value <= 0:
        value = float(input(error_prompt))
    return value

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def display_bmi(value):
    print("Your BMI is: {0:7.2f}".format(value))

def determine_risk_class(bmi):
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

    return index

def display_risk_class(index):
    print("Classification: {0:20s}".format(classification[index]))
    print("Risk: {0:20s}".format(risk[index]))

def main():
    # Enter weight
    weight = input_value("Enter weight: ", "Enter weight > 0: ")
    # Enter height
    height = input_value("Enter height: ", "Enter height > 0: ")
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    # Display BMI
    display_bmi(bmi)
    # Determine index
    index = determine_risk_class(bmi)
    # Display risk and classification
    display_risk_class(index)

if __name__ == '__main__':
    main()
