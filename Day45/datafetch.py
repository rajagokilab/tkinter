import tkinter as tk
import threading
import time

class DataFetcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Background Data Fetcher")

        self.label = tk.Label(root, text="Click fetch to get data")
        self.label.pack(pady=20)

        self.fetch_btn = tk.Button(root, text="Fetch Data", command=self.start_fetch)
        self.fetch_btn.pack(pady=10)

    def start_fetch(self):
        self.fetch_btn.config(state=tk.DISABLED)
        self.label.config(text="Fetching...")
        thread = threading.Thread(target=self.fake_api_fetch)
        thread.start()

    def fake_api_fetch(self):
        # Simulate network delay
        time.sleep(3)
        data = "Data fetched successfully!"

        # Use after() to update GUI safely from thread
        self.root.after(0, self.update_label, data)

    def update_label(self, data):
        self.label.config(text=data)
        self.fetch_btn.config(state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    app = DataFetcherApp(root)
    root.mainloop()
