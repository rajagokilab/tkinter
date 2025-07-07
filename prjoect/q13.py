import tkinter as tk
from tkinter import ttk, filedialog, messagebox

class SimpleTextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📝 Basic Text Editor")
        self.geometry("500x400")
        self.resizable(False, False)  # Disable resizing

        # -------- Text widget --------
        self.text_widget = tk.Text(self, wrap="word")
        self.text_widget.pack(expand=True, fill="both", padx=10, pady=(10, 0))

        # Insert sample content
        sample_text = (
            "Welcome to your simple text editor!\n\n"
            "You can write your notes here.\n"
            "Use the buttons below to Save or Clear your text.\n"
        )
        self.text_widget.insert("1.0", sample_text)

        # -------- Bottom Frame for buttons and status --------
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(fill="x", padx=10, pady=10)

        # Save button
        save_btn = ttk.Button(bottom_frame, text="Save", command=self.save_file)
        save_btn.pack(side="left", padx=(0, 10))

        # Clear button
        clear_btn = ttk.Button(bottom_frame, text="Clear", command=self.clear_text)
        clear_btn.pack(side="left")

        # Character and word count label
        self.status_label = ttk.Label(bottom_frame, text="Chars: 0 | Words: 0")
        self.status_label.pack(side="right")

        # Bind key release to update counts dynamically
        self.text_widget.bind("<KeyRelease>", self.update_counts)

        # Initialize counts
        self.update_counts()

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
            title="Save As"
        )
        if file_path:
            try:
                content = self.text_widget.get("1.0", tk.END)
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("Saved", "File saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file:\n{e}")

    def clear_text(self):
        if messagebox.askyesno("Clear Text", "Are you sure you want to clear all text?"):
            self.text_widget.delete("1.0", tk.END)
            self.update_counts()

    def update_counts(self, event=None):
        text = self.text_widget.get("1.0", tk.END).strip()
        char_count = len(text)
        word_count = len(text.split()) if text else 0
        self.status_label.config(text=f"Chars: {char_count} | Words: {word_count}")

if __name__ == "__main__":
    SimpleTextEditor().mainloop()
