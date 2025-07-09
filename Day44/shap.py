import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    radius = 15
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")
    coord_label.config(text=f"Circle at ({x}, {y})")

def draw_rectangle(event):
    x, y = event.x, event.y
    size = 30
    canvas.create_rectangle(x, y, x + size, y + size, fill="red")
    coord_label.config(text=f"Rectangle at ({x}, {y})")

root = tk.Tk()
root.title("Shape Drawer Canvas")
root.geometry("400x400")

canvas = tk.Canvas(root, bg="white", width=380, height=320)
canvas.pack(pady=10)

coord_label = tk.Label(root, text="Click to draw shapes")
coord_label.pack()

canvas.bind("<Button-1>", draw_circle)    # Left click draws circle
canvas.bind("<Button-3>", draw_rectangle) # Right click draws rectangle

root.mainloop()
