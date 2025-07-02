import tkinter as tk
import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

def submit_form():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    message = text_message.get("1.0", "end").strip()
    
    error_msg = ""
    if not name:
        error_msg += "Name cannot be empty.\n"
    if not email or not validate_email(email):
        error_msg += "Invalid email address.\n"
    if len(message) < 10:
        error_msg += "Message must be at least 10 characters long.\n"
    
    if error_msg:
        label_error.config(text=error_msg, fg="red")
        label_thankyou.config(text="")
    else:
        label_error.config(text="")
        label_thankyou.config(text="Thank you for your message!", fg="green")
        # Clear fields after submission (optional)
        entry_name.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        text_message.delete("1.0", tk.END)

root = tk.Tk()
root.title("Contact Form")

# Name
tk.Label(root, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name = tk.Entry(root, width=40)
entry_name.grid(row=0, column=1, padx=5, pady=5)

# Email
tk.Label(root, text="Email:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_email = tk.Entry(root, width=40)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# Message
tk.Label(root, text="Message:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
text_message = tk.Text(root, width=40, height=8)
text_message.grid(row=2, column=1, padx=5, pady=5)

# Error Label
label_error = tk.Label(root, text="", fg="red")
label_error.grid(row=3, column=0, columnspan=2)

# Thank You Label
label_thankyou = tk.Label(root, text="", fg="green")
label_thankyou.grid(row=4, column=0, columnspan=2)

# Submit Button
btn_submit = tk.Button(root, text="Submit", command=submit_form)
btn_submit.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
