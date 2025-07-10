import tkinter as tk
from tkinter import filedialog, messagebox
import os

class TextFileEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text File Editor")
        self.current_file = None

        self.create_widgets()

    def create_widgets(self):
        # === Menu ===
        menubar = tk.Menu(self.root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        filemenu.add_command(label="Save", command=self.save_file)
        filemenu.add_command(label="Save As", command=self.save_as_file)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        self.root.config(menu=menubar)

        # === Text Editor ===
        self.text = tk.Text(self.root, wrap=tk.WORD, undo=True)
        self.text.pack(expand=True, fill=tk.BOTH)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text.delete("1.0", tk.END)
                self.text.insert(tk.END, content)
                self.current_file = file_path
                self.update_title()
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file: {e}")

    def save_file(self):
        if self.current_file:
            try:
                with open(self.current_file, "w") as file:
                    file.write(self.text.get("1.0", tk.END))
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        else:
            self.save_as_file()

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            initialfile="untitled.txt"
        )
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text.get("1.0", tk.END))
                self.current_file = file_path
                self.update_title()
                messagebox.showinfo("Saved", "File saved successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")

    def update_title(self):
        filename = os.path.basename(self.current_file) if self.current_file else "Untitled"
        self.root.title(f"{filename} - Text File Editor")

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = TextFileEditor(root)
    root.mainloop()
