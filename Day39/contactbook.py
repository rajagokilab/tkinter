import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    if not name or not phone:
        messagebox.showwarning("Input Error", "Please enter both name and phone number.")
        return
    contacts.append((name, phone))
    update_contacts_display()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def update_contacts_display():
    contacts_text.delete("1.0", tk.END)
    for i, (name, phone) in enumerate(contacts, start=1):
        contacts_text.insert(tk.END, f"{i}. {name} - {phone}\n")

root = tk.Tk()
root.title("Contact Book")
root.geometry("350x400")

tk.Label(root, text="Name:").pack(anchor='w', padx=10, pady=(10,0))
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=10)

tk.Label(root, text="Phone:").pack(anchor='w', padx=10, pady=(10,0))
phone_entry = tk.Entry(root, width=40)
phone_entry.pack(padx=10)

add_btn = tk.Button(root, text="Add Contact", command=add_contact)
add_btn.pack(pady=10)

contacts_text = tk.Text(root, width=40, height=15)
contacts_text.pack(padx=10)

root.mainloop()
