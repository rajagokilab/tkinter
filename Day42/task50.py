import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Spinbox Widget Tasks")
root.geometry("450x600")

# 🔢 Numeric Range Tasks

# 41. Create Spinbox 0 to 100
spin_0_100 = tk.Spinbox(root, from_=0, to=100)
spin_0_100.pack(pady=5)

# 42. Spinbox stepping by 5
spin_step5 = tk.Spinbox(root, from_=0, to=100, increment=5)
spin_step5.pack(pady=5)

# 43. Get value on button click
def get_spin_value():
    val = spin_0_100.get()
    tk.messagebox.showinfo("Spinbox Value", f"Value: {val}")

btn_get_value = tk.Button(root, text="Get Spinbox Value", command=get_spin_value)
btn_get_value.pack(pady=5)

# 44. Display Spinbox value dynamically
label_dynamic = tk.Label(root, text="Current Value: 0")
label_dynamic.pack()

def update_label(*args):
    label_dynamic.config(text=f"Current Value: {spin_0_100.get()}")

spin_0_100.config(command=update_label)

# 45. Disable Spinbox conditionally with checkbox
def toggle_spinbox():
    if disable_var.get():
        spin_0_100.config(state='disabled')
    else:
        spin_0_100.config(state='normal')

disable_var = tk.BooleanVar()
chk_disable = tk.Checkbutton(root, text="Disable Spinbox", variable=disable_var, command=toggle_spinbox)
chk_disable.pack(pady=5)

# 🧠 Advanced Spinbox Tasks

# 46. Time format (1-12) + AM/PM using two spinboxes
time_frame = tk.Frame(root)
time_frame.pack(pady=10)

spin_hour = tk.Spinbox(time_frame, from_=1, to=12, width=5)
spin_hour.pack(side=tk.LEFT, padx=5)

am_pm = ttk.Combobox(time_frame, values=["AM", "PM"], state='readonly', width=5)
am_pm.current(0)
am_pm.pack(side=tk.LEFT, padx=5)

tk.Label(root, text="Select Time (Hour + AM/PM)").pack()

# 47. Quantity Spinbox 1-10
spin_quantity = tk.Spinbox(root, from_=1, to=10, width=5)
spin_quantity.pack(pady=5)

tk.Label(root, text="Select Quantity (1-10)").pack()

# 48. Use Spinbox to control canvas size dynamically
canvas_frame = tk.Frame(root)
canvas_frame.pack(pady=10)

canvas_size = tk.IntVar(value=200)
canvas = tk.Canvas(canvas_frame, width=canvas_size.get(), height=canvas_size.get(), bg='lightblue')
canvas.pack()

def resize_canvas():
    size = canvas_size_spin.get()
    canvas.config(width=int(size), height=int(size))

canvas_size_spin = tk.Spinbox(root, from_=100, to=400, increment=10, textvariable=canvas_size, command=resize_canvas)
canvas_size_spin.pack(pady=5)

tk.Label(root, text="Adjust Canvas Size").pack()

# 49. Use Spinbox to control animation speed of canvas object
rect = canvas.create_rectangle(10, 10, 60, 60, fill="green")

speed_var = tk.IntVar(value=50)

def animate():
    x1, y1, x2, y2 = canvas.coords(rect)
    if x2 >= canvas_size.get() or x1 <= 0:
        global direction
        direction = -direction
    canvas.move(rect, direction, 0)
    root.after(speed_var.get(), animate)

direction = 5
animate()

def update_speed():
    speed_var.set(int(speed_spin.get()))

speed_spin = tk.Spinbox(root, from_=10, to=200, increment=10, command=update_speed)
speed_spin.pack(pady=5)

tk.Label(root, text="Adjust Animation Speed (ms)").pack()

# 50. Combine Combobox + Spinbox to select "Item" and "Quantity"
combo_spin_frame = tk.Frame(root)
combo_spin_frame.pack(pady=10)

items_combo = ttk.Combobox(combo_spin_frame, values=["Pen", "Notebook", "Eraser"], state='readonly', width=15)
items_combo.current(0)
items_combo.pack(side=tk.LEFT, padx=5)

qty_spin = tk.Spinbox(combo_spin_frame, from_=1, to=20, width=5)
qty_spin.pack(side=tk.LEFT, padx=5)

def show_selection():
    item = items_combo.get()
    qty = qty_spin.get()
    tk.messagebox.showinfo("Selection", f"Item: {item}\nQuantity: {qty}")

btn_show = tk.Button(root, text="Show Selection", command=show_selection)
btn_show.pack(pady=10)

root.mainloop()
