import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class DatabaseViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")
        self.root.geometry("700x500")

        self.create_menu()
        self.create_toolbar()
        self.create_panedwindow()
        self.data = []

    def create_menu(self):
        menubar = tk.Menu(self.root)
        data_menu = tk.Menu(menubar, tearoff=0)
        data_menu.add_command(label="Load DB", command=self.load_db)
        data_menu.add_separator()
        data_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Data", menu=data_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        refresh_btn = tk.Button(toolbar, text="Refresh", command=self.refresh_data)
        refresh_btn.pack(side="left", padx=5, pady=5)

        filter_btn = tk.Button(toolbar, text="Filter", command=self.apply_filter)
        filter_btn.pack(side="left", padx=5, pady=5)

    def create_panedwindow(self):
        self.paned = tk.PanedWindow(self.root, orient=tk.VERTICAL)
        self.paned.pack(fill="both", expand=True)

        # Top pane: filter/search
        filter_frame = tk.Frame(self.paned, bd=2, relief=tk.SUNKEN)
        self.paned.add(filter_frame, minsize=100)

        tk.Label(filter_frame, text="Filter by keyword:").pack(side="left", padx=5, pady=10)
        self.filter_entry = tk.Entry(filter_frame)
        self.filter_entry.pack(side="left", fill="x", expand=True, padx=5, pady=10)

        # Bottom pane: results display
        results_frame = tk.Frame(self.paned)
        self.paned.add(results_frame)

        columns = ("ID", "Name", "Age", "Email")
        self.tree = ttk.Treeview(results_frame, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150)
        self.tree.pack(fill="both", expand=True)

        scrollbar = ttk.Scrollbar(results_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def load_db(self):
        # For demo, load sample data instead of real DB
        self.data = [
            (1, "Alice Johnson", 30, "alice@example.com"),
            (2, "Bob Smith", 24, "bob@example.com"),
            (3, "Charlie Lee", 29, "charlie@example.com"),
            (4, "Diana King", 35, "diana@example.com"),
        ]
        self.refresh_data()
        messagebox.showinfo("Load DB", "Database loaded successfully!")

    def refresh_data(self):
        self.tree.delete(*self.tree.get_children())
        for row in self.data:
            self.tree.insert("", "end", values=row)

    def apply_filter(self):
        keyword = self.filter_entry.get().lower()
        filtered = [row for row in self.data if keyword in str(row).lower()]
        self.tree.delete(*self.tree.get_children())
        for row in filtered:
            self.tree.insert("", "end", values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseViewer(root)
    root.mainloop()
