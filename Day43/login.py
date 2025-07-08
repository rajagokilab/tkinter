import tkinter as tk
from tkinter import messagebox

class UserSwitchDialog(tk.Toplevel):
    def __init__(self, parent, users, callback):
        super().__init__(parent)
        self.title("Switch User")
        self.geometry("300x200")
        self.callback = callback

        tk.Label(self, text="Select User:", font=("Arial", 12)).pack(pady=10)

        self.users = users
        self.selected_user = tk.StringVar(value=users[0] if users else "")

        self.listbox = tk.Listbox(self)
        for user in users:
            self.listbox.insert(tk.END, user)
        self.listbox.pack(fill="both", expand=True, padx=20, pady=5)
        self.listbox.selection_set(0)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Login", command=self.login).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.destroy).pack(side="left", padx=5)

    def login(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("No Selection", "Please select a user.")
            return
        user = self.listbox.get(sel[0])
        self.callback(user)
        self.destroy()

class LoginPanelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-User Login Panel")
        self.root.geometry("400x200")

        self.users = ["Alice", "Bob", "Charlie", "Diana"]
        self.current_user = None

        self.create_menu()
        self.create_widgets()
        self.update_user_display()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        user_menu = tk.Menu(menubar, tearoff=0)
        user_menu.add_command(label="Logout", command=self.logout)
        user_menu.add_separator()
        user_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="User", menu=user_menu)
        self.root.config(menu=menubar)

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        self.user_label = tk.Label(frame, text="", font=("Arial", 16))
        self.user_label.pack(pady=20)

        self.switch_btn = tk.Button(frame, text="Switch User", command=self.open_switch_dialog)
        self.switch_btn.pack()

    def update_user_display(self):
        if self.current_user:
            self.user_label.config(text=f"Logged in as: {self.current_user}")
        else:
            self.user_label.config(text="No user logged in")

    def open_switch_dialog(self):
        UserSwitchDialog(self.root, self.users, self.set_current_user)

    def set_current_user(self, username):
        self.current_user = username
        self.update_user_display()

    def logout(self):
        if self.current_user is None:
            messagebox.showinfo("Logout", "No user is currently logged in.")
            return
        if messagebox.askyesno("Logout", f"Logout user {self.current_user}?"):
            self.current_user = None
            self.update_user_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginPanelApp(root)
    root.mainloop()
