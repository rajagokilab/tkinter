import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.conn = sqlite3.connect("expenses.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                amount REAL NOT NULL
            )
        """)
        self.conn.commit()

        self.selected_id = None

        self.create_widgets()
        self.load_categories()
        self.load_expenses()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Category:").grid(row=0, column=0, sticky="w")
        self.category_var = tk.StringVar()
        self.category_entry = ttk.Combobox(frame, textvariable=self.category_var, values=[], width=20)
        self.category_entry.grid(row=0, column=1, sticky="w")

        tk.Label(frame, text="Amount:").grid(row=1, column=0, sticky="w")
        self.amount_entry = tk.Entry(frame)
        self.amount_entry.grid(row=1, column=1, sticky="w")

        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.add_btn = tk.Button(btn_frame, text="Add", width=10, command=self.add_expense)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        self.update_btn = tk.Button(btn_frame, text="Update", width=10, command=self.update_expense, state=tk.DISABLED)
        self.update_btn.pack(side=tk.LEFT, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Delete", width=10, command=self.delete_expense, state=tk.DISABLED)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        # Filter section
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(padx=10, pady=5, fill=tk.X)

        tk.Label(filter_frame, text="Filter by Category:").pack(side=tk.LEFT)
        self.filter_var = tk.StringVar()
        self.filter_combo = ttk.Combobox(filter_frame, textvariable=self.filter_var, values=[], width=20)
        self.filter_combo.pack(side=tk.LEFT, padx=5)
        self.filter_combo.bind("<<ComboboxSelected>>", lambda e: self.load_expenses())

        tk.Button(filter_frame, text="Clear Filter", command=self.clear_filter).pack(side=tk.LEFT, padx=5)
        tk.Button(filter_frame, text="Export Report", command=self.export_report).pack(side=tk.RIGHT)

        # Listbox and scrollbar
        list_frame = tk.Frame(self.root)
        list_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

        self.expense_list = tk.Listbox(list_frame, height=10)
        self.expense_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.expense_list.bind('<<ListboxSelect>>', self.on_select)

        scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.expense_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.expense_list.config(yscrollcommand=scrollbar.set)

        # Total label
        self.total_label = tk.Label(self.root, text="Total: $0.00", font=("Arial", 12, "bold"))
        self.total_label.pack(pady=5)

    def load_categories(self):
        self.cur.execute("SELECT DISTINCT category FROM expenses")
        cats = [row[0] for row in self.cur.fetchall()]
        self.category_entry['values'] = cats
        self.filter_combo['values'] = [""] + cats  # "" for no filter

    def load_expenses(self):
        self.expense_list.delete(0, tk.END)
        cat_filter = self.filter_var.get().strip()
        if cat_filter:
            self.cur.execute("SELECT id, category, amount FROM expenses WHERE category=? ORDER BY id DESC", (cat_filter,))
        else:
            self.cur.execute("SELECT id, category, amount FROM expenses ORDER BY id DESC")
        rows = self.cur.fetchall()
        self.expenses = rows
        total = 0
        for idx, (eid, category, amount) in enumerate(rows):
            self.expense_list.insert(tk.END, f"{category} - ${amount:.2f}")
            total += amount
        self.total_label.config(text=f"Total: ${total:.2f}")
        self.clear_selection()
        self.load_categories()

    def clear_selection(self):
        self.selected_id = None
        self.update_btn.config(state=tk.DISABLED)
        self.delete_btn.config(state=tk.DISABLED)
        self.add_btn.config(state=tk.NORMAL)
        self.category_var.set("")
        self.amount_entry.delete(0, tk.END)

    def on_select(self, event):
        if not self.expense_list.curselection():
            return
        index = self.expense_list.curselection()[0]
        eid, category, amount = self.expenses[index]
        self.selected_id = eid
        self.category_var.set(category)
        self.amount_entry.delete(0, tk.END)
        self.amount_entry.insert(0, str(amount))
        self.add_btn.config(state=tk.DISABLED)
        self.update_btn.config(state=tk.NORMAL)
        self.delete_btn.config(state=tk.NORMAL)

    def add_expense(self):
        category = self.category_var.get().strip()
        amount_text = self.amount_entry.get().strip()
        if not category or not amount_text:
            messagebox.showwarning("Input Error", "Please enter both category and amount.")
            return
        try:
            amount = float(amount_text)
            if amount < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid positive number for amount.")
            return

        self.cur.execute("INSERT INTO expenses (category, amount) VALUES (?, ?)", (category, amount))
        self.conn.commit()
        self.load_expenses()

    def update_expense(self):
        if self.selected_id is None:
            return
        category = self.category_var.get().strip()
        amount_text = self.amount_entry.get().strip()
        if not category or not amount_text:
            messagebox.showwarning("Input Error", "Please enter both category and amount.")
            return
        try:
            amount = float(amount_text)
            if amount < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid positive number for amount.")
            return

        self.cur.execute("UPDATE expenses SET category=?, amount=? WHERE id=?", (category, amount, self.selected_id))
        self.conn.commit()
        self.load_expenses()

    def delete_expense(self):
        if self.selected_id is None:
            return
        if messagebox.askyesno("Confirm Delete", "Delete the selected expense?"):
            self.cur.execute("DELETE FROM expenses WHERE id=?", (self.selected_id,))
            self.conn.commit()
            self.load_expenses()

    def clear_filter(self):
        self.filter_var.set("")
        self.load_expenses()

    def export_report(self):
        cat_filter = self.filter_var.get().strip()
        if cat_filter:
            self.cur.execute("SELECT category, amount FROM expenses WHERE category=? ORDER BY id DESC", (cat_filter,))
        else:
            self.cur.execute("SELECT category, amount FROM expenses ORDER BY id DESC")
        rows = self.cur.fetchall()

        if not rows:
            messagebox.showinfo("Export", "No expenses to export.")
            return

        file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")],
            title="Save Report As"
        )
        if not file:
            return

        total = sum(amount for _, amount in rows)
        with open(file, "w", encoding="utf-8") as f:
            f.write("Expense Report\n")
            f.write("================\n")
            if cat_filter:
                f.write(f"Category Filter: {cat_filter}\n\n")
            for category, amount in rows:
                f.write(f"{category}: ${amount:.2f}\n")
            f.write("\n")
            f.write(f"Total Expenses: ${total:.2f}\n")

        messagebox.showinfo("Export", f"Report saved to {file}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x450")
    app = ExpenseTracker(root)
    root.mainloop()
