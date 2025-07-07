import tkinter as tk
from tkinter import ttk

SHAPES = ["Oval", "Rectangle", "Line"]

class ShapeDrawer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Shape Drawing Canvas")
        self.geometry("500x500")

        # ---------- Shape selection ----------
        ttk.Label(self, text="Select Shape:").pack(pady=(10, 2))
        self.shape_var = tk.StringVar(value=SHAPES[0])
        self.shape_combo = ttk.Combobox(self, textvariable=self.shape_var, values=SHAPES, state="readonly")
        self.shape_combo.pack()

        # ---------- Canvas ----------
        self.canvas = tk.Canvas(self, bg="white", width=480, height=400)
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.draw_shape)

        # ---------- Coordinate label ----------
        self.coord_label = ttk.Label(self, text="Click anywhere on canvas")
        self.coord_label.pack(pady=(0, 10))

    def draw_shape(self, event):
        shape = self.shape_var.get()
        x, y = event.x, event.y
        self.coord_label.config(text=f"Last click: ({x}, {y})")

        size = 40  # size of shape

        if shape == "Oval":
            self.canvas.create_oval(x - size, y - size, x + size, y + size, fill="skyblue")
        elif shape == "Rectangle":
            self.canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="lightgreen")
        elif shape == "Line":
            self.canvas.create_line(x - size, y - size, x + size, y + size, fill="black", width=2)

if __name__ == "__main__":
    ShapeDrawer().mainloop()
