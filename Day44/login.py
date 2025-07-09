import tkinter as tk

def update_button_state(event=None):
    # Get the current text in both entries
    user = username_entry.get().strip()
    pwd = password_entry.get().strip()

    # Enable button only if both fields are non-empty
    if user and pwd:
        login_btn.config(state="normal")
    else:
        login_btn.config(state="disabled")

# Setup the window
root = tk.Tk()
root.title("Login Form with Dynamic Button State")
root.geometry("300x180")

# Username Entry
tk.Label(root, text="Username:").pack(pady=(10, 0))
username_entry = tk.Entry(root)
username_entry.pack()
username_entry.bind("<KeyRelease>", update_button_state)

# Password Entry
tk.Label(root, text="Password:").pack(pady=(10, 0))
password_entry = tk.Entry(root, show="*")
password_entry.pack()
password_entry.bind("<KeyRelease>", update_button_state)

# Login Button (initially disabled)
login_btn = tk.Button(root, text="Login", state="disabled", command=lambda: print("Logged in!"))
login_btn.pack(pady=20)

root.mainloop()
