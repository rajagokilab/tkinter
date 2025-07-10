import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import csv
import os

DB_NAME = "students.db"

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Database Manager")

        self.setup_db()
        self.create_widgets()
        self.load_names()
        self.update_student_count()

    def setup_db(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER,
                grade TEXT,
                email TEXT UNIQUE
            )
        """)
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        self.conn.commit()

    def create_widgets(self):
        # === Entry Form ===
        tk.Label(self.root, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Age").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Grade").grid(row=2, column=0)
        self.grade_entry = tk.Entry(self.root)
        self.grade_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Email").grid(row=3, column=0)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=3, column=1)

        tk.Button(self.root, text="Save", command=self.save_record).grid(row=4, column=0)
        tk.Button(self.root, text="View All", command=self.view_records).grid(row=4, column=1)
        tk.Button(self.root, text="Clear", command=self.clear_fields).grid(row=4, column=2)

        # === Update/Delete Section ===
        tk.Label(self.root, text="Select Student").grid(row=5, column=0)
        self.select_combo = ttk.Combobox(self.root, state="readonly")
        self.select_combo.grid(row=5, column=1)
        self.select_combo.bind("<<ComboboxSelected>>", self.fill_selected)

        tk.Button(self.root, text="Update", command=self.update_record).grid(row=6, column=0)
        tk.Button(self.root, text="Delete", command=self.delete_record).grid(row=6, column=1)

        # === Search ===
        tk.Label(self.root, text="Search Name").grid(row=7, column=0)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.grid(row=7, column=1)
        tk.Button(self.root, text="Search", command=self.search_student).grid(row=7, column=2)

        # === Info ===
        self.status_label = tk.Label(self.root, text="Status: Ready")
        self.status_label.grid(row=8, column=0, columnspan=3)

        self.count_label = tk.Label(self.root, text="Total Students: 0")
        self.count_label.grid(row=9, column=0, columnspan=3)

        # === Text View ===
        self.view_box = tk.Text(self.root, width=60, height=10)
        self.view_box.grid(row=10, column=0, columnspan=3, pady=5)

        # === File Options ===
        tk.Button(self.root, text="Insert Dummy Data", command=self.insert_dummy).grid(row=11, column=0)
        tk.Button(self.root, text="Export to .txt", command=self.export_txt).grid(row=11, column=1)
        tk.Button(self.root, text="Import .csv", command=self.import_csv).grid(row=11, column=2)

    def save_record(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        grade = self.grade_entry.get()
        email = self.email_entry.get()
        try:
            self.cur.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                             (name, age, grade, email))
            self.conn.commit()
            self.status_label.config(text="Record Saved!")
            self.clear_fields()
            self.load_names()
            self.update_student_count()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Duplicate email. Use a different one.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.grade_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def view_records(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        self.view_box.delete(1.0, tk.END)
        for row in rows:
            self.view_box.insert(tk.END, f"{row}\n")

    def delete_record(self):
        name = self.select_combo.get()
        if not name:
            return
        if messagebox.askyesno("Confirm", f"Delete record for {name}?"):
            self.cur.execute("DELETE FROM students WHERE name = ?", (name,))
            self.conn.commit()
            self.status_label.config(text=f"Deleted {name}")
            self.load_names()
            self.update_student_count()

    def update_record(self):
        name = self.select_combo.get()
        if not name:
            return
        new_name = self.name_entry.get()
        age = self.age_entry.get()
        grade = self.grade_entry.get()
        email = self.email_entry.get()
        try:
            self.cur.execute("UPDATE students SET name=?, age=?, grade=?, email=? WHERE name=?",
                             (new_name, age, grade, email, name))
            self.conn.commit()
            self.status_label.config(text=f"Updated {name}")
            self.load_names()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Email already exists!")

    def fill_selected(self, event):
        selected = self.select_combo.get()
        self.cur.execute("SELECT name, age, grade, email FROM students WHERE name = ?", (selected,))
        row = self.cur.fetchone()
        if row:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, row[0])
            self.age_entry.delete(0, tk.END)
            self.age_entry.insert(0, row[1])
            self.grade_entry.delete(0, tk.END)
            self.grade_entry.insert(0, row[2])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, row[3])

    def load_names(self):
        self.cur.execute("SELECT name FROM students")
        names = [r[0] for r in self.cur.fetchall()]
        self.select_combo["values"] = names

    def search_student(self):
        query = self.search_entry.get()
        self.cur.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + query + '%',))
        results = self.cur.fetchall()
        self.view_box.delete(1.0, tk.END)
        for r in results:
            self.view_box.insert(tk.END, f"{r}\n")

    def update_student_count(self):
        self.cur.execute("SELECT COUNT(*) FROM students")
        count = self.cur.fetchone()[0]
        self.count_label.config(text=f"Total Students: {count}")

    def insert_dummy(self):
        for i in range(1, 21):
            try:
                self.cur.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                                 (f"Student{i}", 18 + i % 5, f"A{i % 3 + 1}", f"student{i}@mail.com"))
            except sqlite3.IntegrityError:
                continue
        self.conn.commit()
        self.load_names()
        self.update_student_count()
        self.view_records()

    def export_txt(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if not path:
            return
        self.cur.execute("SELECT * FROM students")
        records = self.cur.fetchall()
        with open(path, "w") as f:
            for row in records:
                f.write(str(row) + "\n")
        messagebox.showinfo("Export", f"Records exported to {path}")

    def import_csv(self):
        path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not path:
            return
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    self.cur.execute("INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)",
                                     (row['name'], row['age'], row['grade'], row['email']))
                except sqlite3.IntegrityError:
                    continue
        self.conn.commit()
        self.status_label.config(text="CSV Import Complete")
        self.load_names()
        self.update_student_count()
        self.view_records()

# Run
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
