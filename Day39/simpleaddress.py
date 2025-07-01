import tkinter as tk
from tkinter import messagebox

def display_info():
    name = name_entry.get().strip()
    address = address_entry.get("1.0", tk.END).strip()
    phone = phone_entry.get().strip()
    
    if not name or not address or not phone:
        messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
        return
    
    info = f"Name: {name}\nAddress: {address}\nPhone: {phone}"
    messagebox.showinfo("Entered Information", info)

root = tk.Tk()
root.title("Simple Address Form")
root.geometry("400x350")

tk.Label(root, text="Name:").pack(anchor='w', padx=10, pady=(10,0))
name_entry = tk.Entry(root, width=50)
name_entry.pack(padx=10)

tk.Label(root, text="Address:").pack(anchor='w', padx=10, pady=(10,0))
address_entry = tk.Text(root, width=50, height=5)
address_entry.pack(padx=10)

tk.Label(root, text="Phone:").pack(anchor='w', padx=10, pady=(10,0))
phone_entry = tk.Entry(root, width=50)
phone_entry.pack(padx=10)

submit_btn = tk.Button(root, text="Display Information", command=display_info)
submit_btn.pack(pady=20)

root.mainloop()
