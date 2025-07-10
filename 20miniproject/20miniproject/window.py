import tkinter as tk
from tkinter import messagebox, filedialog

def apply_changes():
    title = title_entry.get().strip()
    width = width_entry.get().strip()
    height = height_entry.get().strip()
    icon_path = icon_entry.get().strip()

    # Validate width and height
    if not width.isdigit() or not height.isdigit():
        messagebox.showerror("Invalid input", "Width and Height must be positive integers.")
        return

    # Apply title and geometry
    root.title(title if title else "Custom Window")
    root.geometry(f"{width}x{height}")

    # Apply icon if provided
    if icon_path:
        try:
            root.iconbitmap(icon_path)
        except Exception as e:
            messagebox.showwarning("Icon Error", f"Failed to set icon:\n{e}")

def browse_icon():
    file = filedialog.askopenfilename(
        title="Select Icon",
        filetypes=[("Icon files", "*.ico"), ("All files", "*.*")]
    )
    if file:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, file)

# Main window
root = tk.Tk()
root.geometry("400x250")
root.title("Custom Window Configurator")

# Labels and Entries
tk.Label(root, text="Window Title:").place(x=20, y=20)
title_entry = tk.Entry(root, width=30)
title_entry.place(x=140, y=20)

tk.Label(root, text="Width:").place(x=20, y=60)
width_entry = tk.Entry(root, width=10)
width_entry.place(x=140, y=60)
width_entry.insert(0, "400")

tk.Label(root, text="Height:").place(x=20, y=100)
height_entry = tk.Entry(root, width=10)
height_entry.place(x=140, y=100)
height_entry.insert(0, "250")

tk.Label(root, text="Icon Path (.ico):").place(x=20, y=140)
icon_entry = tk.Entry(root, width=25)
icon_entry.place(x=140, y=140)

browse_btn = tk.Button(root, text="Browse...", command=browse_icon)
browse_btn.place(x=320, y=136)

apply_btn = tk.Button(root, text="Apply Changes", command=apply_changes)
apply_btn.place(x=140, y=180)

root.mainloop()
