import tkinter as tk
from tkinter import messagebox, filedialog

def load_file():
    filepath = filepath_entry.get().strip()
    if not filepath:
        messagebox.showwarning("Input Error", "Please enter a file path.")
        return
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, content)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load file:\n{e}")

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        filepath_entry.delete(0, tk.END)
        filepath_entry.insert(0, filename)

root = tk.Tk()
root.title("Text File Viewer")
root.geometry("600x400")

tk.Label(root, text="File Path:").pack(anchor='w', padx=10, pady=(10, 0))
filepath_entry = tk.Entry(root, width=70)
filepath_entry.pack(padx=10)

browse_btn = tk.Button(root, text="Browse...", command=browse_file)
browse_btn.pack(pady=5)

load_btn = tk.Button(root, text="Load File", command=load_file)
load_btn.pack(pady=5)

text_area = tk.Text(root, wrap='word')
text_area.pack(expand=True, fill='both', padx=10, pady=10)

root.mainloop()
