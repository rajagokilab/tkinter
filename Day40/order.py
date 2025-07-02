import tkinter as tk
from tkinter import messagebox

# Product data: name and price
products = {
    "Apple": 0.5,
    "Banana": 0.3,
    "Orange": 0.7,
}

def validate_quantity(P):
    # Allow empty string or digits only
    if P == "" or P.isdigit():
        return True
    return False

def update_total(*args):
    total = 0.0
    for product, var in qty_vars.items():
        qty = var.get()
        if qty.isdigit():
            total += int(qty) * products[product]
    total_var.set(f"Total Price: ${total:.2f}")

def place_order():
    order_summary = []
    for product, var in qty_vars.items():
        qty = var.get()
        if qty.isdigit() and int(qty) > 0:
            order_summary.append(f"{product}: {qty} pcs")
    if not order_summary:
        messagebox.showwarning("Order", "Please enter quantities before placing order.")
        return
    messagebox.showinfo("Order Placed", "You ordered:\n" + "\n".join(order_summary))

root = tk.Tk()
root.title("Basic Product Order Form")
root.geometry("350x200")

qty_vars = {}
vcmd = (root.register(validate_quantity), '%P')

# Create form header
tk.Label(root, text="Product").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Price ($)").grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Quantity").grid(row=0, column=2, padx=10, pady=5)

# List products with price and quantity entry
for i, (product, price) in enumerate(products.items(), start=1):
    tk.Label(root, text=product).grid(row=i, column=0, sticky="w", padx=10)
    tk.Label(root, text=f"{price:.2f}").grid(row=i, column=1)
    
    var = tk.StringVar()
    var.trace_add("write", update_total)
    qty_vars[product] = var
    
    entry = tk.Entry(root, width=10, textvariable=var, validate="key", validatecommand=vcmd)
    entry.grid(row=i, column=2, padx=10)

total_var = tk.StringVar(value="Total Price: $0.00")
tk.Label(root, textvariable=total_var, font=("Arial", 12, "bold")).grid(row=len(products)+1, column=0, columnspan=3, pady=10)

btn_order = tk.Button(root, text="Place Order", command=place_order)
btn_order.grid(row=len(products)+2, column=0, columnspan=3, pady=10)

root.mainloop()
