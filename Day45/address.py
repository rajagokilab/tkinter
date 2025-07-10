import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class AddressBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("SQLite Address Book")

        self.setup_db()
        self.create_widgets()
        self.load_contacts()

    def setup_db(self):
        self.conn = sqlite3.connect("address_book.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT,
                phone TEXT
            )
        """)
        self.conn.commit()

    def create_widgets(self):
        # === Input Fields ===
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name").grid(row=0, column=0, padx=5)
        self.name_entry = tk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, padx=5)

        tk.Label(form_frame, text="Email").grid(row=1, column=0, padx=5)
        self.email_entry = tk.Entry(form_frame, width=30)
        self.email_entry.grid(row=1, column=1, padx=5)

        tk.Label(form_frame, text="Phone").grid(row=2, column=0, padx=5)
        self.phone_entry = tk.Entry(form_frame, width=30)
        self.phone_entry.grid(row=2, column=1, padx=5)

        # === Buttons ===
        btn_frame = tk.Frame(self.root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add", width=12, command=self.add_contact).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Update", width=12, command=self.update_contact).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Delete", width=12, command=self.delete_contact).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Search", width=12, command=self.search_contacts).grid(row=0, column=3, padx=5)
        tk.Button(btn_frame, text="Clear", width=12, command=self.clear_fields).grid(row=0, column=4, padx=5)

        # === Listbox for Results ===
        self.listbox = tk.Listbox(self.root, width=80, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind('<<ListboxSelect>>', self.load_selected_contact)

    def load_contacts(self):
        self.listbox.delete(0, tk.END)
        self.cur.execute("SELECT * FROM contacts ORDER BY name")
        rows = self.cur.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, f"{row[0]}: {row[1]} | {row[2]} | {row[3]}")

    def add_contact(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name:
            messagebox.showwarning("Validation Error", "Name is required.")
            return

        self.cur.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        self.conn.commit()
        self.load_contacts()
        self.clear_fields()

    def update_contact(self):
        selected = self.get_selected_contact_id()
        if selected is None:
            return

        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()
        phone = self.phone_entry.get().strip()

        if not name:
            messagebox.showwarning("Validation Error", "Name is required.")
            return

        self.cur.execute("UPDATE contacts SET name=?, email=?, phone=? WHERE id=?",
                         (name, email, phone, selected))
        self.conn.commit()
        self.load_contacts()
        self.clear_fields()

    def delete_contact(self):
        selected = self.get_selected_contact_id()
        if selected is None:
            return

        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this contact?")
        if confirm:
            self.cur.execute("DELETE FROM contacts WHERE id=?", (selected,))
            self.conn.commit()
            self.load_contacts()
            self.clear_fields()

    def search_contacts(self):
        search_term = self.name_entry.get().strip()
        query = f"%{search_term}%"
        self.cur.execute("SELECT * FROM contacts WHERE name LIKE ? OR email LIKE ? OR phone LIKE ?",
                         (query, query, query))
        results = self.cur.fetchall()

        self.listbox.delete(0, tk.END)
        for row in results:
            self.listbox.insert(tk.END, f"{row[0]}: {row[1]} | {row[2]} | {row[3]}")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.listbox.selection_clear(0, tk.END)

    def load_selected_contact(self, event):
        if not self.listbox.curselection():
            return
        index = self.listbox.curselection()[0]
        line = self.listbox.get(index)
        contact_id = int(line.split(":")[0])

        self.cur.execute("SELECT * FROM contacts WHERE id=?", (contact_id,))
        row = self.cur.fetchone()
        if row:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, row[1])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, row[2])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, row[3])

    def get_selected_contact_id(self):
        if not self.listbox.curselection():
            messagebox.showinfo("No Selection", "Please select a contact from the list.")
            return None
        line = self.listbox.get(self.listbox.curselection()[0])
        return int(line.split(":")[0])

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AddressBookApp(root)
    root.mainloop()
