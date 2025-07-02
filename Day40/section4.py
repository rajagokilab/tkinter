import tkinter as tk
from tkinter import messagebox
import re

def task1():
    # Form with name, email entries and submit button
    def submit():
        name = entry_name.get()
        email = entry_email.get()
        print(f"Name: {name}")
        print(f"Email: {email}")
    root = tk.Tk()
    root.title("Task 1: Simple Form")
    tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
    entry_name = tk.Entry(root)
    entry_email = tk.Entry(root)
    entry_name.grid(row=0, column=1, padx=10, pady=5)
    entry_email.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Submit", command=submit).grid(row=2, column=0, columnspan=2, pady=10)
    root.mainloop()

def task2():
    # Use insert() to prefill name entry
    root = tk.Tk()
    root.title("Task 2: Prefill Entry")
    tk.Label(root, text="Name").pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)
    entry.insert(0, "Enter Name")
    root.mainloop()

def task3():
    # Use delete() to clear Entry on button click
    def clear_entry():
        entry.delete(0, tk.END)
    root = tk.Tk()
    root.title("Task 3: Clear Entry")
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=10)
    tk.Button(root, text="Clear", command=clear_entry).pack(pady=5)
    root.mainloop()

def task4():
    # Validate name field not empty before submit
    def submit():
        name = entry.get()
        if not name.strip():
            messagebox.showwarning("Validation Error", "Name cannot be empty!")
        else:
            messagebox.showinfo("Success", f"Hello, {name}!")
    root = tk.Tk()
    root.title("Task 4: Validate Name")
    tk.Label(root, text="Name").pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)
    tk.Button(root, text="Submit", command=submit).pack(pady=10)
    root.mainloop()

def task5():
    # Validate email format using regex
    def submit():
        email = entry.get()
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            messagebox.showwarning("Invalid Email", "Please enter a valid email address!")
        else:
            messagebox.showinfo("Success", f"Valid Email: {email}")
    root = tk.Tk()
    root.title("Task 5: Email Validation")
    tk.Label(root, text="Email").pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)
    tk.Button(root, text="Submit", command=submit).pack(pady=10)
    root.mainloop()

def task6():
    # Password entry field with show="*"
    root = tk.Tk()
    root.title("Task 6: Password Entry")
    tk.Label(root, text="Password").pack(pady=5)
    entry = tk.Entry(root, show="*")
    entry.pack(padx=10, pady=5)
    root.mainloop()

def task7():
    # Login form with username/password check
    def login():
        user = entry_user.get()
        pwd = entry_pwd.get()
        if user == "admin" and pwd == "1234":
            messagebox.showinfo("Login", "Login Success")
        else:
            messagebox.showerror("Login", "Invalid credentials")
    root = tk.Tk()
    root.title("Task 7: Login Form")
    tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=5)
    entry_user = tk.Entry(root)
    entry_pwd = tk.Entry(root, show="*")
    entry_user.grid(row=0, column=1, padx=10, pady=5)
    entry_pwd.grid(row=1, column=1, padx=10, pady=5)
    tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)
    root.mainloop()

def task8():
    # Display warning if email invalid or empty
    def submit():
        email = entry.get().strip()
        if not email:
            messagebox.showwarning("Warning", "Email cannot be empty!")
        else:
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if not re.match(pattern, email):
                messagebox.showwarning("Warning", "Invalid email format!")
            else:
                messagebox.showinfo("Success", "Email is valid!")
    root = tk.Tk()
    root.title("Task 8: Email Warning")
    tk.Label(root, text="Email").pack(pady=5)
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)
    tk.Button(root, text="Submit", command=submit).pack(pady=10)
    root.mainloop()

def task9():
    # Allow only numeric input using regex validation
    def validate(P):
        # P is the new text in the entry after the edit
        return P == "" or P.isdigit()
    root = tk.Tk()
    root.title("Task 9: Numeric Only Entry")
    tk.Label(root, text="Enter numbers only").pack(pady=5)
    vcmd = (root.register(validate), '%P')
    entry = tk.Entry(root, validate='key', validatecommand=vcmd)
    entry.pack(padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    # Uncomment to run a specific task:
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    task9()
    print("Uncomment a task() call at the bottom to run a demo.")
