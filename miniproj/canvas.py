import tkinter as tk
from tkinter import ttk

def draw_shape(event):
    shape = shape_combobox.get()
    color = color_combobox.get()
    x, y = event.x, event.y
    size = 50  # fixed size for shapes

    if shape == "Rectangle":
        canvas.create_rectangle(x, y, x + size, y + size, fill=color, outline="black")
    elif shape == "Oval":
        canvas.create_oval(x, y, x + size, y + size, fill=color, outline="black")

root = tk.Tk()
root.title("Canvas Drawing Shapes Tool")

# Controls frame
controls_frame = tk.Frame(root)
controls_frame.pack(pady=10)

tk.Label(controls_frame, text="Shape:").grid(row=0, column=0, padx=5)
shape_combobox = ttk.Combobox(controls_frame, values=["Rectangle", "Oval"], state="readonly", width=10)
shape_combobox.grid(row=0, column=1, padx=5)
shape_combobox.current(0)

tk.Label(controls_frame, text="Color:").grid(row=0, column=2, padx=5)
color_combobox = ttk.Combobox(controls_frame, values=["red", "green", "blue", "yellow", "orange", "purple"], state="readonly", width=10)
color_combobox.grid(row=0, column=3, padx=5)
color_combobox.current(0)

# Canvas for drawing
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)

# Bind left click to drawing function
canvas.bind("<Button-1>", draw_shape)

root.mainloop()
