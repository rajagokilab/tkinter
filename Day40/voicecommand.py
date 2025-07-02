import tkinter as tk

def log_command():
    command = command_entry.get().strip()
    if command:
        commands_text.insert(tk.END, command + "\n")
        command_entry.delete(0, tk.END)
        update_count()

def update_count():
    # Count lines in the Text widget to get number of commands
    lines = int(commands_text.index('end-1c').split('.')[0])
    count_label.config(text=f"Commands entered: {lines}")

root = tk.Tk()
root.title("Voice Command Logger")

tk.Label(root, text="Enter command:").pack(pady=5)
command_entry = tk.Entry(root, width=40)
command_entry.pack(pady=5)

log_btn = tk.Button(root, text="Log Command", command=log_command)
log_btn.pack(pady=5)

commands_text = tk.Text(root, width=50, height=10)
commands_text.pack(pady=5)

count_label = tk.Label(root, text="Commands entered: 0")
count_label.pack(pady=5)

root.mainloop()
