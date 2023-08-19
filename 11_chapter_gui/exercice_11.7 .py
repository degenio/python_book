import tkinter as tk
def calculate():
    name_text = ent_name.get().upper()
    ent_name.delete(0, tk.END)
    ent_name.insert(0, name_text)
    salary = float(txt_salary.get()) + 1000
    lbl_result.config(text=str(salary))

# Create the root window
root = tk.Tk()
root.geometry('400x200')
root.title('Salary Calculator')

# Add name section
lbl_name = tk.Label(root, text='Name:')
lbl_name.grid(row=1, column=1, sticky='w', padx=5, pady=5)
ent_name = tk.Entry(root)
ent_name.grid(row=1, column=2, sticky='w', padx=5, pady=5)

# Add salary section
lbl_salary = tk.Label(root, text='Salary:')
lbl_salary.grid(row=2, column=1, sticky='w', padx=5, pady=5)
txt_salary = tk.Entry(root, font=('arial', 14))
txt_salary.grid(row=2, column=2, sticky='w', padx=5, pady=5)

# Result display
lbl_result = tk.Label(root, font=('arial', 14), fg='red')
lbl_result.grid(row=3, column=2, sticky='w', padx=5, pady=5)

# Add the calculate button
btn_calculate = tk.Button(root, text='Calculate', command=calculate)
btn_calculate.grid(row=4, column=2, sticky='w', padx=5, pady=5)

# Display the window
root.mainloop()