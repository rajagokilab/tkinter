import tkinter as tk
from tkinter import messagebox
import sqlite3
import time

class TimerTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ask Timer Tracker")

        self.conn = sqlite3.connect("tasks.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE,
                total_seconds INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

        self.timers = {}  # task_name: start_time or None
        self.running_task = None
        self.elapsed = 0

        self.create_widgets()
        self.load_tasks()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="New Task Name:").grid(row=0, column=0)
        self.task_entry = tk.Entry(frame, width=30)
        self.task_entry.grid(row=0, column=1)
        tk.Button(frame, text="Add Task", command=self.add_task).grid(row=0, column=2, padx=5)

        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)

        tk.Label(self.task_frame, text="Tasks").grid(row=0, column=0, padx=5)
        tk.Label(self.task_frame, text="Timer").grid(row=0, column=1, padx=5)
        tk.Label(self.task_frame, text="Action").grid(row=0, column=2, padx=5)

        self.task_widgets = {}

        tk.Label(self.root, text="Summary: Total Time Spent").pack()
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.pack(pady=5)

    def add_task(self):
        name = self.task_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Task name cannot be empty.")
            return

        try:
            self.cur.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Task with this name already exists.")
            return

        self.task_entry.delete(0, tk.END)
        self.load_tasks()

    def load_tasks(self):
        # Clear existing widgets
        for widgets in self.task_widgets.values():
            for w in widgets:
                w.destroy()
        self.task_widgets.clear()

        self.cur.execute("SELECT name, total_seconds FROM tasks ORDER BY name")
        tasks = self.cur.fetchall()

        for i, (name, total_sec) in enumerate(tasks, start=1):
            timer_label = tk.Label(self.task_frame, text=self.format_time(total_sec))
            timer_label.grid(row=i, column=1, padx=5)
            btn = tk.Button(self.task_frame, text="Start", command=lambda n=name: self.toggle_timer(n))
            btn.grid(row=i, column=2, padx=5)
            tk.Label(self.task_frame, text=name).grid(row=i, column=0, padx=5)

            self.task_widgets[name] = (timer_label, btn)

            # Initialize timer state
            self.timers.setdefault(name, None)

        self.update_summary()

    def toggle_timer(self, task_name):
        if self.running_task and self.running_task != task_name:
            messagebox.showinfo("Timer Running", f"Stop '{self.running_task}' before starting another.")
            return

        if self.timers[task_name] is None:
            # Start timing
            self.timers[task_name] = time.time()
            self.running_task = task_name
            self.task_widgets[task_name][1].config(text="Stop")
            self.update_timer()
        else:
            # Stop timing
            start_time = self.timers[task_name]
            elapsed = int(time.time() - start_time)
            self.timers[task_name] = None
            self.running_task = None
            self.task_widgets[task_name][1].config(text="Start")

            # Update DB total_seconds
            self.cur.execute("SELECT total_seconds FROM tasks WHERE name=?", (task_name,))
            total_sec = self.cur.fetchone()[0]
            new_total = total_sec + elapsed
            self.cur.execute("UPDATE tasks SET total_seconds=? WHERE name=?", (new_total, task_name))
            self.conn.commit()

            # Update timer label immediately
            self.task_widgets[task_name][0].config(text=self.format_time(new_total))
            self.update_summary()

    def update_timer(self):
        if self.running_task:
            start_time = self.timers[self.running_task]
            elapsed = int(time.time() - start_time)

            self.task_widgets[self.running_task][0].config(text=self.format_time(
                self.get_total_seconds(self.running_task) + elapsed))
            self.root.after(1000, self.update_timer)

    def get_total_seconds(self, task_name):
        self.cur.execute("SELECT total_seconds FROM tasks WHERE name=?", (task_name,))
        return self.cur.fetchone()[0]

    def update_summary(self):
        self.listbox.delete(0, tk.END)
        self.cur.execute("SELECT name, total_seconds FROM tasks ORDER BY name")
        for name, total_sec in self.cur.fetchall():
            self.listbox.insert(tk.END, f"{name}: {self.format_time(total_sec)}")

    @staticmethod
    def format_time(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerTrackerApp(root)
    root.mainloop()
