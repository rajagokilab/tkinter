import tkinter as tk
from datetime import datetime

def save_note():
    note = text.get("1.0", tk.END).strip()
    if note:
        filename = datetime.now().strftime("%Y-%m-%d") + ".txt"
        with open(filename, "a") as f:
            f.write(note + "\n\n")
        status_label.config(text="Note saved!")
        text.delete("1.0", tk.END)
    else:
        status_label.config(text="Write something before saving!")

root = tk.Tk()
root.title("Simple Diary App")
root.geometry("400x300")

tk.Label(root, text="Write your note:").grid(row=0, column=0, padx=10, pady=10, sticky="w")

text = tk.Text(root, width=40, height=10)
text.grid(row=1, column=0, padx=10, pady=10)

save_button = tk.Button(root, text="Save Note", command=save_note)
save_button.grid(row=2, column=0, pady=(0,10))

status_label = tk.Label(root, text="")
status_label.grid(row=3, column=0)

root.mainloop()
