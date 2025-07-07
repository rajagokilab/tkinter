import tkinter as tk
from tkinter import ttk
import re

class EmailValidatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📧 Email Validator")
        self.geometry("350x180")
        self.resizable(False, False)

        # -------- Email input --------
        ttk.Label(self, text="Enter your email:", font=("Arial", 11)).pack(pady=(20, 5))

        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.pack(pady=5)
        self.email_entry.focus()

        # -------- Validate button --------
        ttk.Button(self, text="Validate ✅", command=self.validate_email).pack(pady=10)

        # -------- Result label --------
        self.result_label = tk.Label(self, text="", font=("Arial", 11))
        self.result_label.pack()

    def validate_email(self):
        email = self.email_var.get().strip()
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"

        if re.match(pattern, email):
            self.result_label.config(text="✔ Valid Email", fg="green")
        else:
            self.result_label.config(text="✖ Invalid Email", fg="red")

if __name__ == "__main__":
    EmailValidatorApp().mainloop()
