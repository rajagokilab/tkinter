import tkinter as tk
from tkinter import messagebox

def add_expense():
    item = item_entry.get().strip()
    amount_str = amount_entry.get().strip()

    if not item:
        messagebox.showwarning("Input Error", "Please enter an item name.")
        return
    try:
        amount = float(amount_str)
        if amount < 0:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid positive amount.")
        return

    # Add to list and update display
    expenses.append((item, amount))
    update_expense_list()
    item_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)

def update_expense_list():
    expenses_text.delete('1.0', tk.END)
    total = 0
    for idx, (item, amount) in enumerate(expenses, 1):
        expenses_text.insert(tk.END, f"{idx}. {item} - ${amount:.2f}\n")
        total += amount
    total_label.config(text=f"Total Expenses: ${total:.2f}")

root = tk.Tk()
root.title("Expense Tracker")

# Expenses list storage
expenses = []

# Form labels and entries (grid)
tk.Label(root, text="Item:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Amount:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

add_btn = tk.Button(root, text="Add Expense", command=add_expense)
add_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Text widget and total label (pack)
expenses_text = tk.Text(root, height=10, width=40)
expenses_text.pack(pady=(10, 5))

total_label = tk.Label(root, text="Total Expenses: $0.00", font=("Arial", 12, "bold"))
total_label.pack(pady=(0, 10))

root.mainloop()
