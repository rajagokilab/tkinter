import tkinter as tk
from tkinter import messagebox, simpledialog

# Sample product data (ID: Description)
products = {
    f"Product {i}": f"Details of Product {i}. This is a sample description."
    for i in range(1, 61)
}

def update_product_list():
    product_listbox.delete(0, tk.END)
    for product in products.keys():
        product_listbox.insert(tk.END, product)

def show_product_details(event):
    selection = product_listbox.curselection()
    if selection:
        product_name = product_listbox.get(selection[0])
        details = products.get(product_name, "No details available.")
        details_label.config(text=f"{product_name}:\n{details}")

def add_product():
    new_name = simpledialog.askstring("Add Product", "Enter product name:")
    if new_name:
        if new_name in products:
            messagebox.showwarning("Duplicate", "Product already exists.")
            return
        new_details = simpledialog.askstring("Add Product", "Enter product details:")
        products[new_name] = new_details or "No details provided."
        update_product_list()

def delete_product():
    selection = product_listbox.curselection()
    if not selection:
        messagebox.showwarning("No selection", "Please select a product to delete.")
        return
    product_name = product_listbox.get(selection[0])
    confirm = messagebox.askyesno("Delete Product", f"Delete {product_name}?")
    if confirm:
        products.pop(product_name, None)
        update_product_list()
        details_label.config(text="")

# === Main Window ===
root = tk.Tk()
root.title("Scrollable Product List")
root.geometry("500x400")
root.configure(padx=10, pady=10)

# === Frame for Listbox and Scrollbar ===
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

product_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
product_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=product_listbox.yview)

product_listbox.bind("<<ListboxSelect>>", show_product_details)

# === Details Label ===
details_label = tk.Label(root, text="Select a product to see details.", justify=tk.LEFT, anchor="w", bg="#f0f0f0", relief=tk.SUNKEN, padx=10, pady=10, width=60, height=5)
details_label.pack(pady=10, fill=tk.X)

# === Buttons Frame ===
btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add Product", width=15, command=add_product)
add_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Product", width=15, command=delete_product)
delete_btn.pack(side=tk.LEFT, padx=5)

# Populate initial list
update_product_list()

root.mainloop()
