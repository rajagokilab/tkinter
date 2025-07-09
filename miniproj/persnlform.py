import tkinter as tk
from tkinter import Frame, Label, Entry, Spinbox, Button, Text, END
import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def submit_data():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    age = age_spinbox.get()
    about = about_text.get("1.0", END).strip()

    if not validate_email(email):
        result_label.config(text="Invalid email format!", fg="red")
        return

    output = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAge: {age}\nAbout: {about}"
    result_label.config(text=output, fg="green")

# Main Window
root = tk.Tk()
root.title("Personal Information Form")
root.geometry("400x500")

# Personal Info Frame
info_frame = Frame(root)
info_frame.grid(row=0, column=0, padx=10, pady=10, sticky="w")

Label(info_frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = Entry(info_frame, width=30)
name_entry.grid(row=0, column=1)

Label(info_frame, text="Email:").grid(row=1, column=0, sticky="w")
email_entry = Entry(info_frame, width=30)
email_entry.grid(row=1, column=1)

Label(info_frame, text="Phone:").grid(row=2, column=0, sticky="w")
phone_entry = Entry(info_frame, width=30)
phone_entry.grid(row=2, column=1)

Label(info_frame, text="Age:").grid(row=3, column=0, sticky="w")
age_spinbox = Spinbox(info_frame, from_=10, to=100, width=5)
age_spinbox.grid(row=3, column=1, sticky="w")

# About You Frame
about_frame = Frame(root)
about_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

Label(about_frame, text="About You:").grid(row=0, column=0, sticky="w")
about_text = Text(about_frame, width=40, height=5)
about_text.grid(row=1, column=0)

# Submit Button
submit_button = Button(root, text="Submit", command=submit_data)
submit_button.grid(row=2, column=0, pady=10)

# Result Label
result_label = Label(root, text="", justify="left", fg="green")
result_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

root.mainloop()
