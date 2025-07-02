import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    feedback = feedback_text.get("1.0", tk.END).strip()

    if not name:
        messagebox.showwarning("Validation Error", "Please enter your name.")
        return
    if not email or not validate_email(email):
        messagebox.showwarning("Validation Error", "Please enter a valid email.")
        return
    if not feedback:
        messagebox.showwarning("Validation Error", "Please enter your feedback.")
        return

    with open("feedback.txt", "a") as f:
        f.write(f"Name: {name}\nEmail: {email}\nFeedback:\n{feedback}\n{'-'*40}\n")

    messagebox.showinfo("Thank You", "Thank you for your feedback!")
    # Clear inputs
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Feedback Collector")

# Labels and inputs
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(root, width=40)
email_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Feedback:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
feedback_text = tk.Text(root, width=40, height=10)
feedback_text.grid(row=2, column=1, padx=5, pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit_feedback)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
