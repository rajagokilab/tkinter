import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Combobox Widget Tasks")
root.geometry("400x500")

# 🔽 31. Create Combobox with fruits
fruits = ["Apple", "Banana", "Cherry"]
fruit_cb = ttk.Combobox(root, values=fruits)
fruit_cb.pack(pady=5)

# 🔽 32. Print selected value
def print_selection():
    selected = fruit_cb.get()
    tk.messagebox.showinfo("Selected Fruit", f"You selected: {selected}")

tk.Button(root, text="Show Selected Fruit", command=print_selection).pack()

# 🔽 33. Set default value
fruit_cb.current(0)  # Select "Apple"

# 🔽 34. Allow typing custom value (default mode allows this)
custom_entry = ttk.Combobox(root, values=["Cat", "Dog", "Rabbit"])
custom_entry.set("Type or Select")
custom_entry.pack(pady=5)

# 🔽 35. Disable editing (readonly mode)
readonly_cb = ttk.Combobox(root, values=["Red", "Green", "Blue"], state="readonly")
readonly_cb.current(1)
readonly_cb.pack(pady=5)

tk.Label(root, text="--- Dynamic Combobox Operations ---").pack(pady=10)

# 🔄 36. Update options in combobox
dynamic_cb = ttk.Combobox(root)
dynamic_cb.pack(pady=5)

def update_items():
    new_items = ["Python", "Java", "C++", "Go"]
    dynamic_cb['values'] = new_items
    dynamic_cb.set("Select Language")

tk.Button(root, text="Load Languages", command=update_items).pack()

# 🔄 37. Dependent dropdown: Country → City
tk.Label(root, text="Country:").pack()
country_cb = ttk.Combobox(root, values=["USA", "India", "UK"], state="readonly")
country_cb.pack()

tk.Label(root, text="City:").pack()
city_cb = ttk.Combobox(root, state="readonly")
city_cb.pack()

def update_cities(event=None):
    selected = country_cb.get()
    city_options = {
        "USA": ["New York", "Los Angeles", "Chicago"],
        "India": ["Delhi", "Mumbai", "Bangalore"],
        "UK": ["London", "Manchester", "Bristol"]
    }
    city_cb['values'] = city_options.get(selected, [])
    city_cb.set("")

country_cb.bind("<<ComboboxSelected>>", update_cities)

# 🔄 38. Clear selection/reset
def reset_combobox():
    fruit_cb.set("")

tk.Button(root, text="Clear Fruit Selection", command=reset_combobox).pack(pady=5)

# 🔄 39. Show selected in a Label
label_display = tk.Label(root, text="Selected: ")
label_display.pack(pady=5)

def update_label(event=None):
    label_display.config(text=f"Selected: {fruit_cb.get()}")

fruit_cb.bind("<<ComboboxSelected>>", update_label)

# 🔄 40. Searchable Combobox (filter options)
search_list = ["Python", "Java", "JavaScript", "C#", "C++", "Go", "Rust", "Kotlin"]
search_cb = ttk.Combobox(root)
search_cb.pack(pady=5)

def filter_options(event):
    input_text = search_cb.get().lower()
    filtered = [item for item in search_list if input_text in item.lower()]
    search_cb['values'] = filtered

search_cb.bind('<KeyRelease>', filter_options)
search_cb.set("Search language")

root.mainloop()
