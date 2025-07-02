import tkinter as tk
from tkinter import messagebox

FILENAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.readlines()
            for task in tasks:
                task = task.strip()
                if task:
                    listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get().strip()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")
        return
    for index in reversed(selected):
        listbox.delete(index)

def clear_all():
    if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
        listbox.delete(0, tk.END)

def on_closing():
    save_tasks()
    root.destroy()

root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected Task", command=delete_task)
delete_btn.pack(pady=5)

clear_btn = tk.Button(root, text="Clear All Tasks", command=clear_all)
clear_btn.pack(pady=5)

listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=40, height=15)
listbox.pack(pady=10)

load_tasks()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
