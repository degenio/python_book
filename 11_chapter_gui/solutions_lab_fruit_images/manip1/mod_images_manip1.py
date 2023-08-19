import tkinter as tk
import random

# List of fruits
fruits = ["apple", "banana", "orange", "mango", "kiwi"]

# Function to verify the answer
def verify_answer():
    pass

# Function to change the fruit
def change_fruit():
    global current_fruit
    global attempts
    attempts = 0
    current_fruit = random.choice(fruits)
    lbl_fruit.config(text=current_fruit)
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Guess the Fruit!")

# Create widgets
lbl_fruit = tk.Label(root, text="", font=("Arial", 14))
lbl_fruit.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.grid(row=1, column=0, columnspan=2, padx=10)

btn_verify = tk.Button(root, text="Verify!", command=verify_answer)
btn_verify.grid(row=1, column=2, columnspan=2, padx=10, pady=10)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0, columnspan=3, padx=10, sticky="w")
 
attempts = 0
lbl_attempts = tk.Label(root, text="Number of attempts: " + str(attempts))
lbl_attempts.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="w")

# Start the game
change_fruit()

# Main window event loop
root.mainloop()