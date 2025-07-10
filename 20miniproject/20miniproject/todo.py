import tkinter as tk
from tkinter import messagebox, filedialog

# === Task Functions ===

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")

def mark_done(event):
    index = task_listbox.curselection()
    if index:
        current = task_listbox.get(index)
        if not current.startswith("✓ "):
            task_listbox.delete(index)
            task_listbox.insert(index, "✓ " + current)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file:
        with open(file, "w") as f:
            for task in tasks:
                f.write(task + "\n")

def load_tasks():
    file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file:
        task_listbox.delete(0, tk.END)
        with open(file, "r") as f:
            for line in f:
                task_listbox.insert(tk.END, line.strip())

# === GUI Setup ===

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x450")

# Entry Frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox Frame with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(list_frame, width=50, height=20, yscrollcommand=scrollbar.set)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=task_listbox.yview)

# Bind double-click to mark task done
task_listbox.bind("<Double-Button-1>", mark_done)

# Save/Load Buttons
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

tk.Button(file_frame, text="Save List", command=save_tasks).pack(side=tk.LEFT, padx=10)
tk.Button(file_frame, text="Load List", command=load_tasks).pack(side=tk.LEFT, padx=10)

root.mainloop()
