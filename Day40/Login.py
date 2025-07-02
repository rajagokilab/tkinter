import tkinter as tk
from tkinter import messagebox
import re
import os

# Regex for email validation
EMAIL_REGEX = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

DATA_FILE = "users.txt"

def validate_email(email):
    return re.match(EMAIL_REGEX, email.lower())

def load_users():
    users = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    username, email, password = line.split(",")
                    users[username] = {"email": email, "password": password}
    return users

def save_user(username, email, password):
    with open(DATA_FILE, "a") as f:
        f.write(f"{username},{email},{password}\n")

def register():
    username = entry_username.get().strip()
    email = entry_email.get().strip()
    password = entry_password.get().strip()

    if not username or not email or not password:
        label_reg_msg.config(text="All fields are required.", fg="red")
        return

    if not validate_email(email):
        label_reg_msg.config(text="Invalid email format.", fg="red")
        return

    if username in users:
        label_reg_msg.config(text="Username already exists.", fg="red")
        return

    users[username] = {"email": email, "password": password}
    save_user(username, email, password)
    label_reg_msg.config(text="Registration successful!", fg="green")
    # Clear fields
    entry_username.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_password.delete(0, tk.END)

def login():
    username = entry_login_username.get().strip()
    password = entry_login_password.get().strip()

    if username in users and users[username]["password"] == password:
        label_login_msg.config(text="Login Success!", fg="green")
    else:
        label_login_msg.config(text="Login Failed!", fg="red")

root = tk.Tk()
root.title("Login and Registration System")
root.geometry("350x350")

users = load_users()

# Registration frame
frame_reg = tk.LabelFrame(root, text="Register", padx=10, pady=10)
frame_reg.pack(padx=10, pady=10, fill="x")

tk.Label(frame_reg, text="Username").grid(row=0, column=0, sticky="w")
entry_username = tk.Entry(frame_reg)
entry_username.grid(row=0, column=1)

tk.Label(frame_reg, text="Email").grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(frame_reg)
entry_email.grid(row=1, column=1)

tk.Label(frame_reg, text="Password").grid(row=2, column=0, sticky="w")
entry_password = tk.Entry(frame_reg, show="*")
entry_password.grid(row=2, column=1)

btn_register = tk.Button(frame_reg, text="Register", command=register)
btn_register.grid(row=3, columnspan=2, pady=5)

label_reg_msg = tk.Label(frame_reg, text="")
label_reg_msg.grid(row=4, columnspan=2)

# Login frame
frame_login = tk.LabelFrame(root, text="Login", padx=10, pady=10)
frame_login.pack(padx=10, pady=10, fill="x")

tk.Label(frame_login, text="Username").grid(row=0, column=0, sticky="w")
entry_login_username = tk.Entry(frame_login)
entry_login_username.grid(row=0, column=1)

tk.Label(frame_login, text="Password").grid(row=1, column=0, sticky="w")
entry_login_password = tk.Entry(frame_login, show="*")
entry_login_password.grid(row=1, column=1)

btn_login = tk.Button(frame_login, text="Login", command=login)
btn_login.grid(row=2, columnspan=2, pady=5)

label_login_msg = tk.Label(frame_login, text="")
label_login_msg.grid(row=3, columnspan=2)

root.mainloop()
