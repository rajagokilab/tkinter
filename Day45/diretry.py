import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import os
import shutil
import time

class BackupUtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Directory Backup Utility")

        self.src_dir = tk.StringVar()
        self.dst_dir = tk.StringVar()
        self.copied_count = 0
        self.total_files = 0
        self.is_running = False

        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10)

        # Source folder selection
        tk.Label(frame, text="Source Folder:").grid(row=0, column=0, sticky="w")
        tk.Entry(frame, textvariable=self.src_dir, width=40).grid(row=0, column=1)
        tk.Button(frame, text="Browse", command=self.browse_src).grid(row=0, column=2, padx=5)

        # Target folder selection
        tk.Label(frame, text="Backup Folder:").grid(row=1, column=0, sticky="w")
        tk.Entry(frame, textvariable=self.dst_dir, width=40).grid(row=1, column=1)
        tk.Button(frame, text="Browse", command=self.browse_dst).grid(row=1, column=2, padx=5)

        # Start backup button
        self.start_btn = tk.Button(frame, text="Start Backup", command=self.start_backup)
        self.start_btn.grid(row=2, column=0, columnspan=3, pady=10)

        # Status label
        self.status_label = tk.Label(root, text="Select folders to begin.")
        self.status_label.pack(pady=5)

    def browse_src(self):
        folder = filedialog.askdirectory()
        if folder:
            self.src_dir.set(folder)

    def browse_dst(self):
        folder = filedialog.askdirectory()
        if folder:
            self.dst_dir.set(folder)

    def start_backup(self):
        if self.is_running:
            messagebox.showinfo("Backup Running", "Backup is already running.")
            return

        src = self.src_dir.get()
        dst = self.dst_dir.get()

        if not os.path.isdir(src):
            messagebox.showerror("Error", "Invalid source directory.")
            return
        if not os.path.isdir(dst):
            messagebox.showerror("Error", "Invalid backup directory.")
            return
        if src == dst:
            messagebox.showerror("Error", "Source and backup folders must be different.")
            return

        self.start_btn.config(state=tk.DISABLED)
        self.copied_count = 0
        self.status_label.config(text="Starting backup...")
        self.is_running = True

        thread = threading.Thread(target=self.backup_thread, args=(src, dst), daemon=True)
        thread.start()
        self.root.after(100, self.update_status)

    def backup_thread(self, src, dst):
        txt_files = [f for f in os.listdir(src) if f.lower().endswith(".txt")]
        self.total_files = len(txt_files)
        for f in txt_files:
            if not self.is_running:
                break
            src_path = os.path.join(src, f)
            dst_path = os.path.join(dst, f)
            try:
                shutil.copy2(src_path, dst_path)
                time.sleep(0.5)  # simulate delay
                self.copied_count += 1
            except Exception as e:
                print(f"Error copying {f}: {e}")
        self.is_running = False

    def update_status(self):
        if self.is_running:
            self.status_label.config(text=f"Copied {self.copied_count} / {self.total_files} files...")
            self.root.after(200, self.update_status)
        else:
            self.status_label.config(text=f"Backup complete! {self.copied_count} files copied.")
            self.start_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x180")
    app = BackupUtilityApp(root)
    root.mainloop()
