import tkinter as tk
from tkinter import messagebox, filedialog

def add_task():
    task = task_entry.get().strip()
    if not task:
        messagebox.showwarning("Input Error", "Please enter a task.")
        return
    task_listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def mark_done(event):
    index = task_listbox.curselection()
    if not index:
        return
    i = index[0]
    task = task_listbox.get(i)
    if not task.startswith("✓ "):
        task_listbox.delete(i)
        task_listbox.insert(i, "✓ " + task)
        task_listbox.itemconfig(i, fg="green")

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    if not tasks:
        messagebox.showinfo("Save Tasks", "No tasks to save.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path, "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Save Tasks", f"Tasks saved to {file_path}")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path, "r") as f:
            tasks = f.readlines()
        task_listbox.delete(0, tk.END)
        for task in tasks:
            task = task.strip()
            task_listbox.insert(tk.END, task)
            if task.startswith("✓ "):
                task_listbox.itemconfig(tk.END, fg="green")

root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

# Entry and add button frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=30)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox with scrollbar
list_frame = tk.Frame(root)
list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=task_listbox.yview)

# Bind double click to mark done
task_listbox.bind("<Double-Button-1>", mark_done)

# Save and Load buttons
save_load_frame = tk.Frame(root)
save_load_frame.pack(pady=10)

save_button = tk.Button(save_load_frame, text="Save Tasks", command=save_tasks)
save_button.pack(side=tk.LEFT, padx=10)

load_button = tk.Button(save_load_frame, text="Load Tasks", command=load_tasks)
load_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
