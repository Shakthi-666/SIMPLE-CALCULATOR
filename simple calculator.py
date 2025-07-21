import tkinter as tk

# Function to handle number and operator button clicks
def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))

# Function to evaluate the expression
def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

# Function to clear the entry for a new calculation
def clear():
    entry_var.set("")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("320x430")
root.resizable(False, False)

# Entry widget
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button layout as list of tuples: (text, row, column)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create calculator buttons
for (text, row, col) in buttons:
    action = equal if text == '=' else lambda x=text: press(x)
    btn = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 14), command=action)
    btn.grid(row=row, column=col, sticky="nsew")

# Clear button across full row
clear_btn = tk.Button(root, text='C', font=("Arial", 14), padx=20, pady=20, bg="red", fg="white", command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, sticky="nsew")

# Start the app
root.mainloop()
