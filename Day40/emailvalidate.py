import tkinter as tk
import re

def validate_email():
    email = entry.get().strip()
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        result_label.config(text="Valid Email ✅", fg="green")
    else:
        result_label.config(text="Invalid Email ❌", fg="red")

def clear():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Email Validator")
root.geometry("300x150")

tk.Label(root, text="Enter Email:").pack(pady=(15,5))

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

validate_btn = tk.Button(root, text="Validate", command=validate_email)
validate_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear", command=clear)
clear_btn.pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()

