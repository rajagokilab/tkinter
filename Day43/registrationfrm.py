import tkinter as tk
from tkinter import ttk

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Section Registration Form")
        self.root.geometry("500x500")

        # Personal Info Frame
        personal_frame = tk.LabelFrame(root, text="Personal Info", padx=10, pady=10)
        personal_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(personal_frame, text="First Name:").grid(row=0, column=0, sticky="e")
        self.first_name = tk.Entry(personal_frame)
        self.first_name.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(personal_frame, text="Last Name:").grid(row=1, column=0, sticky="e")
        self.last_name = tk.Entry(personal_frame)
        self.last_name.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(personal_frame, text="Age:").grid(row=2, column=0, sticky="e")
        self.age = tk.Spinbox(personal_frame, from_=1, to=120)
        self.age.grid(row=2, column=1, padx=5, pady=2)

        # Contact Info Frame
        contact_frame = tk.LabelFrame(root, text="Contact Info", padx=10, pady=10)
        contact_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(contact_frame, text="Email:").grid(row=0, column=0, sticky="e")
        self.email = tk.Entry(contact_frame)
        self.email.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(contact_frame, text="Phone:").grid(row=1, column=0, sticky="e")
        self.phone = tk.Entry(contact_frame)
        self.phone.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(contact_frame, text="Country:").grid(row=2, column=0, sticky="e")
        self.country = ttk.Combobox(contact_frame, values=["USA", "Canada", "UK", "India", "Other"])
        self.country.grid(row=2, column=1, padx=5, pady=2)
        self.country.set("USA")

        # Account Info Frame
        account_frame = tk.LabelFrame(root, text="Account Info", padx=10, pady=10)
        account_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(account_frame, text="Username:").grid(row=0, column=0, sticky="e")
        self.username = tk.Entry(account_frame)
        self.username.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(account_frame, text="Password:").grid(row=1, column=0, sticky="e")
        self.password = tk.Entry(account_frame, show="*")
        self.password.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(account_frame, text="Account Type:").grid(row=2, column=0, sticky="e")
        self.account_type = ttk.Combobox(account_frame, values=["Standard", "Premium", "Admin"])
        self.account_type.grid(row=2, column=1, padx=5, pady=2)
        self.account_type.set("Standard")

        # Submit Button
        submit_btn = tk.Button(root, text="Submit", command=self.show_summary)
        submit_btn.pack(pady=10)

    def show_summary(self):
        summary_window = tk.Toplevel(self.root)
        summary_window.title("Submitted Info")
        summary_window.geometry("400x300")
        summary_window.grab_set()

        tk.Label(summary_window, text="Submitted Information", font=("Arial", 14, "bold")).pack(pady=10)

        info = [
            ("First Name", self.first_name.get()),
            ("Last Name", self.last_name.get()),
            ("Age", self.age.get()),
            ("Email", self.email.get()),
            ("Phone", self.phone.get()),
            ("Country", self.country.get()),
            ("Username", self.username.get()),
            ("Account Type", self.account_type.get())
        ]

        for label, value in info:
            tk.Label(summary_window, text=f"{label}: {value}", anchor="w").pack(fill="x", padx=20, pady=2)

# Run the form
if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
