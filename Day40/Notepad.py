import tkinter as tk
from tkinter import messagebox, filedialog

def save_notes():
    content = text_area.get("1.0", tk.END)
    with open("notes.txt", "w") as f:
        f.write(content)
    messagebox.showinfo("Save", "Notes saved successfully!")

def load_notes():
    try:
        with open("notes.txt", "r") as f:
            content = f.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)
    except FileNotFoundError:
        messagebox.showwarning("Load", "No saved notes found.")

def clear_notes():
    text_area.delete("1.0", tk.END)

root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")  # resizable by default

# Text widget for note input
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(fill="x")

btn_save = tk.Button(button_frame, text="Save", command=save_notes)
btn_save.pack(side="left", padx=5, pady=5)

btn_load = tk.Button(button_frame, text="Load", command=load_notes)
btn_load.pack(side="left", padx=5, pady=5)

btn_clear = tk.Button(button_frame, text="Clear", command=clear_notes)
btn_clear.pack(side="left", padx=5, pady=5)

root.mainloop()
