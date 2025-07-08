import tkinter as tk
from tkinter import ttk

class GridGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Grid Game")

        # Canvas settings
        self.rows = 5
        self.cols = 5
        self.cell_size = 60
        self.canvas_size = self.cell_size * self.rows

        # Track marked cells: set of (row, col)
        self.marked_cells = set()

        # Canvas
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack(side="left", padx=10, pady=10)
        self.draw_grid()

        # Bind click event
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Frame for listbox and reset button
        right_frame = ttk.Frame(root)
        right_frame.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(right_frame, text="Clicked Positions:").pack(anchor="w")

        # Listbox + scrollbar
        self.log_listbox = tk.Listbox(right_frame, height=12)
        self.log_listbox.pack(side="left", fill="y")

        self.scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.log_listbox.yview)
        self.scrollbar.pack(side="left", fill="y")
        self.log_listbox.config(yscrollcommand=self.scrollbar.set)

        # Reset button
        self.reset_btn = ttk.Button(right_frame, text="Reset", command=self.reset_game)
        self.reset_btn.pack(pady=10)

    def draw_grid(self):
        self.canvas.delete("gridline")
        for i in range(self.rows + 1):
            # Horizontal lines
            y = i * self.cell_size
            self.canvas.create_line(0, y, self.canvas_size, y, tag="gridline")
        for j in range(self.cols + 1):
            # Vertical lines
            x = j * self.cell_size
            self.canvas.create_line(x, 0, x, self.canvas_size, tag="gridline")

        # Redraw marked cells
        for (r, c) in self.marked_cells:
            self.fill_cell(r, c)

    def fill_cell(self, row, col):
        x1 = col * self.cell_size + 1
        y1 = row * self.cell_size + 1
        x2 = (col + 1) * self.cell_size - 1
        y2 = (row + 1) * self.cell_size - 1
        self.canvas.create_rectangle(x1, y1, x2, y2, fill="lightblue", tags="mark")

    def clear_cell(self, row, col):
        # Remove rectangles tagged 'mark' inside that cell area
        x1 = col * self.cell_size + 1
        y1 = row * self.cell_size + 1
        x2 = (col + 1) * self.cell_size - 1
        y2 = (row + 1) * self.cell_size - 1
        # Find items overlapping this area and delete them if tagged "mark"
        items = self.canvas.find_enclosed(x1, y1, x2, y2)
        for item in items:
            if "mark" in self.canvas.gettags(item):
                self.canvas.delete(item)

    def on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            if (row, col) in self.marked_cells:
                # Unmark cell
                self.marked_cells.remove((row, col))
                self.clear_cell(row, col)
            else:
                # Mark cell
                self.marked_cells.add((row, col))
                self.fill_cell(row, col)

            # Log clicked position
            pos_text = f"Row: {row+1}, Col: {col+1}"
            self.log_listbox.insert("end", pos_text)
            self.log_listbox.yview_moveto(1)  # Auto scroll to bottom

    def reset_game(self):
        self.marked_cells.clear()
        self.canvas.delete("mark")
        self.log_listbox.delete(0, "end")

if __name__ == "__main__":
    root = tk.Tk()
    GridGameApp(root)
    root.mainloop()
