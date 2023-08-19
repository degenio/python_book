# IMC Integration Project
from mod_classes import Patient

risk = ["Increased", "Low", "Increased", "High", "Very High", "Extremely High"]
classification = ["Underweight", "Normal weight", "Overweight", "Obesity class I", "Obesity class II", "Obesity class III"]

def input_value(prompt, error_prompt):
    '''
    Input a value for BMI requirements
    :param prompt: Message for input value
    :param error_prompt: Message in case of input error
    :return: The input value
    '''
    data = float(input(prompt))
    while data <= 0:
        data = float(input(error_prompt))
    return data

def calculate_bmi(patient):
    return patient.weight / patient.height ** 2

def display_bmi(bmi):
    print("Your BMI is: {0:5.2f}".format(bmi))

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
    weight = input_value("Please enter your weight: ", "Please enter a numeric weight greater than 0: ")
    height = input_value("Please enter your height: ", "Please enter a numeric height greater than 0: ")
    name = input("Please enter your name: ")
    age = int(input("Please enter your age: "))

    # Create an object of type Patient
    patient = Patient(name, age, weight, height)
    # Calculate BMI
    bmi = patient.calculate_bmi()
    # Display BMI
    display_bmi(bmi)
    # Determine index
    index = determine_risk_class(bmi)
    # Display risk and classification
    display_risk_class(index)

if __name__ == '__main__':
    main()
