import tkinter as tk
from tkinter import messagebox

def click_btn(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    expr = entry.get()
    try:
        # Evaluate the expression safely
        # Only allow digits and operators to prevent code injection
        if any(c not in "0123456789+-*/.()" for c in expr):
            raise ValueError("Invalid characters")
        result = eval(expr)
        if result == float('inf') or result == float('-inf'):
            raise ZeroDivisionError
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed")
        clear()
    except Exception:
        messagebox.showerror("Error", "Invalid input")
        clear()

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="ridge")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == 'C':
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        command=lambda t=text: click_btn(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
