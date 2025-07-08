import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Listbox Widget Tasks")

# 📋 21. Create Listbox and insert five static items
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=30, height=10)
items = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
for item in items:
    listbox.insert(tk.END, item)
listbox.pack()

# 📋 22. Print selected item (single)
def print_selected():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        messagebox.showinfo("Selected Item", f"You selected: {item}")

btn_single = tk.Button(root, text="Show Selected Item", command=print_selected)
btn_single.pack(pady=2)

# 📋 23. Print multiple selections
def print_all_selected():
    selected = listbox.curselection()
    items = [listbox.get(i) for i in selected]
    messagebox.showinfo("Multiple Selected", f"You selected: {', '.join(items)}")

btn_multi = tk.Button(root, text="Show All Selected", command=print_all_selected)
btn_multi.pack(pady=2)

# 📋 24. Clear all items
def clear_listbox():
    listbox.delete(0, tk.END)

btn_clear = tk.Button(root, text="Clear Listbox", command=clear_listbox)
btn_clear.pack(pady=2)

# 📋 25. Add item dynamically
entry = tk.Entry(root)
entry.pack(pady=2)

def add_item():
    text = entry.get()
    if text:
        listbox.insert(tk.END, text)
        entry.delete(0, tk.END)

btn_add = tk.Button(root, text="Add Item", command=add_item)
btn_add.pack(pady=2)

# Separator
tk.Label(root, text="--- Scrollbar Section ---").pack(pady=10)

# 🧭 26. Listbox with 20+ items and vertical scrollbar
frame_scroll = tk.Frame(root)
frame_scroll.pack()

scrollbar_y = tk.Scrollbar(frame_scroll, orient=tk.VERTICAL)
scroll_listbox = tk.Listbox(frame_scroll, yscrollcommand=scrollbar_y.set, width=50)
scrollbar_y.config(command=scroll_listbox.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_listbox.pack(side=tk.LEFT)

for i in range(1, 31):
    scroll_listbox.insert(tk.END, f"Item number {i}")

# 🧭 27. Horizontal scrollbar for long text
scrollbar_x = tk.Scrollbar(root, orient=tk.HORIZONTAL)
scroll_x_listbox = tk.Listbox(root, width=50, xscrollcommand=scrollbar_x.set)
scrollbar_x.config(command=scroll_x_listbox.xview)
scroll_x_listbox.config(width=40)
scrollbar_x.pack(fill=tk.X)
scroll_x_listbox.pack()

# Add long items
long_items = ["This is a very long item name " + str(i) for i in range(1, 6)]
for item in long_items:
    scroll_x_listbox.insert(tk.END, item)

# 🧭 28. Sync yscrollcommand (already done in #26)

# 🧭 29. Scroll programmatically to specific item
def scroll_to_item_10():
    scroll_listbox.see(9)  # Index 9 is Item 10

btn_scroll = tk.Button(root, text="Scroll to Item 10", command=scroll_to_item_10)
btn_scroll.pack(pady=4)

# 🧭 30. Show current scroll position
def show_scroll_position():
    pos = scroll_listbox.yview()
    messagebox.showinfo("Scroll Position", f"Top and Bottom fractions: {pos}")

btn_yview = tk.Button(root, text="Show Scroll Position", command=show_scroll_position)
btn_yview.pack(pady=4)

root.mainloop()
