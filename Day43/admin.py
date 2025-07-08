import tkinter as tk
from tkinter import messagebox

class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Dashboard")
        self.root.geometry("900x600")

        self.create_menu()
        self.create_toolbar()
        self.create_frames()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        manage_menu = tk.Menu(menubar, tearoff=0)
        manage_menu.add_command(label="Users", command=lambda: self.show_message("Users"))
        manage_menu.add_command(label="Roles", command=lambda: self.show_message("Roles"))
        manage_menu.add_command(label="Reports", command=lambda: self.show_message("Reports"))
        menubar.add_cascade(label="Manage", menu=manage_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        add_btn = tk.Button(toolbar, text="Add", command=self.open_add_user)
        add_btn.pack(side="left", padx=5, pady=5)

        edit_btn = tk.Button(toolbar, text="Edit", command=lambda: self.show_message("Edit clicked"))
        edit_btn.pack(side="left", padx=5, pady=5)

        delete_btn = tk.Button(toolbar, text="Delete", command=lambda: self.show_message("Delete clicked"))
        delete_btn.pack(side="left", padx=5, pady=5)

    def create_frames(self):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True)

        # Left navigation frame
        self.nav_frame = tk.Frame(container, width=200, bg="#333")
        self.nav_frame.pack(side="left", fill="y")

        nav_items = ["Dashboard", "Users", "Roles", "Reports", "Settings"]
        for item in nav_items:
            btn = tk.Button(self.nav_frame, text=item, fg="white", bg="#333", bd=0,
                            anchor="w", padx=20,
                            command=lambda i=item: self.display_content(i))
            btn.pack(fill="x", pady=2)

        # Right content frame
        self.content_frame = tk.Frame(container, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.content_label = tk.Label(self.content_frame, text="Welcome to Admin Dashboard",
                                      font=("Arial", 16), bg="white")
        self.content_label.pack(padx=20, pady=20)

    def display_content(self, name):
        self.content_label.config(text=f"Selected: {name}")

    def show_message(self, msg):
        messagebox.showinfo("Info", f"{msg} selected")

    def open_add_user(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New User")
        dialog.geometry("300x200")
        dialog.grab_set()  # Modal dialog

        tk.Label(dialog, text="Username:").pack(pady=(20, 5))
        username_entry = tk.Entry(dialog)
        username_entry.pack(pady=5, padx=20, fill="x")

        tk.Label(dialog, text="Email:").pack(pady=5)
        email_entry = tk.Entry(dialog)
        email_entry.pack(pady=5, padx=20, fill="x")

        def submit():
            username = username_entry.get().strip()
            email = email_entry.get().strip()
            if not username or not email:
                messagebox.showwarning("Input Error", "Please enter username and email.")
                return
            # You could add more validation here
            messagebox.showinfo("Success", f"User '{username}' added!")
            dialog.destroy()

        btn_frame = tk.Frame(dialog)
        btn_frame.pack(pady=20)

        submit_btn = tk.Button(btn_frame, text="Submit", command=submit)
        submit_btn.pack(side="left", padx=10)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=dialog.destroy)
        cancel_btn.pack(side="left", padx=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = AdminDashboard(root)
    root.mainloop()
