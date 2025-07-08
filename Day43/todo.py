import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk

class AddTaskDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add New Task")
        self.geometry("300x150")
        self.grab_set()  # modal

        tk.Label(self, text="Task Name:").pack(pady=(10, 2))
        self.task_entry = tk.Entry(self)
        self.task_entry.pack(fill="x", padx=20)

        tk.Label(self, text="Deadline (YYYY-MM-DD):").pack(pady=(10, 2))
        self.deadline_entry = tk.Entry(self)
        self.deadline_entry.pack(fill="x", padx=20)

        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="Add", command=self.on_add).pack(side="left", padx=10)
        tk.Button(btn_frame, text="Cancel", command=self.destroy).pack(side="left")

        self.task = None
        self.deadline = None

    def on_add(self):
        task = self.task_entry.get().strip()
        deadline = self.deadline_entry.get().strip()
        if not task:
            messagebox.showwarning("Input Error", "Please enter a task name.")
            return
        # You could add deadline format validation here if desired
        self.task = task
        self.deadline = deadline
        self.destroy()


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("500x400")

        self.create_menu()
        self.create_panedwindow()
        self.tasks = []  # Store tasks as tuples (task, deadline)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Save List", command=self.save_list)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def create_panedwindow(self):
        pw = tk.PanedWindow(self.root, orient=tk.VERTICAL)
        pw.pack(fill="both", expand=True)

        # Top pane: toolbar frame
        toolbar_frame = tk.Frame(pw, bd=2, relief=tk.RAISED)
        pw.add(toolbar_frame, minsize=50)

        add_btn = tk.Button(toolbar_frame, text="Add Task", command=self.open_add_task_dialog)
        add_btn.pack(side="left", padx=10, pady=5)

        del_btn = tk.Button(toolbar_frame, text="Delete Task", command=self.delete_task)
        del_btn.pack(side="left", padx=10, pady=5)

        # Bottom pane: task list frame
        task_frame = tk.Frame(pw)
        pw.add(task_frame)

        # Scrollable Treeview for tasks
        self.tree = ttk.Treeview(task_frame, columns=("Deadline"), show="headings", selectmode="browse")
        self.tree.heading("Deadline", text="Deadline")
        self.tree.heading("#0", text="Task")
        self.tree.column("#0", width=250)
        self.tree.column("Deadline", width=120)
        self.tree.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(task_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def open_add_task_dialog(self):
        dialog = AddTaskDialog(self.root)
        self.root.wait_window(dialog)

        if dialog.task:
            self.tasks.append((dialog.task, dialog.deadline))
            self.tree.insert("", "end", text=dialog.task, values=(dialog.deadline,))

    def delete_task(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Delete Task", "Please select a task to delete.")
            return
        task_text = self.tree.item(selected)["text"]
        if messagebox.askyesno("Delete Task", f"Are you sure you want to delete '{task_text}'?"):
            self.tree.delete(selected)
            # Also remove from internal list
            self.tasks = [t for t in self.tasks if t[0] != task_text]

    def save_list(self):
        if not self.tasks:
            messagebox.showinfo("Save List", "No tasks to save.")
            return
        try:
            with open("todo_list.txt", "w") as f:
                for task, deadline in self.tasks:
                    f.write(f"{task} - {deadline}\n")
            messagebox.showinfo("Save List", "Task list saved to todo_list.txt")
        except Exception as e:
            messagebox.showerror("Save Error", f"Error saving file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
