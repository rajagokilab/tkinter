import tkinter as tk
from tkinter import messagebox
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def submit():
    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()
    course = entry_course.get().strip()

    # Validation
    if not name:
        messagebox.showerror("Validation Error", "Name cannot be empty.")
        return
    if not age.isdigit() or int(age) <= 0:
        messagebox.showerror("Validation Error", "Age must be a positive integer.")
        return
    if not validate_email(email):
        messagebox.showerror("Validation Error", "Invalid email format.")
        return
    if not course:
        messagebox.showerror("Validation Error", "Course cannot be empty.")
        return

    # Save to file
    with open("students.txt", "a") as f:
        f.write(f"Name: {name}, Age: {age}, Email: {email}, Course: {course}\n")

    # Show summary
    summary = f"Student Registered Successfully:\n\nName: {name}\nAge: {age}\nEmail: {email}\nCourse: {course}"
    messagebox.showinfo("Success", summary)

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_course.delete(0, tk.END)

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x250")

# Labels and entries
tk.Label(root, text="Name:").grid(row=0, column=0, sticky='e', padx=10, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_age = tk.Entry(root, width=30)
entry_age.grid(row=1, column=1, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.grid(row=2, column=1, pady=5)

tk.Label(root, text="Course:").grid(row=3, column=0, sticky='e', padx=10, pady=5)
entry_course = tk.Entry(root, width=30)
entry_course.grid(row=3, column=1, pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.grid(row=4, column=0, columnspan=2, pady=15)

root.mainloop()
