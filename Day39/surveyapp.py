import tkinter as tk
from tkinter import messagebox

def submit_survey():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    color = color_entry.get().strip()
    
    if not name or not age or not color:
        messagebox.showwarning("Incomplete", "Please fill in all fields.")
        return
    
    if not age.isdigit():
        messagebox.showerror("Invalid Input", "Age must be a number.")
        return
    
    summary = f"Name: {name}\nAge: {age}\nFavorite Color: {color}"
    messagebox.showinfo("Survey Summary", summary)
    # Optionally clear inputs
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    color_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Survey App")
root.geometry("300x250")

# Name
tk.Label(root, text="Name:").pack(anchor='w', padx=10, pady=(10,0))
name_entry = tk.Entry(root, width=30)
name_entry.pack(padx=10)

# Age
tk.Label(root, text="Age:").pack(anchor='w', padx=10, pady=(10,0))
age_entry = tk.Entry(root, width=30)
age_entry.pack(padx=10)

# Favorite Color
tk.Label(root, text="Favorite Color:").pack(anchor='w', padx=10, pady=(10,0))
color_entry = tk.Entry(root, width=30)
color_entry.pack(padx=10)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_survey)
submit_btn.pack(pady=20)

root.mainloop()
