import tkinter as tk
from tkinter import ttk, messagebox
import re

# Validation and Registration Function
def register_student():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    course = course_combobox.get()
    age = age_spinbox.get()

    # Email Validation
    if not name or not email or not course:
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address.")
        return

    student_info = f"{name} | {email} | {course} | Age: {age}"
    student_listbox.insert(tk.END, student_info)

    # Clear fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    course_combobox.set('')
    age_spinbox.delete(0, tk.END)
    age_spinbox.insert(0, '18')

# Main Window
root = tk.Tk()
root.title("Student Registration App")
root.geometry("500x450")
root.configure(padx=20, pady=20)

# === Input Frame ===
input_frame = tk.Frame(root)
input_frame.pack(pady=10, fill='x')

# Name
tk.Label(input_frame, text="Name:").pack(anchor="w")
name_entry = tk.Entry(input_frame, width=40)
name_entry.pack()

# Email
tk.Label(input_frame, text="Email:").pack(anchor="w", pady=(10, 0))
email_entry = tk.Entry(input_frame, width=40)
email_entry.pack()

# Course
tk.Label(input_frame, text="Course:").pack(anchor="w", pady=(10, 0))
course_combobox = ttk.Combobox(input_frame, values=["Python", "Java", "Web Dev", "Data Science"], state="readonly")
course_combobox.pack()

# Age
tk.Label(input_frame, text="Age:").pack(anchor="w", pady=(10, 0))
age_spinbox = tk.Spinbox(input_frame, from_=10, to=100, width=5)
age_spinbox.pack()

# Submit Button
submit_button = tk.Button(root, text="Register Student", command=register_student)
submit_button.pack(pady=10)

# === Student List Frame ===
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill="both", expand=True)

# Scrollbar and Listbox
scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

student_listbox = tk.Listbox(list_frame, width=60, yscrollcommand=scrollbar.set)
student_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=student_listbox.yview)

root.mainloop()
