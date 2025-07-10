import tkinter as tk
from tkinter import ttk
import threading
import time

class BackgroundTaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Task Notifier")
        self.create_widgets()

    def create_widgets(self):
        self.start_btn = tk.Button(self.root, text="Start Task", command=self.start_task)
        self.start_btn.pack(pady=10)

        self.progress_label = tk.Label(self.root, text="Progress: Not started")
        self.progress_label.pack(pady=10)

        self.progress_bar = ttk.Progressbar(self.root, length=300, mode='determinate')
        self.progress_bar.pack(pady=10)

    def start_task(self):
        self.start_btn.config(state="disabled")
        thread = threading.Thread(target=self.background_task)
        thread.start()

    def background_task(self):
        for i in range(1, 11):
            time.sleep(0.5)  # Simulate work
            progress_text = f"Progress: {i*10}%"
            self.root.after(0, self.update_ui, progress_text, i * 10)

        # Final completion message
        self.root.after(0, self.task_complete)

    def update_ui(self, text, percent):
        self.progress_label.config(text=text)
        self.progress_bar["value"] = percent

    def task_complete(self):
        self.progress_label.config(text="✅ Task Complete!")
        self.start_btn.config(state="normal")

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundTaskApp(root)
    root.mainloop()
