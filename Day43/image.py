import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.root.geometry("800x600")

        self.image = None
        self.photo = None
        self.zoom_level = 1.0

        self.create_menu()
        self.create_toolbar()
        self.create_canvas()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_image)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        open_btn = tk.Button(toolbar, text="Open Image", command=self.open_image)
        open_btn.pack(side="left", padx=5, pady=5)

        zoom_in_btn = tk.Button(toolbar, text="Zoom In", command=self.zoom_in)
        zoom_in_btn.pack(side="left", padx=5, pady=5)

        zoom_out_btn = tk.Button(toolbar, text="Zoom Out", command=self.zoom_out)
        zoom_out_btn.pack(side="left", padx=5, pady=5)

    def create_canvas(self):
        self.canvas = tk.Canvas(self.root, bg="gray")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Configure>", self.redraw_image)

    def open_image(self):
        filetypes = [
            ("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"),
            ("All files", "*.*")
        ]
        path = filedialog.askopenfilename(title="Open Image", filetypes=filetypes)
        if path:
            try:
                self.image = Image.open(path)
                self.zoom_level = 1.0
                self.redraw_image()
            except Exception as e:
                messagebox.showerror("Error", f"Cannot open image:\n{e}")

    def redraw_image(self, event=None):
        if self.image:
            # Resize image based on zoom_level
            w, h = self.image.size
            new_size = (int(w * self.zoom_level), int(h * self.zoom_level))
            resized = self.image.resize(new_size, Image.ANTIALIAS)
            self.photo = ImageTk.PhotoImage(resized)

            self.canvas.delete("all")
            # Center image in canvas
            canvas_w = self.canvas.winfo_width()
            canvas_h = self.canvas.winfo_height()
            x = (canvas_w - new_size[0]) // 2
            y = (canvas_h - new_size[1]) // 2
            self.canvas.create_image(x, y, anchor="nw", image=self.photo)

    def zoom_in(self):
        if self.image:
            self.zoom_level *= 1.2
            self.redraw_image()

    def zoom_out(self):
        if self.image:
            self.zoom_level /= 1.2
            self.redraw_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageViewer(root)
    root.mainloop()
