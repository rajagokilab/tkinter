import tkinter as tk
from tkinter import ttk

# === Main window ===
root = tk.Tk()
root.title("Color Picker App")
root.geometry("500x500")

# === Selected color ===
selected_color = tk.StringVar(value="Red")

# === Color Combobox ===
colors = ["Red", "Green", "Blue", "Yellow", "Orange", "Purple", "Black"]
tk.Label(root, text="Choose Color:").pack(pady=5)
color_cb = ttk.Combobox(root, values=colors, textvariable=selected_color, state="readonly")
color_cb.pack()

# === Canvas ===
canvas = tk.Canvas(root, bg="white", width=480, height=400)
canvas.pack(pady=10)

# === Coordinate + Color Label ===
info_label = tk.Label(root, text="Click on canvas to paint", font=("Arial", 10))
info_label.pack()

# === Constants ===
CELL_SIZE = 20  # Square cell size

# === Painting with Left Click ===
def paint(event):
    x = event.x - (event.x % CELL_SIZE)
    y = event.y - (event.y % CELL_SIZE)
    color = selected_color.get()
    canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill=color, outline="")
    info_label.config(text=f"Painted ({x}, {y}) with {color}")

# === Erasing with Right Click ===
def erase(event):
    x = event.x - (event.x % CELL_SIZE)
    y = event.y - (event.y % CELL_SIZE)
    canvas.create_rectangle(x, y, x + CELL_SIZE, y + CELL_SIZE, fill="white", outline="")
    info_label.config(text=f"Erased at ({x}, {y})")

# === Event Bindings ===
canvas.bind("<Button-1>", paint)    # Left click
canvas.bind("<Button-3>", erase)    # Right click

root.mainloop()
