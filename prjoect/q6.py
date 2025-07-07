import tkinter as tk
from tkinter import ttk, messagebox
import re

class EnrollmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Course Enrollment")
        self.geometry("500x400")
        self.resizable(False, False)

        # ---------- Input Frame ----------
        form = ttk.LabelFrame(self, text="Student Info", padding=10)
        form.pack(padx=10, pady=10, fill="x")

        # Name
        ttk.Label(form, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.name_var, width=30).grid(row=0, column=1, pady=5)

        # Email
        ttk.Label(form, text="Email:").grid(row=1, column=0, sticky="w")
        self.email_var = tk.StringVar()
        ttk.Entry(form, textvariable=self.email_var, width=30).grid(row=1, column=1, pady=5)

        # Age
        ttk.Label(form, text="Age:").grid(row=2, column=0, sticky="w")
        self.age_var = tk.IntVar(value=18)
        tk.Spinbox(form, from_=15, to=100, textvariable=self.age_var, width=5).grid(row=2, column=1, sticky="w", pady=5)

        # Course selection
        ttk.Label(form, text="Course:").grid(row=3, column=0, sticky="w")
        self.course_var = tk.StringVar()
        courses = ["Python Basics", "Data Science", "Web Development", "AI & ML", "Cybersecurity"]
        ttk.Combobox(form, textvariable=self.course_var, values=courses, state="readonly").grid(row=3, column=1, pady=5)

        # Submit button
        ttk.Button(form, text="Enroll Student", command=self.enroll_student).grid(row=4, column=0, columnspan=2, pady=10)

        # ---------- Display Frame ----------
        display = ttk.LabelFrame(self, text="Enrolled Students", padding=10)
        display.pack(padx=10, pady=5, fill="both", expand=True)

        self.listbox = tk.Listbox(display, height=10)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(display, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

    def enroll_student(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        age = self.age_var.get()
        course = self.course_var.get()

        # Basic validation
        if not name or not email or not course:
            messagebox.showwarning("Missing Info", "Please fill all the fields.")
            return
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        # Add to listbox
        entry = f"{name} ({age}) - {course} [{email}]"
        self.listbox.insert(tk.END, entry)

        # Clear fields
        self.name_var.set("")
        self.email_var.set("")
        self.age_var.set(18)
        self.course_var.set("")

if __name__ == "__main__":
    EnrollmentApp().mainloop()
