import tkinter as tk
from tkinter import messagebox
import re

def validate_and_display():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    age = age_spinbox.get()
    about = about_text.get("1.0", tk.END).strip()

    # Email validation using regex
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    result = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAge: {age}\nAbout: {about}"
    result_label.config(text=result)

# Main Window
root = tk.Tk()
root.title("Personal Information Form")
root.geometry("500x500")
root.configure(padx=20, pady=20)

# === Personal Info Frame ===
info_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
info_frame.grid(row=0, column=0, sticky="ew")

tk.Label(info_frame, text="Name:").grid(row=0, column=0, sticky="e", pady=5)
name_entry = tk.Entry(info_frame, width=30)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(info_frame, text="Email:").grid(row=1, column=0, sticky="e", pady=5)
email_entry = tk.Entry(info_frame, width=30)
email_entry.grid(row=1, column=1, pady=5)

tk.Label(info_frame, text="Phone:").grid(row=2, column=0, sticky="e", pady=5)
phone_entry = tk.Entry(info_frame, width=30)
phone_entry.grid(row=2, column=1, pady=5)

tk.Label(info_frame, text="Age:").grid(row=3, column=0, sticky="e", pady=5)
age_spinbox = tk.Spinbox(info_frame, from_=10, to=100, width=5)
age_spinbox.grid(row=3, column=1, sticky="w", pady=5)

# === About Frame ===
about_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
about_frame.grid(row=1, column=0, sticky="ew", pady=10)

tk.Label(about_frame, text="About You:").grid(row=0, column=0, sticky="nw")
about_text = tk.Text(about_frame, width=40, height=5)
about_text.grid(row=1, column=0, padx=5)

# === Submit and Display ===
submit_button = tk.Button(root, text="Submit", command=validate_and_display)
submit_button.grid(row=2, column=0, pady=10)

result_label = tk.Label(root, text="", justify="left", anchor="w")
result_label.grid(row=3, column=0, sticky="w")

root.mainloop()
