import tkinter as tk
from tkinter import ttk, messagebox

class ProductOrderForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🛒 Product Order Form")
        self.geometry("400x400")
        self.resizable(False, False)

        # -------- Product Selection Frame --------
        form_frame = ttk.LabelFrame(self, text="Place Your Order", padding=10)
        form_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(form_frame, text="Select Product:").grid(row=0, column=0, sticky="w")
        self.product_var = tk.StringVar()
        products = ["Laptop", "Smartphone", "Headphones", "Camera", "Smartwatch"]
        self.product_combo = ttk.Combobox(form_frame, textvariable=self.product_var, values=products, state="readonly")
        self.product_combo.grid(row=0, column=1, pady=5)
        self.product_combo.current(0)

        ttk.Label(form_frame, text="Quantity:").grid(row=1, column=0, sticky="w")
        self.quantity_var = tk.IntVar(value=1)
        self.quantity_spin = tk.Spinbox(form_frame, from_=1, to=100, textvariable=self.quantity_var, width=5)
        self.quantity_spin.grid(row=1, column=1, sticky="w", pady=5)

        ttk.Button(form_frame, text="Submit Order", command=self.submit_order).grid(row=2, column=0, columnspan=2, pady=10)

        # -------- Order List Frame --------
        list_frame = ttk.LabelFrame(self, text="Order List", padding=10)
        list_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.order_listbox = tk.Listbox(list_frame, height=12)
        self.order_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.order_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.order_listbox.config(yscrollcommand=scrollbar.set)

    def submit_order(self):
        product = self.product_var.get()
        quantity = self.quantity_var.get()

        if not product:
            messagebox.showwarning("Missing Selection", "Please select a product.")
            return
        if quantity < 1:
            messagebox.showwarning("Invalid Quantity", "Quantity must be at least 1.")
            return

        order_entry = f"{product} x {quantity}"
        self.order_listbox.insert(tk.END, order_entry)

if __name__ == "__main__":
    ProductOrderForm().mainloop()
