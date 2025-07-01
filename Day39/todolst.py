import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def remove_task():
    selected_indices = task_listbox.curselection()
    if not selected_indices:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")
        return
    for index in reversed(selected_indices):  # Remove from end to avoid index shift
        task_listbox.delete(index)

root = tk.Tk()
root.title("To-Do List App")
root.geometry("350x400")

# Task entry and add button
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack()

# Listbox to show tasks
task_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40, height=15)
task_listbox.pack(pady=10)

# Remove selected task(s) button
remove_btn = tk.Button(root, text="Remove Selected Task(s)", width=20, command=remove_task)
remove_btn.pack()

root.mainloop()
