import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_combo.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as zde:
        messagebox.showerror("Math Error", str(zde))

# Main Window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("350x200")

# Input Fields
tk.Label(root, text="First Number:").grid(row=0, column=0, pady=10, sticky="e")
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number:").grid(row=1, column=0, pady=10, sticky="e")
entry2 = tk.Entry(root, width=20)
entry2.grid(row=1, column=1)

# Operation Selection
tk.Label(root, text="Operation:").grid(row=2, column=0, pady=10, sticky="e")
operation_combo = ttk.Combobox(root, values=["+", "-", "*", "/"], state="readonly", width=5)
operation_combo.grid(row=2, column=1, sticky="w")
operation_combo.set("+")

# Calculate Button
calc_btn = tk.Button(root, text="Calculate", command=calculate)
calc_btn.grid(row=3, column=0, columnspan=2, pady=10)

# Result Display
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
