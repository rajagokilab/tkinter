import tkinter as tk
from tkinter import ttk, messagebox

class TaskManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📝 Daily Task List Manager")
        self.geometry("400x400")
        self.resizable(False, False)

        # -------- Input Frame --------
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10, padx=10, fill='x')

        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(input_frame, textvariable=self.task_var)
        self.task_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        ttk.Button(input_frame, text="Add Task ➕", command=self.add_task).pack(side="right")

        # -------- Listbox + Scrollbar --------
        list_frame = ttk.Frame(self)
        list_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.task_listbox = tk.Listbox(list_frame, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.task_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # -------- Buttons --------
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=5)

        ttk.Button(btn_frame, text="Delete Selected ❌", command=self.delete_task).pack()

        # Double-click binding to mark complete
        self.task_listbox.bind("<Double-Button-1>", self.mark_completed)

    # -------- Functions --------
    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task before adding.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showinfo("No Selection", "Please select a task to delete.")

    def mark_completed(self, event):
        index = self.task_listbox.curselection()
        if index:
            current_task = self.task_listbox.get(index)
            if not current_task.startswith("✓ "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✓ {current_task}")
            else:
                # Optionally toggle back to unmarked
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, current_task[2:])

if __name__ == "__main__":
    TaskManager().mainloop()
