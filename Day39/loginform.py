import tkinter as tk
from tkinter import messagebox
import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    # Preset username and password
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", f"Welcome, {username}!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

root = tk.Tk()
root.title("Simple Login Form")
root.geometry("300x150")

# Username label and entry
tk.Label(root, text="Username:").pack(pady=(10,0))
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
tk.Label(root, text="Password:").pack(pady=(10,0))
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
login_btn = tk.Button(root, text="Login", command=login)
login_btn.pack(pady=10)

root.mainloop()
