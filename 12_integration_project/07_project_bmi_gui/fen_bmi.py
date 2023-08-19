from tkinter import *
from mod_classes import Patient
from mod_files import save_bmi_to_file
from mod_functions import determine_risk_class, risk, classification

def quit():
    root.destroy()

def main_calculate():
    patient = Patient(name.get(), int(age.get()), float(weight.get()), float(height.get()))
    # Call for BMI calculation
    bmi = patient.calculate_bmi()
    # Display BMI, risk, and classification
    lbl_bmi.config(text="{0:5.2f}".format(bmi))
    index = determine_risk_class(bmi)
    lbl_risk.config(text=str(risk[index]))
    lbl_classification.config(text=str(classification[index]))

def save():
    person = Patient(name.get(), int(age.get()), float(weight.get()), float(height.get()))
    # Save to CSV
    save_bmi_to_file("annual_bmi.csv", person)

# Create the main window
root = Tk()
root.title("Body Mass Index Calculation")
root.geometry("380x400")

# Create a frame for the title
frame_title = Frame(root)
title_font = ('arial', 20, 'bold')
label_title = Label(frame_title, text='Patient Data Entry', font=title_font)
label_title.grid(row=1, column=1, padx=5, pady=5)

# Create a frame for graphical components
frame_components = Frame(root)
Label(frame_components, text='Name').grid(row=1, column=1, sticky=E, padx=5, pady=5)
Label(frame_components, text='Age').grid(row=2, column=1, sticky=E, padx=5, pady=5)
Label(frame_components, text='Weight').grid(row=3, column=1, sticky=E, padx=5, pady=5)
Label(frame_components, text='Height').grid(row=4, column=1, sticky=E, padx=5, pady=5)
Label(frame_components, text='BMI:').grid(row=5, column=1, sticky=E, padx=5, pady=5)
Label(frame_components, text='Health Risk:').grid(row=6, column=1, sticky=E, padx=5, pady=5)
Label(frame_components, text='Classification:').grid(row=7, column=1, sticky=E, padx=5, pady=5)

name = Entry(frame_components, width=40)
name.grid(row=1, column=2, columnspan=4, sticky=W)
age = Entry(frame_components, width=10)
age.grid(row=2, column=2, columnspan=4, sticky=W)
weight = Entry(frame_components, width=20)
weight.grid(row=3, column=2, columnspan=4, sticky=W)
height = Entry(frame_components, width=20)
height.grid(row=4, column=2, columnspan=4, sticky=W)
lbl_bmi = Label(frame_components)
lbl_bmi.grid(row=5, column=2, sticky=W)
lbl_risk = Label(frame_components)
lbl_risk.grid(row=6, column=2, sticky=W)
lbl_classification = Label(frame_components)
lbl_classification.grid(row=7, column=2, sticky=W)

# Create a frame for buttons
frame_buttons = Frame(root)
btn_calculate = Button(frame_buttons, text='Calculate', width=15, command=main_calculate)
btn_calculate.grid(row=1, column=1, padx=5, pady=5)
btn_save = Button(frame_buttons, text='Save', width=15, command=save)
btn_save.grid(row=1, column=2, padx=5, pady=5)
btn_cancel = Button(frame_buttons, text='Quit', width=15, command=quit)
btn_cancel.grid(row=1, column=3)

# Place the frames
frame_title.grid(row=1, column=1, columnspan=3, padx=5, pady=5)
frame_components.grid(row=2, column=1, padx=5, pady=5)
frame_buttons.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
