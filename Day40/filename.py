import tkinter as tk
from tkinter import messagebox
import re

def generate_filename():
    project = project_entry.get().strip()
    date = date_entry.get().strip()
    file_type = type_entry.get().strip()

    # Basic validation for date format YYYY-MM-DD
    if not project or not date or not file_type:
        messagebox.showwarning("Input Error", "All fields are required.")
        return
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        messagebox.showwarning("Input Error", "Date must be in YYYY-MM-DD format.")
        return

    filename = f"{project}_{date}_{file_type}.txt"
    result_label.config(text=filename)

    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(filename)
    messagebox.showinfo("Copied", f"Filename '{filename}' copied to clipboard!")

root = tk.Tk()
root.title("File Name Generator")

tk.Label(root, text="Project Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
project_entry = tk.Entry(root)
project_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
date_entry = tk.Entry(root)
date_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Type:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
type_entry = tk.Entry(root)
type_entry.grid(row=2, column=1, padx=5, pady=5)

generate_btn = tk.Button(root, text="Generate Filename", command=generate_filename)
generate_btn.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", fg="blue", font=("Arial", 12, "bold"))
result_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
