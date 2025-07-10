import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
import sqlite3
import time

DB = "recent_file.db"

class FileDialogApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Dialogs & Notepad")
        self.current_file = None

        self.setup_db()
        self.create_widgets()
        self.load_last_file()

    def setup_db(self):
        self.conn = sqlite3.connect(DB)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS recent (file TEXT)")
        self.conn.commit()

    def create_widgets(self):
        # === Menu ===
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as_file)
        filemenu.add_command(label="New", command=self.new_file)
        menubar.add_cascade(label="File", menu=filemenu)

        self.root.config(menu=menubar)

        # === Text Widget ===
        self.text = tk.Text(self.root, wrap=tk.WORD, height=20, width=60)
        self.text.pack(pady=10)

        # === Buttons ===
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Open .txt File", command=self.open_txt).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Open Image", command=self.open_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Choose Directory", command=self.choose_directory).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Load Form from .txt", command=self.load_form_from_txt).pack(side=tk.LEFT, padx=5)

        # === File Info ===
        self.file_info = tk.Label(self.root, text="File Info: N/A", anchor="w")
        self.file_info.pack(fill=tk.X, padx=10, pady=5)

        # === Image Canvas ===
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()

        # === Registration Form ===
        form_frame = tk.LabelFrame(self.root, text="Auto-Fill Form from File")
        form_frame.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(form_frame, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1)

        tk.Label(form_frame, text="Age").grid(row=1, column=0)
        self.age_entry = tk.Entry(form_frame)
        self.age_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=2, column=1)

    # === File Methods ===
    def open_txt(self):
        try:
            file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if file:
                with open(file, 'r') as f:
                    content = f.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)
                self.current_file = file
                self.set_recent(file)
                self.show_file_info(file)
        except FileNotFoundError:
            messagebox.showerror("Error", "File not found.")

    def save_file(self):
        if not self.current_file:
            self.save_as_file()
            return
        if messagebox.askyesno("Confirm", f"Overwrite {self.current_file}?"):
            with open(self.current_file, 'w') as f:
                f.write(self.text.get("1.0", tk.END))
            messagebox.showinfo("Saved", f"Saved to {self.current_file}")

    def save_as_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text File", "*.txt"),
                                                       ("CSV File", "*.csv"),
                                                       ("JSON File", "*.json")],
                                            initialfile="Untitled.txt")
        if file:
            with open(file, 'w') as f:
                f.write(self.text.get("1.0", tk.END))
            self.current_file = file
            self.set_recent(file)
            self.show_file_info(file)

    def new_file(self):
        self.text.delete("1.0", tk.END)
        self.current_file = None
        self.file_info.config(text="File Info: N/A")

    def open_file(self):
        self.open_txt()

    def open_image(self):
        file = filedialog.askopenfilename(filetypes=[("Images", "*.png;*.jpg;*.jpeg;*.gif")])
        if file:
            try:
                img = Image.open(file)
                img.thumbnail((300, 300))
                self.tk_image = ImageTk.PhotoImage(img)
                self.canvas.delete("all")
                self.canvas.create_image(150, 150, image=self.tk_image)
                self.file_info.config(text=f"Loaded image: {os.path.basename(file)}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load image: {e}")

    def choose_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.file_info.config(text=f"Directory: {folder}")

    def show_file_info(self, file):
        if os.path.exists(file):
            size = os.path.getsize(file)
            modified = time.ctime(os.path.getmtime(file))
            self.file_info.config(text=f"Size: {size} bytes | Modified: {modified}")

    def set_recent(self, file):
        self.cur.execute("DELETE FROM recent")
        self.cur.execute("INSERT INTO recent (file) VALUES (?)", (file,))
        self.conn.commit()

    def load_last_file(self):
        self.cur.execute("SELECT file FROM recent ORDER BY ROWID DESC LIMIT 1")
        row = self.cur.fetchone()
        if row and os.path.exists(row[0]):
            with open(row[0], 'r') as f:
                content = f.read()
            self.text.insert(tk.END, content)
            self.current_file = row[0]
            self.show_file_info(row[0])

    def load_form_from_txt(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            try:
                with open(file, 'r') as f:
                    lines = f.readlines()
                    if len(lines) >= 3:
                        self.name_entry.delete(0, tk.END)
                        self.name_entry.insert(0, lines[0].strip())

                        self.age_entry.delete(0, tk.END)
                        self.age_entry.insert(0, lines[1].strip())

                        self.email_entry.delete(0, tk.END)
                        self.email_entry.insert(0, lines[2].strip())
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load: {e}")

# === Run ===
if __name__ == "__main__":
    root = tk.Tk()
    app = FileDialogApp(root)
    root.mainloop()
