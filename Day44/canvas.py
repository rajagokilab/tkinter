import tkinter as tk

class CanvasMover(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Canvas Object Mover with Keys")
        self.geometry("400x300")

        self.canvas = tk.Canvas(self, width=350, height=250, bg="white")
        self.canvas.pack(padx=20, pady=20)

        # Create a rectangle at start position
        self.rect_size = 50
        self.rect = self.canvas.create_rectangle(50, 50, 50 + self.rect_size, 50 + self.rect_size, fill="blue")

        self.step = 10  # pixels to move per key press

        self.bind("<Left>", self.move_left)
        self.bind("<Right>", self.move_right)
        self.bind("<Up>", self.move_up)
        self.bind("<Down>", self.move_down)

    def move_left(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        if x1 - self.step >= 0:
            self.canvas.move(self.rect, -self.step, 0)

    def move_right(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        if x2 + self.step <= self.canvas.winfo_width():
            self.canvas.move(self.rect, self.step, 0)

    def move_up(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        if y1 - self.step >= 0:
            self.canvas.move(self.rect, 0, -self.step)

    def move_down(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        if y2 + self.step <= self.canvas.winfo_height():
            self.canvas.move(self.rect, 0, self.step)

if __name__ == "__main__":
    app = CanvasMover()
    app.mainloop()
