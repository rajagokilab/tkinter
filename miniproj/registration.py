import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Listbox, Scrollbar, Spinbox, ttk, END
import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def submit_student():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    course = course_combobox.get()
    age = age_spinbox.get()

    if not name:
        status_label.config(text="Name is required!", fg="red")
        return
    if not validate_email(email):
        status_label.config(text="Invalid email format!", fg="red")
        return
    if course == "":
        status_label.config(text="Please select a course!", fg="red")
        return

    student_info = f"{name}, {email}, {course}, Age: {age}"
    student_listbox.insert(END, student_info)

    # Clear inputs
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    course_combobox.set('')
    age_spinbox.delete(0, END)
    age_spinbox.insert(0, '18')

    status_label.config(text="Student registered successfully!", fg="green")

# Main window
root = tk.Tk()
root.title("Student Registration App")
root.geometry("450x400")

# Top frame for inputs
input_frame = Frame(root)
input_frame.pack(pady=10)

# Name
Label(input_frame, text="Name:").pack(anchor="w")
name_entry = Entry(input_frame, width=40)
name_entry.pack()

# Email
Label(input_frame, text="Email:").pack(anchor="w")
email_entry = Entry(input_frame, width=40)
email_entry.pack()

# Course Combobox
Label(input_frame, text="Course:").pack(anchor="w")
course_combobox = ttk.Combobox(input_frame, values=["Math", "Science", "History", "Art", "Computer Science"], state="readonly")
course_combobox.pack()

# Age Spinbox
Label(input_frame, text="Age:").pack(anchor="w")
age_spinbox = Spinbox(input_frame, from_=10, to=100, width=5)
age_spinbox.pack()
age_spinbox.delete(0, END)
age_spinbox.insert(0, '18')

# Submit Button
submit_button = Button(root, text="Register Student", command=submit_student)
submit_button.pack(pady=10)

# Frame for Listbox + Scrollbar
list_frame = Frame(root)
list_frame.pack(fill="both", expand=True, padx=10, pady=10)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

student_listbox = Listbox(list_frame, yscrollcommand=scrollbar.set)
student_listbox.pack(side="left", fill="both", expand=True)

scrollbar.config(command=student_listbox.yview)

# Status label
status_label = Label(root, text="", fg="green")
status_label.pack()

root.mainloop()
