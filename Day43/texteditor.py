import tkinter as tk
from tkinter import filedialog, messagebox

class MiniNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Notepad")
        self.root.geometry("600x400")

        self.file_path = None

        self.create_menu()
        self.create_toolbar()
        self.create_text_area()

        # Confirm on exit
        self.root.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    # Menu Bar
    def create_menu(self):
        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.confirm_exit)
        menubar.add_cascade(label="File", menu=file_menu)

        self.root.config(menu=menubar)

    # Toolbar
    def create_toolbar(self):
        toolbar_frame = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#f0f0f0")
        toolbar_frame.pack(side="top", fill="x")

        open_btn = tk.Button(toolbar_frame, text="Open", command=self.open_file)
        open_btn.pack(side="left", padx=4, pady=4)

        save_btn = tk.Button(toolbar_frame, text="Save", command=self.save_file)
        save_btn.pack(side="left", padx=4, pady=4)

    # Text area
    def create_text_area(self):
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill="both", expand=True)

        self.text_widget = tk.Text(text_frame, wrap="word")
        self.text_widget.pack(fill="both", expand=True)

    # New file
    def new_file(self):
        if self.confirm_discard():
            self.text_widget.delete("1.0", tk.END)
            self.file_path = None
            self.root.title("Mini Notepad")

    # Open file
    def open_file(self):
        if not self.confirm_discard():
            return
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
            self.text_widget.delete("1.0", tk.END)
            self.text_widget.insert(tk.END, content)
            self.file_path = file_path
            self.root.title(f"Mini Notepad - {file_path}")

    # Save file
    def save_file(self):
        if not self.file_path:
            self.file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                          filetypes=[("Text Files", "*.txt")])
        if self.file_path:
            content = self.text_widget.get("1.0", tk.END)
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(content)
            messagebox.showinfo("Saved", "File saved successfully.")
            self.root.title(f"Mini Notepad - {self.file_path}")

    # Confirm before closing
    def confirm_exit(self):
        if self.confirm_discard():
            self.root.destroy()

    # Confirm unsaved changes
    def confirm_discard(self):
        content = self.text_widget.get("1.0", tk.END).strip()
        if content:
            return messagebox.askokcancel("Unsaved Changes", "Discard current text?")
        return True

# Run the editor
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniNotepad(root)
    root.mainloop()
