import tkinter as tk
from tkinter import filedialog, messagebox

class FilePreviewWordCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("File Preview and Word Counter")

        # Text widget with scrollbar
        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.text = tk.Text(frame, wrap=tk.WORD)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.text.bind("<<Modified>>", self.on_text_change)

        scrollbar = tk.Scrollbar(frame, command=self.text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text.config(yscrollcommand=scrollbar.set)

        # Stats labels
        stats_frame = tk.Frame(root)
        stats_frame.pack(padx=10, pady=5)

        self.words_label = tk.Label(stats_frame, text="Words: 0")
        self.words_label.pack(side=tk.LEFT, padx=10)

        self.lines_label = tk.Label(stats_frame, text="Lines: 0")
        self.lines_label.pack(side=tk.LEFT, padx=10)

        self.chars_label = tk.Label(stats_frame, text="Chars: 0")
        self.chars_label.pack(side=tk.LEFT, padx=10)

        # Open File button
        open_btn = tk.Button(root, text="Open File", command=self.open_file)
        open_btn.pack(pady=5)

    def open_file(self):
        filepath = filedialog.askopenfilename(
            title="Open Text File",
            filetypes=[("Text Files", "*.txt")]
        )
        if not filepath:
            return

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            self.text.delete("1.0", tk.END)
            self.text.insert(tk.END, content)
            self.update_stats()
            self.text.edit_modified(False)  # reset modified flag
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file:\n{e}")

    def on_text_change(self, event):
        if self.text.edit_modified():
            self.update_stats()
            self.text.edit_modified(False)

    def update_stats(self):
        text = self.text.get("1.0", "end-1c")
        words = len(text.split())
        lines = int(self.text.index('end-1c').split('.')[0])
        chars = len(text)
        self.words_label.config(text=f"Words: {words}")
        self.lines_label.config(text=f"Lines: {lines}")
        self.chars_label.config(text=f"Chars: {chars}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x400")
    app = FilePreviewWordCounter(root)
    root.mainloop()
