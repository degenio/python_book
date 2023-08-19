import tkinter as tk

def show_size():
    selected_product = txt_product.get()
    selected_size = v.get()
    lbl_result.config(text=selected_product + ':' + selected_size, font=('arial', 16))

# Create the root window
root = tk.Tk()
root.geometry('300x150')
root.title('Size Selection')

v = tk.StringVar()
v.set("large")  # initial value

sizes = [("Large", 'large'),
         ("Medium", 'medium'),
         ("Small", 'small')]

# Add product section
lbl_product = tk.Label(root, text='Product:')
lbl_product.grid(row=1, column=1, sticky='w', padx=5, pady=5)
txt_product = tk.Entry(root)
txt_product.grid(row=1, column=2, sticky='w', padx=5, pady=5)

# Add size section
frame = tk.Frame(root)
frame.grid(row=2, column=2, sticky='w', padx=3, pady=5)
i = 2
for size, value in sizes:
    tk.Radiobutton(frame,
                   text=size,
                   padx=5,
                   variable=v,
                   command=show_size,
                   value=value).grid(row=2, column=i, sticky='w', padx=5, pady=5)
    i += 1

lbl_result = tk.Label(root)
lbl_result.grid(row=3, column=2, sticky='w', padx=5, pady=5)

# Display the window
root.mainloop()
