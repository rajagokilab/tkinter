import tkinter as tk
from tkinter import filedialog, messagebox

def apply_config():
    title = entry_title.get().strip()
    width = entry_width.get().strip()
    height = entry_height.get().strip()
    icon_path = icon_path_var.get().strip()

    if not width.isdigit() or not height.isdigit():
        messagebox.showerror("Invalid input", "Width and Height must be positive integers.")
        return

    # Apply window size and title
    root.geometry(f"{width}x{height}")
    root.title(title if title else "Custom Window Configurator")

    # Apply icon if path provided
    if icon_path:
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            messagebox.showerror("Icon Error", f"Failed to set icon:\n{e}")

def browse_icon():
    filetypes = [("Icon files", "*.ico"), ("All files", "*.*")]
    filename = filedialog.askopenfilename(title="Select Icon File", filetypes=filetypes)
    if filename:
        icon_path_var.set(filename)

root = tk.Tk()
root.geometry("400x250")
root.title("Custom Window Configurator")

# Labels and Entries
tk.Label(root, text="Window Title:").place(x=20, y=20)
entry_title = tk.Entry(root, width=30)
entry_title.place(x=140, y=20)

tk.Label(root, text="Width:").place(x=20, y=60)
entry_width = tk.Entry(root, width=10)
entry_width.place(x=140, y=60)

tk.Label(root, text="Height:").place(x=220, y=60)
entry_height = tk.Entry(root, width=10)
entry_height.place(x=270, y=60)

tk.Label(root, text="Icon (.ico) Path:").place(x=20, y=100)
icon_path_var = tk.StringVar()
entry_icon = tk.Entry(root, textvariable=icon_path_var, width=30)
entry_icon.place(x=140, y=100)

btn_browse = tk.Button(root, text="Browse...", command=browse_icon)
btn_browse.place(x=330, y=95)

btn_apply = tk.Button(root, text="Apply Configuration", command=apply_config)
btn_apply.place(x=140, y=150)

root.mainloop()
