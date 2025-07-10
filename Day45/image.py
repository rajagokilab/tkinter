import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Organizer App")

        self.image_list = []
        self.current_image = None

        self.setup_ui()

    def setup_ui(self):
        # Directory selection
        tk.Button(self.root, text="Select Folder", command=self.select_folder).pack(pady=5)

        # Listbox for image files
        self.listbox = tk.Listbox(self.root, width=40)
        self.listbox.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)
        self.listbox.bind('<<ListboxSelect>>', self.display_image)

        # Canvas for image display
        self.canvas = tk.Canvas(self.root, bg="gray", width=500, height=400)
        self.canvas.pack(side=tk.LEFT, padx=5, pady=5)

        # Label for image dimensions
        self.dim_label = tk.Label(self.root, text="Dimensions: ")
        self.dim_label.pack(pady=5)

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        if not folder_path:
            return

        self.image_list = [f for f in os.listdir(folder_path)
                           if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        self.listbox.delete(0, tk.END)
        self.folder_path = folder_path

        if not self.image_list:
            messagebox.showinfo("No Images", "No image files found in the selected folder.")
        else:
            for img in self.image_list:
                self.listbox.insert(tk.END, img)

    def display_image(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return

        filename = self.image_list[selection[0]]
        filepath = os.path.join(self.folder_path, filename)

        try:
            image = Image.open(filepath)
            image.thumbnail((500, 400))  # Resize to fit canvas
            self.current_image = ImageTk.PhotoImage(image)

            self.canvas.delete("all")  # Clear canvas
            self.canvas.create_image(250, 200, image=self.current_image)  # Center

            # Show dimensions
            width, height = image.size
            self.dim_label.config(text=f"Dimensions: {width} x {height}")

        except Exception as e:
            messagebox.showerror("Error", f"Cannot open image: {e}")

# === Run the app ===
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageOrganizerApp(root)
    root.mainloop()
