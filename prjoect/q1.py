import re
import tkinter as tk
from tkinter import ttk, messagebox

EMAIL_PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$")

class AuthApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Registration & Login")
        self.resizable(False, False)

        # In‑memory user store: {username: (email, password)}
        self.users = {}

        # ---------- GUI ----------
        self.frm = ttk.Frame(self, padding=20)   # main frame
        self.frm.grid(column=0, row=0)

        ttk.Label(self.frm, text="Username").grid(column=0, row=0, sticky="w")
        ttk.Label(self.frm, text="E‑mail").grid(column=0, row=1, sticky="w")
        ttk.Label(self.frm, text="Password").grid(column=0, row=2, sticky="w")

        self.username_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.password_var = tk.StringVar()

        ttk.Entry(self.frm, textvariable=self.username_var).grid(column=1, row=0, padx=5, pady=4)
        ttk.Entry(self.frm, textvariable=self.email_var).grid(column=1, row=1, padx=5, pady=4)
        ttk.Entry(self.frm, textvariable=self.password_var, show="*").grid(column=1, row=2, padx=5, pady=4)

        self.mode = tk.StringVar(value="register")  # register ⬅► login
        ttk.Radiobutton(self.frm, text="Register", value="register", variable=self.mode).grid(column=0, row=3, pady=(10,0))
        ttk.Radiobutton(self.frm, text="Login",    value="login",    variable=self.mode).grid(column=1, row=3, pady=(10,0))

        ttk.Button(self.frm, text="Submit", command=self.submit).grid(column=0, row=4, columnspan=2, pady=10)

        self.status_lbl = ttk.Label(self.frm, text="", foreground="darkgreen")
        self.status_lbl.grid(column=0, row=5, columnspan=2)

    # ---------- Logic ----------
    def submit(self):
        user = self.username_var.get().strip()
        email = self.email_var.get().strip()
        pwd  = self.password_var.get()

        if not user or not email or not pwd:
            self.update_status("All fields are required.", error=True)
            return

        if not EMAIL_PATTERN.match(email):
            self.update_status("Invalid e‑mail format.", error=True)
            return

        if self.mode.get() == "register":
            self.register(user, email, pwd)
        else:
            self.login(user, email, pwd)

    def register(self, user, email, pwd):
        if user in self.users:
            self.update_status("Username already exists. Choose another.", error=True)
            return
        self.users[user] = (email, pwd)
        self.clear_fields()
        self.update_status("Registration successful! You can now log in.")

    def login(self, user, email, pwd):
        if user not in self.users:
            self.update_status("User not found. Please register first.", error=True)
            return
        stored_email, stored_pwd = self.users[user]
        if email != stored_email or pwd != stored_pwd:
            self.update_status("Incorrect e‑mail or password.", error=True)
            return
        self.clear_fields()
        self.update_status(f"Welcome back, {user}!", error=False)
        messagebox.showinfo("Login", "Login successful 🎉")

    # helpers
    def update_status(self, msg, error=False):
        self.status_lbl.configure(text=msg, foreground=("red" if error else "darkgreen"))

    def clear_fields(self):
        self.username_var.set("")
        self.email_var.set("")
        self.password_var.set("")

if __name__ == "__main__":
    AuthApp().mainloop()
