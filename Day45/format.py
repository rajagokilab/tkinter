import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time

class DownloadSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Download Simulator")

        self.progress = ttk.Progressbar(root, length=300, maximum=100)
        self.progress.pack(pady=20)

        btn_frame = tk.Frame(root)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start Download", command=self.start_download)
        self.start_btn.pack(side=tk.LEFT, padx=10)

        self.cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.cancel_download, state=tk.DISABLED)
        self.cancel_btn.pack(side=tk.LEFT, padx=10)

        self.is_downloading = False
        self.thread = None

    def start_download(self):
        if self.is_downloading:
            return
        self.is_downloading = True
        self.progress["value"] = 0
        self.start_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.thread = threading.Thread(target=self.download_task, daemon=True)
        self.thread.start()
        self.update_progress()

    def download_task(self):
        for i in range(101):
            if not self.is_downloading:
                break
            time.sleep(0.05)  # simulate download delay
            self.progress_value = i
        self.is_downloading = False

    def update_progress(self):
        self.progress["value"] = getattr(self, "progress_value", 0)
        if self.is_downloading:
            self.root.after(100, self.update_progress)
        else:
            self.start_btn.config(state=tk.NORMAL)
            self.cancel_btn.config(state=tk.DISABLED)
            if self.progress["value"] == 100:
                messagebox.showinfo("Download Simulator", "Download completed!")
            else:
                messagebox.showinfo("Download Simulator", "Download canceled.")

    def cancel_download(self):
        if self.is_downloading:
            self.is_downloading = False

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x120")
    app = DownloadSimulator(root)
    root.mainloop()
