import tkinter as tk
from tkinter import ttk

def display():
    product = txt_product.get()
    quantity = float(txt_quantity.get())
    size = size_combobox.get()
    result = 'Product: {}, Size: {}, Quantity: {}'.format(product, size, quantity)
    lbl_result.config(text=result)

# Create the root window
root = tk.Tk()
root.geometry('450x200')
root.title('Sweater Selection')

# Add product section
lbl_product = tk.Label(root, text='Product:')
lbl_product.grid(row=1, column=1, sticky='w', padx=5, pady=5)
txt_product = tk.Entry(root)
txt_product.grid(row=1, column=2, sticky='w', padx=5, pady=5)

# Add size section
lbl_size = tk.Label(root, text='Size:')
lbl_size.grid(row=2, column=1, sticky='w', padx=5, pady=5)

# Combobox creation
size_var = tk.StringVar()
size_combobox = ttk.Combobox(root, width=10, textvariable=size_var)
# Values
size_combobox['values'] = ('Large',
                          'Medium',
                          'Small')
size_combobox.current(1)
size_combobox.grid(row=2, column=2, sticky='w', padx=5, pady=5)

# Add quantity section
lbl_quantity = tk.Label(root, text='Quantity:')
lbl_quantity.grid(row=3, column=1, sticky='w', padx=5, pady=5)
txt_quantity = tk.Entry(root)
txt_quantity.grid(row=3, column=2, sticky='w', padx=5, pady=5)

# Result display
lbl_result = tk.Label(root, font=('arial', 14), fg='red')
lbl_result.grid(row=4, column=2, sticky='w', padx=5, pady=5)

# Add the display button
btn_display = tk.Button(root, text='Display', command=display)
btn_display.grid(row=5, column=2, sticky='w', padx=5, pady=5)

# Display the window
root.mainloop()