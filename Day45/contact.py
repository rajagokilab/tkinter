import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3
import csv
import re

class ContactImporter:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact CSV Importer")

        self.conn = sqlite3.connect("contacts.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE,
                phone TEXT
            )
        """)
        self.conn.commit()

        self.import_btn = tk.Button(root, text="Import Contacts from CSV", command=self.import_csv)
        self.import_btn.pack(padx=10, pady=10)

        self.status_label = tk.Label(root, text="")
        self.status_label.pack(padx=10, pady=5)

    def validate_email(self, email):
        # Simple regex for email validation
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def import_csv(self):
        filepath = filedialog.askopenfilename(
            title="Select CSV file",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not filepath:
            self.status_label.config(text="Import cancelled.")
            return

        inserted = 0
        errors = 0
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row.get("name") or row.get("Name")
                email = row.get("email") or row.get("Email")
                phone = row.get("phone") or row.get("Phone")

                if not name or not email:
                    errors += 1
                    continue

                if not self.validate_email(email):
                    errors += 1
                    continue

                try:
                    self.cur.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
                                     (name.strip(), email.strip(), phone.strip() if phone else None))
                    self.conn.commit()
                    inserted += 1
                except sqlite3.IntegrityError:
                    # Duplicate email, skip
                    errors += 1
                except Exception:
                    errors += 1

        msg = f"Import complete: {inserted} inserted, {errors} skipped."
        self.status_label.config(text=msg)
        messagebox.showinfo("Import Results", msg)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x120")
    app = ContactImporter(root)
    root.mainloop()
