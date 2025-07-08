import tkinter as tk
from tkinter import messagebox

def open_file():
    print("Open command triggered")
    update_recent_files("OpenedFile.txt")

def save_file():
    print("Save command triggered")

def new_file():
    print("New file created")

def show_about():
    messagebox.showinfo("About", "Tkinter Menu Example\nVersion 1.0")

def update_recent_files(filename):
    if filename not in recent_files:
        recent_files.insert(0, filename)
        if len(recent_files) > 5:
            recent_files.pop()
    refresh_recent_menu()

def refresh_recent_menu():
    recent_menu.delete(0, tk.END)
    for file in recent_files:
        recent_menu.add_command(label=file, command=lambda f=file: print(f"Opening {f}"))

# Main window
root = tk.Tk()
root.title("Tkinter Menu Example")
root.geometry("500x300")

# 26. Create a basic Menu bar with File and Edit menus
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 27–30. File menu with Open, Exit, separator, submenus
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file, accelerator="Ctrl+O")  # 27
file_menu.add_command(label="Save", command=save_file, state="disabled")  # 30 (disabled)
file_menu.add_separator()  # 29
file_menu.add_command(label="Exit", command=root.quit)  # 28

# 31. Help menu with “About” dialog using messagebox.showinfo()
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=show_about)

# 32. Use add_cascade() to attach submenus to the main menu
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=tk.Menu(menu_bar, tearoff=0))  # Placeholder Edit menu
menu_bar.add_cascade(label="Help", menu=help_menu)

# 33. Add multiple submenus (File → New, Open, Save)
new_submenu = tk.Menu(file_menu, tearoff=0)
new_submenu.add_command(label="New File", command=new_file)
new_submenu.add_command(label="New Project", command=lambda: print("New Project created"))
file_menu.insert_cascade(0, label="New", menu=new_submenu)

# 34. Bind keyboard shortcuts (e.g., Ctrl+O for Open)
root.bind_all("<Control-o>", lambda event: open_file())

# 35. Dynamically update menu contents at runtime (e.g., recent files)
recent_menu = tk.Menu(file_menu, tearoff=0)
file_menu.insert_cascade(4, label="Recent Files", menu=recent_menu)  # Insert before "Exit"

recent_files = []
update_recent_files("Example1.txt")
update_recent_files("Example2.txt")

root.mainloop()
