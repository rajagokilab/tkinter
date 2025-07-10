import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import random

class RealTimeLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Logger")

        self.text_area = scrolledtext.ScrolledText(root, width=60, height=20, state=tk.DISABLED)
        self.text_area.pack(padx=10, pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.start_btn = tk.Button(btn_frame, text="Start Logging", command=self.start_logging)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop Logging", command=self.stop_logging, state=tk.DISABLED)
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.logging = False
        self.log_thread = None

    def start_logging(self):
        if not self.logging:
            self.logging = True
            self.start_btn.config(state=tk.DISABLED)
            self.stop_btn.config(state=tk.NORMAL)
            self.log_thread = threading.Thread(target=self.generate_logs, daemon=True)
            self.log_thread.start()

    def stop_logging(self):
        if self.logging:
            self.logging = False
            self.start_btn.config(state=tk.NORMAL)
            self.stop_btn.config(state=tk.DISABLED)

    def generate_logs(self):
        while self.logging:
            log_msg = f"[{time.strftime('%H:%M:%S')}] Log entry: Event {random.randint(1000,9999)} occurred.\n"
            self.root.after(0, self.append_log, log_msg)
            time.sleep(1)

    def append_log(self, msg):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, msg)
        self.text_area.see(tk.END)
        self.text_area.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeLoggerApp(root)
    root.mainloop()
