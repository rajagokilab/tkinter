import tkinter as tk
from tkinter import simpledialog, messagebox
import re

class NameDialog(tk.Toplevel):
    def __init__(self, parent, title="Enter Your Name"):
        super().__init__(parent)
        self.title(title)
        self.transient(parent)
        self.grab_set()

        # 49. Center the dialog window using geometry()
        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 150
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 75
        self.geometry(f"300x150+{x}+{y}")

        self.result = None

        tk.Label(self, text="Enter your name:").pack(pady=(15, 5))
        self.entry = tk.Entry(self)
        self.entry.pack(pady=5)
        self.entry.focus()

        # 48. Submit and Cancel buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Submit", command=self.submit).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.cancel).pack(side="left", padx=5)

    def submit(self):
        self.result = self.entry.get()
        self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()


class EmailDialog(tk.Toplevel):
    def __init__(self, parent, title="Enter Email"):
        super().__init__(parent)
        self.title(title)
        self.transient(parent)
        self.grab_set()

        self.result = None

        self.update_idletasks()
        x = parent.winfo_x() + (parent.winfo_width() // 2) - 150
        y = parent.winfo_y() + (parent.winfo_height() // 2) - 75
        self.geometry(f"300x150+{x}+{y}")

        tk.Label(self, text="Enter your email:").pack(pady=(15, 5))
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5)
        self.email_entry.focus()

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Submit", command=self.validate_email).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.cancel).pack(side="left", padx=5)

    def validate_email(self):
        email = self.email_entry.get()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.result = email
            self.destroy()
        else:
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")

    def cancel(self):
        self.result = None
        self.destroy()


# 47. Pass data from dialog back to main window
def open_name_dialog():
    dialog = NameDialog(root)
    root.wait_window(dialog)
    if dialog.result:
        name_label.config(text=f"Name: {dialog.result}")

def open_email_dialog():
    dialog = EmailDialog(root)
    root.wait_window(dialog)
    if dialog.result:
        email_label.config(text=f"Email: {dialog.result}")

# Main Window
root = tk.Tk()
root.title("Custom Dialog Example")
root.geometry("400x250")

tk.Button(root, text="Enter Name", command=open_name_dialog).pack(pady=10)
name_label = tk.Label(root, text="Name: (none)")
name_label.pack()

tk.Button(root, text="Enter Email", command=open_email_dialog).pack(pady=10)
email_label = tk.Label(root, text="Email: (none)")
email_label.pack()

root.mainloop()
