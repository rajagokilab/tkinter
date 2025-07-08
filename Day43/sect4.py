import tkinter as tk
from tkinter import messagebox

def open_action():
    print("Open button clicked")

def save_action():
    print("Save button clicked")

def custom_action():
    print("Custom action performed")

def toggle_toolbar():
    global toolbar_visible
    if toolbar_visible:
        toolbar.pack_forget()
        toggle_btn.config(text="Show Toolbar")
    else:
        toolbar.pack(side="top", fill="x")
        toggle_btn.config(text="Hide Toolbar")
    toolbar_visible = not toolbar_visible

# Main window
root = tk.Tk()
root.title("Tkinter Toolbar Example")
root.geometry("500x300")

# 36. Create a toolbar at the top of the window using Frame
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED, bg="lightgray")
toolbar.pack(side="top", fill="x")

# 37. Add "Open" and "Save" Buttons with icons or text
# (Using text here, but you could use images with `PhotoImage`)
open_btn = tk.Button(toolbar, text="Open", command=open_action)
save_btn = tk.Button(toolbar, text="Save", command=save_action)

# 38. Align buttons horizontally using pack(side=LEFT)
open_btn.pack(side="left", padx=2, pady=2)
save_btn.pack(side="left", padx=2, pady=2)

# 39. Create a toolbar with Buttons that perform different actions
custom_btn = tk.Button(toolbar, text="Run", command=custom_action)
custom_btn.pack(side="left", padx=2, pady=2)

# 40. Hide and show the toolbar dynamically with a toggle button
toolbar_visible = True
toggle_btn = tk.Button(root, text="Hide Toolbar", command=toggle_toolbar)
toggle_btn.pack(side="top", pady=10)

# Dummy content area
tk.Label(root, text="Main content area").pack(expand=True)

root.mainloop()
