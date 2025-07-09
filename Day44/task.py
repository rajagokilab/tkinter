import tkinter as tk

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Task Manager with Completion Toggle")
        self.geometry("350x300")

        self.tasks = [
            "Buy groceries",
            "Read book",
            "Write report",
            "Call Alice",
            "Workout"
        ]

        self.listbox = tk.Listbox(self, font=("Arial", 14))
        self.listbox.pack(fill="both", expand=True, padx=20, pady=20)
        self.populate_tasks()

        self.listbox.bind("<Double-Button-1>", self.toggle_task)

    def populate_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

    def toggle_task(self, event):
        selection = self.listbox.curselection()
        if not selection:
            return
        index = selection[0]
        task = self.listbox.get(index)

        if task.startswith("✔ "):
            # Mark as incomplete
            new_task = task[2:]
        else:
            # Mark as complete
            new_task = "✔ " + task

        # Update internal list
        self.tasks[index] = new_task
        # Refresh listbox
        self.listbox.delete(index)
        self.listbox.insert(index, new_task)

        # Optional: change color for completed tasks
        if new_task.startswith("✔ "):
            self.listbox.itemconfig(index, fg="gray")
        else:
            self.listbox.itemconfig(index, fg="black")

if __name__ == "__main__":
    app = TaskManager()
    app.mainloop()
