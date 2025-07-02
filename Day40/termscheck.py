import tkinter as tk
from tkinter import messagebox

def toggle_submit():
    if terms_var.get():
        submit_btn.config(state="normal")
    else:
        submit_btn.config(state="disabled")

def submit():
    name = name_entry.get()
    email = email_entry.get()
    if not name or not email:
        messagebox.showwarning("Input Error", "Please fill all fields.")
        return
    messagebox.showinfo("Success", "Form submitted successfully!")

root = tk.Tk()
root.title("Terms and Conditions Form")

# Labels and Entries
tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Terms Checkbutton
terms_var = tk.BooleanVar()
terms_check = tk.Checkbutton(root, text="I agree to the Terms and Conditions", variable=terms_var, command=toggle_submit)
terms_check.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Submit Button
submit_btn = tk.Button(root, text="Submit", state="disabled", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
