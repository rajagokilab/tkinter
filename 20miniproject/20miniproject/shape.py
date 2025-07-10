import tkinter as tk
from tkinter import ttk

def draw_circle(event):
    color = color_combo.get()
    r = 20
    x, y = event.x, event.y
    canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="")

    coord_label.config(text=f"Circle at ({x}, {y})")

def draw_square(event):
    color = color_combo.get()
    side = 40
    x, y = event.x, event.y
    half = side // 2
    canvas.create_rectangle(x - half, y - half, x + half, y + half, fill=color, outline="")

    coord_label.config(text=f"Square at ({x}, {y})")

# === Main Window ===
root = tk.Tk()
root.title("Shape Drawing with Coordinates")
root.geometry("500x400")

# Color selection Combobox
color_label = tk.Label(root, text="Select Color:")
color_label.pack(pady=5)

color_combo = ttk.Combobox(root, values=["red", "green", "blue", "yellow", "purple"], state="readonly")
color_combo.pack()
color_combo.set("red")

# Canvas
canvas = tk.Canvas(root, bg="white", width=480, height=300)
canvas.pack(pady=10)

# Coordinate Label
coord_label = tk.Label(root, text="Click on canvas to draw shape", font=("Arial", 12))
coord_label.pack(pady=5)

# Bind mouse clicks
canvas.bind("<Button-1>", draw_circle)  # Left-click
canvas.bind("<Button-3>", draw_square)  # Right-click (on Mac: might be Ctrl+Click)

root.mainloop()
