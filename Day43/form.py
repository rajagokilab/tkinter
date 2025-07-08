import tkinter as tk
from tkinter import messagebox

import re

class FormValidationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Form Validation App")
        self.root.geometry("350x220")

        self.create_menu()
        self.create_form()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        form_menu = tk.Menu(menubar, tearoff=0)
        form_menu.add_command(label="Reset", command=self.reset_form)
        form_menu.add_separator()
        form_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Form", menu=form_menu)
        self.root.config(menu=menubar)

    def create_form(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        # Name
        tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(frame, textvariable=self.name_var)
        self.name_entry.grid(row=0, column=1, pady=5)

        # Email
        tk.Label(frame, text="Email:").grid(row=1, column=0, sticky="e", pady=5)
        self.email_var = tk.StringVar()
        self.email_entry = tk.Entry(frame, textvariable=self.email_var)
        self.email_entry.grid(row=1, column=1, pady=5)

        # Phone
        tk.Label(frame, text="Phone:").grid(row=2, column=0, sticky="e", pady=5)
        self.phone_var = tk.StringVar()
        self.phone_entry = tk.Entry(frame, textvariable=self.phone_var)
        self.phone_entry.grid(row=2, column=1, pady=5)

        # Submit Button
        submit_btn = tk.Button(frame, text="Submit", command=self.validate_form)
        submit_btn.grid(row=3, column=0, columnspan=2, pady=15)

    def validate_form(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        phone = self.phone_var.get().strip()

        if not name:
            messagebox.showerror("Validation Error", "Name cannot be empty.")
            return

        # Basic email validation regex
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            messagebox.showerror("Validation Error", "Invalid email format.")
            return

        # Basic phone validation: digits only, length 7-15
        if not phone.isdigit() or not (7 <= len(phone) <= 15):
            messagebox.showerror("Validation Error", "Phone must be 7-15 digits.")
            return

        messagebox.showinfo("Success", "Form submitted successfully!")

    def reset_form(self):
        self.name_var.set("")
        self.email_var.set("")
        self.phone_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = FormValidationApp(root)
    root.mainloop()
