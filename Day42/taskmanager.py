import tkinter as tk
from tkinter import messagebox
import os

# === Setup main window ===
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")

# === Functions ===
tasks = []
task_file = "tasks.txt"

def add_task():
    task = entry.get().strip()
    if task:
        tasks.append({"text": task, "done": False})
        update_listbox()
        entry.delete(0, tk.END)

def remove_task():
    selected = listbox.curselection()
    for index in reversed(selected):
        del tasks[index]
    update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        text = task["text"]
        if task["done"]:
            text += " ✔"  # Or just show as is and use font styling
        listbox.insert(tk.END, text)
        if task["done"]:
            listbox.itemconfig(tk.END, fg="gray", font=("Arial", 10, "overstrike"))
        else:
            listbox.itemconfig(tk.END, fg="black", font=("Arial", 10))

def toggle_task(event):
    index = listbox.curselection()
    if index:
        i = index[0]
        tasks[i]["done"] = not tasks[i]["done"]
        update_listbox()

def save_tasks():
    with open(task_file, "w") as f:
        for task in tasks:
            line = f"{task['text']}|{task['done']}\n"
            f.write(line)
    messagebox.showinfo("Saved", "Tasks saved successfully!")

def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, "r") as f:
            tasks.clear()
            for line in f:
                if '|' in line:
                    text, done = line.strip().split("|")
                    tasks.append({"text": text, "done": done == "True"})
        update_listbox()
    else:
        messagebox.showwarning("No File", "No saved task file found.")

# === Entry + Add Button ===
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=30)
entry.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(entry_frame, text="Add Task", command=add_task)
add_btn.pack(side=tk.LEFT)

# === Listbox + Scrollbar ===
listbox_frame = tk.Frame(root)
listbox_frame.pack()

scrollbar = tk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, width=45, height=10, yscrollcommand=scrollbar.set)
listbox.pack(side=tk.LEFT)

scrollbar.config(command=listbox.yview)

# === Buttons for Actions ===
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Remove Selected", command=remove_task).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Save Tasks", command=save_tasks).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Load Tasks", command=load_tasks).pack(side=tk.LEFT, padx=5)

# === Bind Double-click to Toggle Completion ===
listbox.bind("<Double-1>", toggle_task)

# === Load tasks initially if file exists ===
load_tasks()

root.mainloop()
