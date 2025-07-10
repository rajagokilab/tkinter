import tkinter as tk
from tkinter import messagebox, filedialog

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Notepad")
        self.filename = None
        self.text_changed = False

        self.text = tk.Text(root, undo=True)
        self.text.pack(fill=tk.BOTH, expand=True)

        self.text.bind("<<Modified>>", self.on_text_changed)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Menu
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.save_file)
        menubar.add_cascade(label="File", menu=filemenu)
        root.config(menu=menubar)

    def on_text_changed(self, event=None):
        if self.text.edit_modified():
            self.text_changed = True
            self.text.edit_modified(False)

    def save_file(self):
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if not self.filename:
                return False
        try:
            with open(self.filename, "w", encoding="utf-8") as f:
                content = self.text.get(1.0, tk.END)
                f.write(content)
            self.text_changed = False
            self.root.title(f"{self.filename} - Notepad")
            return True
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save file: {e}")
            return False

    def on_close(self):
        if self.text_changed:
            answer = messagebox.askyesnocancel("Save Changes",
                "You have unsaved changes. Save before exiting?")
            if answer is True:
                if self.save_file():
                    self.root.destroy()
            elif answer is False:
                self.root.destroy()
            # else cancel: do nothing
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.geometry("600x400")
    root.mainloop()
