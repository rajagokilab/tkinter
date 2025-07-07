import tkinter as tk
from tkinter import ttk, messagebox

class InventoryTracker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📦 Inventory Stock Tracker")
        self.geometry("400x350")
        self.resizable(False, False)

        # Data storage: {item_name: quantity}
        self.stock = {}

        # Item name input
        ttk.Label(self, text="Item Name:").pack(anchor="w", padx=20, pady=(20, 0))
        self.item_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.item_var).pack(fill="x", padx=20)

        # Quantity input
        ttk.Label(self, text="Quantity:").pack(anchor="w", padx=20, pady=(10, 0))
        self.qty_var = tk.IntVar(value=1)
        ttk.Spinbox(self, from_=1, to=1000, textvariable=self.qty_var).pack(fill="x", padx=20)

        # Add button
        ttk.Button(self, text="Add / Update Stock", command=self.add_item).pack(pady=15)

        # Frame for Listbox + scrollbar
        frame = ttk.Frame(self)
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        self.listbox = tk.Listbox(frame, font=("Arial", 12))
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")

        self.listbox.config(yscrollcommand=scrollbar.set)

    def add_item(self):
        item = self.item_var.get().strip()
        qty = self.qty_var.get()

        if not item:
            messagebox.showwarning("Input Error", "Please enter an item name.")
            return
        if qty <= 0:
            messagebox.showwarning("Input Error", "Quantity must be greater than zero.")
            return

        # Update stock
        if item in self.stock:
            self.stock[item] += qty
        else:
            self.stock[item] = qty

        self.refresh_list()
        self.item_var.set("")
        self.qty_var.set(1)

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for item, qty in sorted(self.stock.items()):
            self.listbox.insert(tk.END, f"{item}: {qty}")

if __name__ == "__main__":
    InventoryTracker().mainloop()
