import tkinter as tk
from tkinter import ttk

# Function to draw shape on canvas at mouse click
def draw_shape(event):
    shape = shape_combobox.get()
    color = color_combobox.get()

    x, y = event.x, event.y
    size = 40  # Fixed size for simplicity

    if shape == "Rectangle":
        canvas.create_rectangle(x, y, x + size, y + size, fill=color)
    elif shape == "Oval":
        canvas.create_oval(x, y, x + size, y + size, fill=color)

# Main Window
root = tk.Tk()
root.title("Canvas Drawing Shapes Tool")
root.geometry("500x450")

# === Controls Frame ===
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

# Shape Selection
tk.Label(control_frame, text="Shape:").pack(side="left", padx=(0, 5))
shape_combobox = ttk.Combobox(control_frame, values=["Rectangle", "Oval"], state="readonly")
shape_combobox.pack(side="left", padx=5)
shape_combobox.set("Rectangle")

# Color Selection
tk.Label(control_frame, text="Color:").pack(side="left", padx=(10, 5))
color_combobox = ttk.Combobox(control_frame, values=["red", "green", "blue", "yellow", "black"], state="readonly")
color_combobox.pack(side="left", padx=5)
color_combobox.set("blue")

# === Drawing Canvas ===
canvas = tk.Canvas(root, width=450, height=350, bg="white")
canvas.pack(pady=10)
canvas.bind("<Button-1>", draw_shape)

root.mainloop()
