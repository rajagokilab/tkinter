import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Drawing Tool Application")
root.geometry("500x550")

# === Top Controls Frame ===
controls = tk.Frame(root)
controls.pack(pady=10)

# Shape selection Combobox
tk.Label(controls, text="Shape:").grid(row=0, column=0, padx=5)
shape_cb = ttk.Combobox(controls, values=["Rectangle", "Circle", "Line"], state="readonly", width=10)
shape_cb.current(0)
shape_cb.grid(row=0, column=1)

# Color selection Combobox
tk.Label(controls, text="Color:").grid(row=0, column=2, padx=5)
color_cb = ttk.Combobox(controls, values=["black", "red", "blue", "green", "orange", "purple"], state="readonly", width=10)
color_cb.current(0)
color_cb.grid(row=0, column=3)

# Line thickness Spinbox
tk.Label(controls, text="Size:").grid(row=0, column=4, padx=5)
size_spin = tk.Spinbox(controls, from_=1, to=20, width=5)
size_spin.grid(row=0, column=5)

# === Canvas for Drawing ===
canvas = tk.Canvas(root, bg="white", width=480, height=400)
canvas.pack(pady=10)

# === Clear Button ===
def clear_canvas():
    canvas.delete("all")

tk.Button(root, text="Clear Canvas", command=clear_canvas).pack()

# === Shape Drawing Logic ===
start_x, start_y = None, None

def on_click(event):
    global start_x, start_y
    shape = shape_cb.get()
    color = color_cb.get()
    size = int(size_spin.get())

    # Save start point for line drawing
    if shape == "Line":
        if start_x is None:
            start_x, start_y = event.x, event.y
        else:
            canvas.create_line(start_x, start_y, event.x, event.y, fill=color, width=size)
            start_x, start_y = None, None
    else:
        offset = size * 5
        x1, y1 = event.x - offset, event.y - offset
        x2, y2 = event.x + offset, event.y + offset

        if shape == "Rectangle":
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color, width=size)
        elif shape == "Circle":
            canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color, width=size)

canvas.bind("<Button-1>", on_click)

root.mainloop()
