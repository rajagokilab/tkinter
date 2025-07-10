import tkinter as tk
from tkinter import messagebox
import sqlite3

class BookManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Library Manager")

        self.conn = sqlite3.connect("library.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                year INTEGER NOT NULL
            )
        """)
        self.conn.commit()

        self.selected_id = None
        self.create_widgets()
        self.load_books()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Author
        tk.Label(frame, text="Author:").grid(row=0, column=0, sticky="w")
        self.author_entry = tk.Entry(frame, width=30)
        self.author_entry.grid(row=0, column=1)

        # Title
        tk.Label(frame, text="Title:").grid(row=1, column=0, sticky="w")
        self.title_entry = tk.Entry(frame, width=30)
        self.title_entry.grid(row=1, column=1)

        # Year
        tk.Label(frame, text="Year:").grid(row=2, column=0, sticky="w")
        self.year_entry = tk.Entry(frame, width=30)
        self.year_entry.grid(row=2, column=1)

        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add Book", command=self.add_book, width=12)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.update_btn = tk.Button(btn_frame, text="Update Book", command=self.update_book, width=12, state=tk.DISABLED)
        self.update_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Delete Book", command=self.delete_book, width=12, state=tk.DISABLED)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        # Listbox + Scrollbar
        list_frame = tk.Frame(self.root)
        list_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.book_listbox = tk.Listbox(list_frame, height=10)
        self.book_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.book_listbox.bind('<<ListboxSelect>>', self.on_select)

        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.book_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.book_listbox.config(yscrollcommand=scrollbar.set)

    def load_books(self):
        self.book_listbox.delete(0, tk.END)
        self.cur.execute("SELECT id, author, title, year FROM books ORDER BY id DESC")
        self.books = self.cur.fetchall()
        for _, author, title, year in self.books:
            self.book_listbox.insert(tk.END, f"{title} by {author} ({year})")
        self.clear_form()

    def clear_form(self):
        self.selected_id = None
        self.author_entry.delete(0, tk.END)
        self.title_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.add_btn.config(state=tk.NORMAL)
        self.update_btn.config(state=tk.DISABLED)
        self.delete_btn.config(state=tk.DISABLED)

    def on_select(self, event):
        if not self.book_listbox.curselection():
            return
        idx = self.book_listbox.curselection()[0]
        book = self.books[idx]
        self.selected_id = book[0]
        self.author_entry.delete(0, tk.END)
        self.author_entry.insert(0, book[1])
        self.title_entry.delete(0, tk.END)
        self.title_entry.insert(0, book[2])
        self.year_entry.delete(0, tk.END)
        self.year_entry.insert(0, book[3])
        self.add_btn.config(state=tk.DISABLED)
        self.update_btn.config(state=tk.NORMAL)
        self.delete_btn.config(state=tk.NORMAL)

    def add_book(self):
        author = self.author_entry.get().strip()
        title = self.title_entry.get().strip()
        year = self.year_entry.get().strip()
        if not author or not title or not year:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
        if not year.isdigit():
            messagebox.showwarning("Input Error", "Year must be a number.")
            return
        self.cur.execute("INSERT INTO books (author, title, year) VALUES (?, ?, ?)", (author, title, int(year)))
        self.conn.commit()
        self.load_books()

    def update_book(self):
        if self.selected_id is None:
            return
        author = self.author_entry.get().strip()
        title = self.title_entry.get().strip()
        year = self.year_entry.get().strip()
        if not author or not title or not year:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
        if not year.isdigit():
            messagebox.showwarning("Input Error", "Year must be a number.")
            return
        self.cur.execute(
            "UPDATE books SET author=?, title=?, year=? WHERE id=?",
            (author, title, int(year), self.selected_id)
        )
        self.conn.commit()
        self.load_books()

    def delete_book(self):
        if self.selected_id is None:
            return
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this book?"):
            self.cur.execute("DELETE FROM books WHERE id=?", (self.selected_id,))
            self.conn.commit()
            self.load_books()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x350")
    app = BookManager(root)
    root.mainloop()
