import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import os

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("700x400")

        self.current_path = os.path.expanduser("~")

        self.create_menu()
        self.create_toolbar()
        self.create_panes()

        self.load_directories()
        self.load_files()

    # 1. Menu Bar
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_folder)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    # 2. Toolbar
    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#e0e0e0")
        toolbar.pack(side="top", fill="x")

        tk.Button(toolbar, text="Refresh", command=self.refresh).pack(side="left", padx=4, pady=4)
        tk.Button(toolbar, text="Open Folder", command=self.open_folder).pack(side="left", padx=4, pady=4)

    # 3. PanedWindow (directory tree + file list)
    def create_panes(self):
        paned = tk.PanedWindow(self.root, sashrelief=tk.RAISED)
        paned.pack(fill="both", expand=True)

        # Left: Directory list
        self.dir_listbox = tk.Listbox(paned, width=30)
        self.dir_listbox.bind("<<ListboxSelect>>", self.on_dir_select)
        paned.add(self.dir_listbox)

        # Right: File list
        self.file_listbox = tk.Listbox(paned)
        paned.add(self.file_listbox)

    # Load directories in current path
    def load_directories(self):
        self.dir_listbox.delete(0, tk.END)
        try:
            for item in os.listdir(self.current_path):
                full_path = os.path.join(self.current_path, item)
                if os.path.isdir(full_path):
                    self.dir_listbox.insert(tk.END, item)
        except PermissionError:
            messagebox.showinfo("Access Denied", "Cannot access this folder.")

    # Load files in current path
    def load_files(self):
        self.file_listbox.delete(0, tk.END)
        try:
            for item in os.listdir(self.current_path):
                full_path = os.path.join(self.current_path, item)
                if os.path.isfile(full_path):
                    self.file_listbox.insert(tk.END, item)
        except PermissionError:
            messagebox.showinfo("Access Denied", "Cannot access this folder.")

    # Directory selection handler
    def on_dir_select(self, event):
        selection = self.dir_listbox.curselection()
        if selection:
            selected_folder = self.dir_listbox.get(selection[0])
            next_path = os.path.join(self.current_path, selected_folder)
            if os.path.isdir(next_path):
                self.current_path = next_path
                self.load_directories()
                self.load_files()

    # Refresh current directory
    def refresh(self):
        msg = messagebox.askquestion("Refresh", "Reload current folder contents?")
        if msg == "yes":
            self.load_directories()
            self.load_files()

    # Open a new folder
    def open_folder(self):
        new_path = filedialog.askdirectory(initialdir=self.current_path)
        if new_path:
            self.current_path = new_path
            self.load_directories()
            self.load_files()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FileManagerApp(root)
    root.mainloop()
