import csv

def save_bmi_to_file(file_name, patient):
    with open(file_name, "a", newline="\n") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow((patient.name, patient.age, patient.weight, patient.height))
