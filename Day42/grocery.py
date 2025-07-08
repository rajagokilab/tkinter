import tkinter as tk
from tkinter import ttk

# === Sample Product Data ===
products = {
    "Fruits": ["Apple", "Banana", "Orange", "Grapes", "Pineapple", "Mango"],
    "Vegetables": ["Carrot", "Potato", "Tomato", "Spinach", "Broccoli", "Onion"],
    "Drinks": ["Water", "Juice", "Soda", "Milk", "Tea", "Coffee"]
}

# === Main Window ===
root = tk.Tk()
root.title("Grocery Order Interface")
root.geometry("600x400")

# === Variables ===
selected_category = tk.StringVar(value="Fruits")
quantity_var = tk.IntVar(value=1)

# === Category Selector ===
tk.Label(root, text="Select Category:").pack()
category_cb = ttk.Combobox(root, values=list(products.keys()), textvariable=selected_category, state="readonly")
category_cb.pack()

# === Product Listbox with Scrollbar ===
product_frame = tk.Frame(root)
product_frame.pack(pady=5)

product_scroll = tk.Scrollbar(product_frame)
product_scroll.pack(side=tk.RIGHT, fill=tk.Y)

product_listbox = tk.Listbox(product_frame, height=6, yscrollcommand=product_scroll.set, exportselection=False)
product_listbox.pack(side=tk.LEFT, padx=5)
product_scroll.config(command=product_listbox.yview)

# === Quantity ===
tk.Label(root, text="Quantity:").pack()
qty_spin = tk.Spinbox(root, from_=1, to=50, textvariable=quantity_var, width=5)
qty_spin.pack()

# === Cart Listbox with Scrollbar ===
cart_frame = tk.Frame(root)
cart_frame.pack(pady=5)

tk.Label(cart_frame, text="🛒 Cart").pack()

cart_scroll = tk.Scrollbar(cart_frame)
cart_scroll.pack(side=tk.RIGHT, fill=tk.Y)

cart_listbox = tk.Listbox(cart_frame, height=8, yscrollcommand=cart_scroll.set)
cart_listbox.pack(side=tk.LEFT, padx=5)
cart_scroll.config(command=cart_listbox.yview)

# === Populate product list on category change ===
def update_products(event=None):
    product_listbox.delete(0, tk.END)
    for item in products[selected_category.get()]:
        product_listbox.insert(tk.END, item)

# === Add to Cart ===
def add_to_cart():
    selected_index = product_listbox.curselection()
    if selected_index:
        item = product_listbox.get(selected_index[0])
        qty = quantity_var.get()
        cart_listbox.insert(tk.END, f"{item} x {qty}")

# === Add Button ===
tk.Button(root, text="Add to Cart", command=add_to_cart).pack(pady=5)

# Bind update on category change
category_cb.bind("<<ComboboxSelected>>", update_products)

# Load initial products
update_products()

root.mainloop()
