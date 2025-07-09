import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        op = operation_combobox.get()

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                result_label.config(text="Error: Divide by zero")
                return
            result = num1 / num2
        else:
            result_label.config(text="Select an operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")

# Number 1
tk.Label(root, text="Number 1:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=10)

# Number 2
tk.Label(root, text="Number 2:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=10)

# Operation Combobox
tk.Label(root, text="Operation:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
operation_combobox = ttk.Combobox(root, values=['+', '-', '*', '/'], state='readonly', width=5)
operation_combobox.grid(row=2, column=1, padx=10, pady=10)
operation_combobox.current(0)

# Calculate Button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
