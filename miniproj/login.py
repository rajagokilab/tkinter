import tkinter as tk

# Hardcoded credentials
VALID_USERNAME = "user123"
VALID_PASSWORD = "pass123"

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        show_welcome_screen()
    else:
        message_label.config(text="Invalid username or password", fg="red")

def show_welcome_screen():
    # Clear login widgets
    for widget in root.winfo_children():
        widget.destroy()

    # Update window title and size
    root.title("Welcome Screen")
    root.geometry("300x150")

    # Show welcome message centered
    welcome_label = tk.Label(root, text=f"Welcome, {VALID_USERNAME}!", font=("Arial", 16))
    welcome_label.place(relx=0.5, rely=0.5, anchor="center")

# Main window setup
root = tk.Tk()
root.title("Login")
root.geometry("300x150")

# Username Label and Entry
username_label = tk.Label(root, text="Username:")
username_label.place(relx=0.2, rely=0.3, anchor="e")
username_entry = tk.Entry(root, width=20)
username_entry.place(relx=0.25, rely=0.3, anchor="w")

# Password Label and Entry (masked)
password_label = tk.Label(root, text="Password:")
password_label.place(relx=0.2, rely=0.5, anchor="e")
password_entry = tk.Entry(root, width=20, show="*")
password_entry.place(relx=0.25, rely=0.5, anchor="w")

# Login Button
login_button = tk.Button(root, text="Login", command=validate_login)
login_button.place(relx=0.5, rely=0.7, anchor="center")

# Message label for feedback
message_label = tk.Label(root, text="", fg="red")
message_label.place(relx=0.5, rely=0.85, anchor="center")

root.mainloop()
