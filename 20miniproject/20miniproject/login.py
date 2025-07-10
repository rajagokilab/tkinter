import tkinter as tk
from tkinter import messagebox

# Hardcoded credentials
USERNAME = "admin"
PASSWORD = "pass123"

def validate_login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if entered_username == USERNAME and entered_password == PASSWORD:
        open_welcome_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def open_welcome_window():
    # Hide login window
    root.withdraw()

    # Create new window
    welcome_win = tk.Toplevel()
    welcome_win.title("Welcome Screen")
    welcome_win.geometry("400x200")

    tk.Label(welcome_win, text=f"Welcome, {USERNAME}!", font=("Arial", 18)).pack(pady=60)

# Main Login Window
root = tk.Tk()
root.title("Login")
root.geometry("350x200")

# Login Frame (centered using place)
login_frame = tk.Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(login_frame, text="Username:").grid(row=0, column=0, pady=5, sticky="e")
username_entry = tk.Entry(login_frame, width=25)
username_entry.grid(row=0, column=1, pady=5)

tk.Label(login_frame, text="Password:").grid(row=1, column=0, pady=5, sticky="e")
password_entry = tk.Entry(login_frame, show="*", width=25)
password_entry.grid(row=1, column=1, pady=5)

login_button = tk.Button(login_frame, text="Login", command=validate_login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
