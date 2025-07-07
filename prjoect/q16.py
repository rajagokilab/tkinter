import tkinter as tk
from tkinter import ttk

class LiveCharCounter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⌨️ Live Character Counter")
        self.geometry("450x300")
        self.resizable(False, False)

        # Text widget
        self.text_area = tk.Text(self, wrap="word", font=("Arial", 12))
        self.text_area.place(x=20, y=20, width=410, height=180)
        self.text_area.bind("<Key>", self.update_count)

        # Count Label
        self.count_label = ttk.Label(self, text="Chars: 0 | Words: 0", font=("Arial", 12))
        self.count_label.place(x=20, y=210)

        # Clear Button
        clear_btn = ttk.Button(self, text="Clear", command=self.clear_text)
        clear_btn.place(x=300, y=210, width=60)

        # Reset Button
        reset_btn = ttk.Button(self, text="Reset", command=self.reset_all)
        reset_btn.place(x=370, y=210, width=60)

    def update_count(self, event=None):
        text = self.text_area.get("1.0", "end-1c")
        chars = len(text)
        words = len(text.split()) if text.strip() else 0
        self.count_label.config(text=f"Chars: {chars} | Words: {words}")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)
        self.update_count()

    def reset_all(self):
        self.clear_text()
        # If you want to reset count explicitly (though it's already updated)
        self.count_label.config(text="Chars: 0 | Words: 0")

if __name__ == "__main__":
    LiveCharCounter().mainloop()
