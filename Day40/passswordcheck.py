import tkinter as tk
import re

def check_strength(event=None):
    pwd = entry.get()
    strength = 0

    # Check conditions
    if re.search(r'[A-Z]', pwd):
        strength += 1
    if re.search(r'[a-z]', pwd):
        strength += 1
    if re.search(r'[0-9]', pwd):
        strength += 1
    if re.search(r'[\W_]', pwd):  # special char (non-alphanumeric)
        strength += 1
    if len(pwd) >= 8:
        strength += 1

    # Determine feedback message and color
    if len(pwd) == 0:
        msg = ""
        color = "black"
    elif strength <= 2:
        msg = "Weak"
        color = "red"
    elif strength == 3 or strength == 4:
        msg = "Medium"
        color = "orange"
    else:
        msg = "Strong"
        color = "green"

    feedback_label.config(text=f"Strength: {msg}", fg=color)

root = tk.Tk()
root.title("Password Strength Checker")

tk.Label(root, text="Enter Password:").pack(pady=5)
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)
entry.bind("<KeyRelease>", check_strength)

feedback_label = tk.Label(root, text="", font=("Arial", 14))
feedback_label.pack(pady=10)

root.mainloop()
