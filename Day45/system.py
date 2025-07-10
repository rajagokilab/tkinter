import tkinter as tk
import threading
import time
import psutil 

class SystemInfoViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("System Info Viewer")

        self.label = tk.Label(root, text="CPU Usage: --%", font=("Arial", 24))
        self.label.pack(padx=20, pady=20)

        self.running = True
        self.cpu_usage = 0

        self.thread = threading.Thread(target=self.update_cpu_usage, daemon=True)
        self.thread.start()

        self.update_label()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def update_cpu_usage(self):
        while self.running:
            self.cpu_usage = psutil.cpu_percent(interval=1)
            # Sleep not needed here since cpu_percent already waits 1 sec

    def update_label(self):
        self.label.config(text=f"CPU Usage: {self.cpu_usage}%")
        if self.running:
            self.root.after(1000, self.update_label)

    def on_close(self):
        self.running = False
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x100")
    app = SystemInfoViewer(root)
    root.mainloop()
