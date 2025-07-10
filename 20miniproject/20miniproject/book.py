import tkinter as tk
from tkinter import ttk, messagebox

# Sample book titles
books = [
    "The Great Gatsby", "1984", "To Kill a Mockingbird", "Pride and Prejudice",
    "The Catcher in the Rye", "Moby Dick", "War and Peace", "The Hobbit",
    "Crime and Punishment", "The Odyssey"
]

def issue_book():
    user = user_entry.get().strip()
    book = book_combo.get()
    date = issue_date_spinbox.get()

    if not user:
        messagebox.showwarning("Input Error", "Please enter the user's name.")
        return
    if book == "":
        messagebox.showwarning("Input Error", "Please select a book title.")
        return

    record = f"User: {user} | Book: {book} | Issue Date: {date}"
    issued_listbox.insert(tk.END, record)

    # Clear user entry
    user_entry.delete(0, tk.END)

# === Main Window ===
root = tk.Tk()
root.title("Library Book Issue System")
root.geometry("600x400")
root.configure(padx=15, pady=15)

# Book selection
tk.Label(root, text="Select Book Title:").grid(row=0, column=0, sticky="w", pady=5)
book_combo = ttk.Combobox(root, values=books, state="readonly", width=40)
book_combo.grid(row=0, column=1, pady=5)
book_combo.set(books[0])

# User name entry
tk.Label(root, text="User Name:").grid(row=1, column=0, sticky="w", pady=5)
user_entry = tk.Entry(root, width=42)
user_entry.grid(row=1, column=1, pady=5)

# Issue date spinbox
tk.Label(root, text="Issue Date (1-31):").grid(row=2, column=0, sticky="w", pady=5)
issue_date_spinbox = tk.Spinbox(root, from_=1, to=31, width=5)
issue_date_spinbox.grid(row=2, column=1, sticky="w", pady=5)

# Issue book button
issue_btn = tk.Button(root, text="Issue Book", command=issue_book)
issue_btn.grid(row=3, column=0, columnspan=2, pady=15)

# Listbox and scrollbar for issued records
list_frame = tk.Frame(root)
list_frame.grid(row=4, column=0, columnspan=2, sticky="nsew")

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

issued_listbox = tk.Listbox(list_frame, width=80, height=10, yscrollcommand=scrollbar.set)
issued_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=issued_listbox.yview)

# Make rows and columns expand properly
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()
