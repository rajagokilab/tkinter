import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3

class StudentRegistrationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Registration System")
        self.db_setup()
        self.build_ui()

    def db_setup(self):
        self.conn = sqlite3.connect("students.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def build_ui(self):
        # === Entry Fields ===
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.age_entry = tk.Entry(self.root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Course:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.course_entry = tk.Entry(self.root)
        self.course_entry.grid(row=2, column=1, padx=10, pady=5)

        # === Buttons ===
        tk.Button(self.root, text="Save", width=12, command=self.save_student).grid(row=3, column=0, pady=10)
        tk.Button(self.root, text="View All", width=12, command=self.view_students).grid(row=3, column=1, pady=10)
        tk.Button(self.root, text="Export to .txt", width=26, command=self.export_to_txt).grid(row=4, column=0, columnspan=2, pady=5)

        # === Listbox for Display ===
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def save_student(self):
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        course = self.course_entry.get().strip()

        if not name or not age or not course:
            messagebox.showwarning("Validation Error", "All fields are required.")
            return

        if not age.isdigit():
            messagebox.showerror("Validation Error", "Age must be a number.")
            return

        self.cur.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, int(age), course))
        self.conn.commit()
        messagebox.showinfo("Success", "Student record saved.")

        self.clear_entries()
        self.view_students()

    def view_students(self):
        self.listbox.delete(0, tk.END)
        self.cur.execute("SELECT name, age, course FROM students")
        rows = self.cur.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, f"Name: {row[0]} | Age: {row[1]} | Course: {row[2]}")

    def export_to_txt(self):
        self.cur.execute("SELECT name, age, course FROM students")
        rows = self.cur.fetchall()
        if not rows:
            messagebox.showwarning("No Data", "There are no student records to export.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")],
                                                 initialfile="students.txt")
        if file_path:
            with open(file_path, "w") as file:
                for row in rows:
                    file.write(f"Name: {row[0]}, Age: {row[1]}, Course: {row[2]}\n")
            messagebox.showinfo("Exported", f"Data exported to {file_path}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.course_entry.delete(0, tk.END)

# === Launch App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRegistrationApp(root)
    root.mainloop()
