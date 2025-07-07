import tkinter as tk
from tkinter import ttk, messagebox
import re

class TravelBookingApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("✈️ Travel Booking")
        self.geometry("400x350")
        self.resizable(False, False)

        # Name
        ttk.Label(self, text="Name:").pack(anchor="w", padx=20, pady=(20, 0))
        self.name_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.name_var).pack(fill="x", padx=20)

        # Email
        ttk.Label(self, text="Email:").pack(anchor="w", padx=20, pady=(10, 0))
        self.email_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.email_var).pack(fill="x", padx=20)

        # Destination
        ttk.Label(self, text="Destination:").pack(anchor="w", padx=20, pady=(10, 0))
        self.dest_var = tk.StringVar()
        destinations = ["Paris", "New York", "Tokyo", "Sydney", "Rome"]
        self.dest_combo = ttk.Combobox(self, textvariable=self.dest_var, values=destinations, state="readonly")
        self.dest_combo.pack(fill="x", padx=20)
        self.dest_combo.current(0)

        # Number of Travelers
        ttk.Label(self, text="Number of Travelers:").pack(anchor="w", padx=20, pady=(10, 0))
        self.travelers_var = tk.IntVar(value=1)
        self.travelers_spin = ttk.Spinbox(self, from_=1, to=20, textvariable=self.travelers_var)
        self.travelers_spin.pack(fill="x", padx=20)

        # Book Button
        ttk.Button(self, text="Book Now", command=self.book_trip).pack(pady=20)

        # Confirmation Label
        self.confirm_label = ttk.Label(self, text="", font=("Arial", 11), foreground="green", wraplength=360, justify="center")
        self.confirm_label.pack(padx=20)

    def book_trip(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        dest = self.dest_var.get()
        travelers = self.travelers_var.get()

        # Basic validation
        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        if not self.validate_email(email):
            messagebox.showwarning("Input Error", "Please enter a valid email address.")
            return

        # Confirmation message
        msg = (f"Booking Confirmed!\n\n"
               f"Name: {name}\n"
               f"Email: {email}\n"
               f"Destination: {dest}\n"
               f"Travelers: {travelers}")
        self.confirm_label.config(text=msg)

    def validate_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

if __name__ == "__main__":
    TravelBookingApp().mainloop()
