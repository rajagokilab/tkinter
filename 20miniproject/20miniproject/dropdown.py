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
        "Address": "456 Oak Avenue, Rivertown"
    },
    "Carol Davis": {
        "Contact": "carol.d@example.com",
        "Address": "789 Pine Road, Lakeview"
    }
}

def show_details(event=None):
    selected = customer_combo.get()
    if selected in customers:
        info = customers[selected]
        contact_label.config(text=f"Contact: {info['Contact']}")
        address_label.config(text=f"Address: {info['Address']}")
        # Disable Combobox after selection (optional)
        # customer_combo.config(state="disabled")

# Main window
root = tk.Tk()
root.title("Customer Drop-down Selector")
root.geometry("400x200")
root.configure(padx=15, pady=15)

tk.Label(root, text="Select Customer:").pack(anchor="w")

customer_combo = ttk.Combobox(root, values=list(customers.keys()), state="readonly")
customer_combo.pack(fill=tk.X, pady=5)
customer_combo.bind("<<ComboboxSelected>>", show_details)

contact_label = tk.Label(root, text="Contact: ")
contact_label.pack(anchor="w", pady=(20, 0))

address_label = tk.Label(root, text="Address: ")
address_label.pack(anchor="w")

root.mainloop()
