import tkinter as tk
import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def validate_email(event=None):
    email = email_entry.get()
    if EMAIL_REGEX.fullmatch(email):
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

root = tk.Tk()
root.title("Real-Time Email Validator")
root.geometry("350x150")

tk.Label(root, text="Enter your email:").pack(pady=(20,5))

email_entry = tk.Entry(root, width=30)
email_entry.pack()
email_entry.bind("<KeyRelease>", validate_email)

submit_btn = tk.Button(root, text="Submit", state="disabled", command=lambda: print("Submitted:", email_entry.get()))
submit_btn.pack(pady=20)

root.mainloop()
