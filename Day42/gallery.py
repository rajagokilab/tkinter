import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk
import os

class PhotoGalleryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Gallery Viewer")
        self.root.geometry("700x500")

        # Sample image data: filename -> (image_type, color_for_placeholder)
        self.all_images = {
            "beach.jpg": ("JPG", "lightblue"),
            "forest.png": ("PNG", "lightgreen"),
            "mountain.jpg": ("JPG", "lightgray"),
            "city.png": ("PNG", "lightyellow"),
            "sunset.jpg": ("JPG", "orange"),
            "river.png": ("PNG", "lightcyan"),
        }

        # Current filtered image list
        self.filtered_images = []

        # --- Left Frame: Listbox + scrollbar + filter combobox ---
        left_frame = ttk.Frame(root)
        left_frame.pack(side="left", fill="y", padx=10, pady=10)

        ttk.Label(left_frame, text="Filter by Type:").pack(anchor="w")
        self.filter_var = tk.StringVar(value="All")
        self.filter_cb = ttk.Combobox(left_frame, textvariable=self.filter_var, state="readonly",
                                      values=["All", "JPG", "PNG"])
        self.filter_cb.pack(fill="x")
        self.filter_cb.bind("<<ComboboxSelected>>", self.update_image_list)

        ttk.Label(left_frame, text="Images:").pack(anchor="w", pady=(10,0))

        # Listbox + scrollbar
        self.listbox = tk.Listbox(left_frame, width=30, height=20)
        self.listbox.pack(side="left", fill="y")
        self.scrollbar = ttk.Scrollbar(left_frame, orient="vertical", command=self.listbox.yview)
        self.scrollbar.pack(side="left", fill="y")
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.listbox.bind("<<ListboxSelect>>", self.on_image_select)

        # Buttons for delete/rename
        btn_frame = ttk.Frame(left_frame)
        btn_frame.pack(fill="x", pady=10)
        self.delete_btn = ttk.Button(btn_frame, text="Delete", command=self.delete_image)
        self.delete_btn.pack(side="left", expand=True, fill="x", padx=5)
        self.rename_btn = ttk.Button(btn_frame, text="Rename", command=self.rename_image)
        self.rename_btn.pack(side="left", expand=True, fill="x", padx=5)

        # --- Right Frame: Canvas to show image ---
        right_frame = ttk.Frame(root)
        right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.canvas_size = 400
        self.canvas = tk.Canvas(right_frame, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack(expand=True)

        # Keep reference of displayed image for Tkinter
        self.tk_image = None

        # Initialize list
        self.update_image_list()

    def update_image_list(self, event=None):
        filter_type = self.filter_var.get()
        if filter_type == "All":
            self.filtered_images = list(self.all_images.keys())
        else:
            self.filtered_images = [f for f, (typ, _) in self.all_images.items() if typ == filter_type]

        self.listbox.delete(0, "end")
        for fname in self.filtered_images:
            self.listbox.insert("end", fname)

        self.canvas.delete("all")
        self.tk_image = None

    def on_image_select(self, event):
        sel = self.listbox.curselection()
        if not sel:
            return
        fname = self.filtered_images[sel[0]]
        img_type, color = self.all_images[fname]
        self.display_placeholder_image(fname, color)

    def display_placeholder_image(self, filename, color):
        self.canvas.delete("all")

        # Placeholder rectangle with filename text
        pad = 10
        self.canvas.create_rectangle(pad, pad, self.canvas_size - pad, self.canvas_size - pad,
                                     fill=color, outline="black")
        self.canvas.create_text(self.canvas_size//2, self.canvas_size//2, text=filename,
                                font=("Arial", 20, "bold"))

    def delete_image(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("No selection", "Please select an image to delete.")
            return
        idx = sel[0]
        fname = self.filtered_images[idx]

        if messagebox.askyesno("Confirm Delete", f"Delete image '{fname}'?"):
            del self.all_images[fname]
            self.update_image_list()

    def rename_image(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("No selection", "Please select an image to rename.")
            return
        idx = sel[0]
        old_name = self.filtered_images[idx]

        new_name = simpledialog.askstring("Rename Image", "Enter new filename:", initialvalue=old_name)
        if new_name:
            if new_name in self.all_images:
                messagebox.showerror("Error", "Filename already exists.")
                return

            # Keep type and color from old
            self.all_images[new_name] = self.all_images.pop(old_name)
            self.update_image_list()

if __name__ == "__main__":
    root = tk.Tk()
    PhotoGalleryApp(root)
    root.mainloop()
