import os
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

class FileSearcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Searcher")

        self.folder_path = ""
        self.search_thread = None

        self.create_widgets()

    def create_widgets(self):
        # Folder selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=5, fill=tk.X, padx=5)

        tk.Label(folder_frame, text="Folder:").pack(side=tk.LEFT)
        self.folder_entry = tk.Entry(folder_frame, width=50)
        self.folder_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(folder_frame, text="Browse", command=self.browse_folder).pack(side=tk.LEFT)

        # Keyword input
        keyword_frame = tk.Frame(self.root)
        keyword_frame.pack(pady=5, fill=tk.X, padx=5)

        tk.Label(keyword_frame, text="Keyword:").pack(side=tk.LEFT)
        self.keyword_entry = tk.Entry(keyword_frame, width=30)
        self.keyword_entry.pack(side=tk.LEFT, padx=5)

        # Search button
        self.search_btn = tk.Button(keyword_frame, text="Search", command=self.start_search)
        self.search_btn.pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_label = tk.Label(self.root, text="Status: Ready")
        self.status_label.pack(pady=5)

        # Results box (ScrolledText)
        self.results_box = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.results_box.pack(padx=5, pady=5)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path = folder
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder)

    def start_search(self):
        if self.search_thread and self.search_thread.is_alive():
            messagebox.showwarning("Search Running", "A search is already in progress.")
            return

        folder = self.folder_entry.get().strip()
        keyword = self.keyword_entry.get().strip()

        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Invalid Folder", "Please select a valid folder.")
            return

        if not keyword:
            messagebox.showerror("Invalid Keyword", "Please enter a keyword to search for.")
            return

        self.results_box.delete("1.0", tk.END)
        self.status_label.config(text="Status: Searching...")
        self.search_btn.config(state=tk.DISABLED)

        self.search_thread = threading.Thread(target=self.search_files, args=(folder, keyword))
        self.search_thread.start()

    def search_files(self, folder, keyword):
        matches_found = 0
        for root, _, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(".txt"):
                    filepath = os.path.join(root, file)
                    try:
                        with open(filepath, "r", encoding="utf-8") as f:
                            for lineno, line in enumerate(f, start=1):
                                if keyword.lower() in line.lower():
                                    matches_found += 1
                                    display_text = f"{file} (Line {lineno}): {line.strip()}\n"
                                    # Schedule GUI update
                                    self.root.after(0, self.append_result, display_text)
                    except Exception as e:
                        # Could log errors here if needed
                        pass

        status_msg = f"Status: Search complete. {matches_found} matches found."
        self.root.after(0, self.search_finished, status_msg)

    def append_result(self, text):
        self.results_box.insert(tk.END, text)
        self.results_box.see(tk.END)

    def search_finished(self, status_msg):
        self.status_label.config(text=status_msg)
        self.search_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileSearcherApp(root)
    root.mainloop()
