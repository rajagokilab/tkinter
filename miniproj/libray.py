import tkinter as tk
from tkinter import ttk, messagebox

def issue_book():
    user = entry_user.get().strip()
    book = combo_books.get()
    date = spin_date.get()

    if not user:
        messagebox.showwarning("Input Error", "Please enter the user's name.")
        return
    if not book:
        messagebox.showwarning("Input Error", "Please select a book.")
        return

    record = f"User: {user} | Book: {book} | Date: {date}"
    listbox_records.insert(tk.END, record)
    entry_user.delete(0, tk.END)

root = tk.Tk()
root.title("Library Book Issue System")

# Book titles example list
books = [
    "1984 by George Orwell",
    "To Kill a Mockingbird by Harper Lee",
    "Pride and Prejudice by Jane Austen",
    "The Great Gatsby by F. Scott Fitzgerald",
    "Moby-Dick by Herman Melville",
    "War and Peace by Leo Tolstoy",
    "The Catcher in the Rye by J.D. Salinger"
]

# Widgets
tk.Label(root, text="User Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_user = tk.Entry(root, width=30)
entry_user.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Book Title:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
combo_books = ttk.Combobox(root, values=books, state="readonly", width=28)
combo_books.grid(row=1, column=1, padx=5, pady=5)
combo_books.current(0)

tk.Label(root, text="Issue Date:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
spin_date = tk.Spinbox(root, from_=1, to=31, width=5)
spin_date.grid(row=2, column=1, padx=5, pady=5, sticky="w")

btn_issue = tk.Button(root, text="Issue Book", command=issue_book)
btn_issue.grid(row=3, column=0, columnspan=2, pady=10)

# Listbox with scrollbar for issued records
frame_listbox = tk.Frame(root)
frame_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

scrollbar = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
listbox_records = tk.Listbox(frame_listbox, width=50, height=10, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_records.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_records.pack(side=tk.LEFT, fill=tk.BOTH)

root.mainloop()
