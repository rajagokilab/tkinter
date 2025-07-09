import tkinter as tk
from tkinter import ttk

def draw_circle(event):
    x, y = event.x, event.y
    r = 20
    color = color_combo.get()
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")
    coord_label.config(text=f"Circle at ({x}, {y})")

def draw_square(event):
    x, y = event.x, event.y
    side = 40
    color = color_combo.get()
    half = side // 2
    canvas.create_rectangle(x - half, y - half, x + half, y + half, fill=color, outline="")
    coord_label.config(text=f"Square at ({x}, {y})")

root = tk.Tk()
root.title("Shape Drawing with Coordinates")

# Color selection Combobox
color_label = tk.Label(root, text="Select Color:")
color_label.pack(pady=5)
colors = ["red", "green", "blue", "yellow", "purple", "orange", "black"]
color_combo = ttk.Combobox(root, values=colors, state="readonly")
color_combo.current(0)
color_combo.pack()

# Canvas for drawing
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack(pady=10)

# Label to show coordinates
coord_label = tk.Label(root, text="Click on canvas to draw shapes")
coord_label.pack()

# Bind mouse clicks
canvas.bind("<Button-1>", draw_circle)   # Left click draws circle
canvas.bind("<Button-3>", draw_square)   # Right click draws square

root.mainloop()
