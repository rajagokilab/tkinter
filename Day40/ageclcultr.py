import tkinter as tk
import re
from datetime import datetime, date

def calculate_age():
    dob_str = dob_entry.get()
    # Regex for YYYY-MM-DD format
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", dob_str):
        result_label.config(text="Invalid format! Use YYYY-MM-DD")
        return

    try:
        dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
    except ValueError:
        result_label.config(text="Invalid date! Check the values.")
        return

    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    if age < 0:
        result_label.config(text="Date is in the future!")
        return

    result_label.config(text=f"Your age is: {age} years")

root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x150")

tk.Label(root, text="Enter Date of Birth (YYYY-MM-DD):").pack(pady=5)
dob_entry = tk.Entry(root)
dob_entry.pack(pady=5)

calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
