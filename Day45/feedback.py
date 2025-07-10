import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import threading
import time

class FeedbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Feedback Collector")

        self.conn = sqlite3.connect("feedback.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                rating INTEGER,
                comments TEXT
            )
        """)
        self.conn.commit()

        self.create_widgets()
        self.load_feedback()

    def create_widgets(self):
        frm = tk.Frame(self.root)
        frm.pack(padx=10, pady=10)

        # Name
        tk.Label(frm, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(frm, width=30)
        self.name_entry.grid(row=0, column=1, pady=2)

        # Rating
        tk.Label(frm, text="Rating (1-5):").grid(row=1, column=0, sticky="w")
        self.rating_combo = ttk.Combobox(frm, values=[1,2,3,4,5], width=5, state="readonly")
        self.rating_combo.grid(row=1, column=1, sticky="w", pady=2)
        self.rating_combo.current(4)  # default 5

        # Comments
        tk.Label(frm, text="Comments:").grid(row=2, column=0, sticky="nw")
        self.comments_text = tk.Text(frm, width=40, height=5)
        self.comments_text.grid(row=2, column=1, pady=2)

        # Submit button
        self.submit_btn = tk.Button(frm, text="Submit Feedback", command=self.submit_feedback)
        self.submit_btn.grid(row=3, column=0, columnspan=2, pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

        # Feedback Listbox
        tk.Label(self.root, text="All Feedback:").pack()
        self.listbox = tk.Listbox(self.root, width=70, height=10)
        self.listbox.pack(padx=10, pady=5)

    def submit_feedback(self):
        name = self.name_entry.get().strip()
        rating = self.rating_combo.get()
        comments = self.comments_text.get("1.0", tk.END).strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        if not rating:
            messagebox.showwarning("Input Error", "Please select a rating.")
            return

        self.submit_btn.config(state=tk.DISABLED)
        self.status_label.config(text="Submitting feedback...")

        # Run DB insert in separate thread (simulate delay)
        threading.Thread(target=self.save_feedback_thread, args=(name, int(rating), comments), daemon=True).start()

    def save_feedback_thread(self, name, rating, comments):
        time.sleep(2)  # simulate delay
        try:
            self.cur.execute("INSERT INTO feedback (name, rating, comments) VALUES (?, ?, ?)",
                             (name, rating, comments))
            self.conn.commit()
            self.root.after(0, self.on_feedback_saved)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("DB Error", f"Error saving feedback: {e}"))

    def on_feedback_saved(self):
        self.status_label.config(text="Feedback submitted successfully!")
        self.submit_btn.config(state=tk.NORMAL)
        self.name_entry.delete(0, tk.END)
        self.rating_combo.current(4)
        self.comments_text.delete("1.0", tk.END)
        self.load_feedback()

    def load_feedback(self):
        self.listbox.delete(0, tk.END)
        self.cur.execute("SELECT name, rating, comments FROM feedback ORDER BY id DESC")
        for name, rating, comments in self.cur.fetchall():
            display = f"{name} (Rating: {rating}): {comments}"
            self.listbox.insert(tk.END, display)

if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()
