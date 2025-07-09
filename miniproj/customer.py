import tkinter as tk
from tkinter import ttk

# Sample customer data
customers = {
    "Alice Johnson": {
        "Contact": "alice.j@example.com",
        "Address": "123 Maple Street, Springfield"
    },
    "Bob Smith": {
        "Contact": "bob.smith@example.com",
        "Address": "456 Oak Avenue, Shelbyville"
    },
    "Carol Davis": {
        "Contact": "carol.d@example.com",
        "Address": "789 Pine Road, Capital City"
    }
}

def on_customer_select(event):
    selected = combo_customer.get()
    if selected in customers:
        info = customers[selected]
        label_name.config(text=f"Name: {selected}")
        label_contact.config(text=f"Contact: {info['Contact']}")
        label_address.config(text=f"Address: {info['Address']}")
        # Uncomment below line to disable combobox after selection
        # combo_customer.config(state="disabled")
    else:
        label_name.config(text="Name:")
        label_contact.config(text="Contact:")
        label_address.config(text="Address:")

root = tk.Tk()
root.title("Customer Drop-down Selector")

tk.Label(root, text="Select Customer:").pack(pady=5)

combo_customer = ttk.Combobox(root, values=list(customers.keys()), state="readonly", width=30)
combo_customer.pack(pady=5)
combo_customer.bind("<<ComboboxSelected>>", on_customer_select)

label_name = tk.Label(root, text="Name:")
label_name.pack(pady=2)

label_contact = tk.Label(root, text="Contact:")
label_contact.pack(pady=2)

label_address = tk.Label(root, text="Address:")
label_address.pack(pady=2)

root.mainloop()
