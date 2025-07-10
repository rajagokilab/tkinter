import tkinter as tk
from tkinter import ttk, messagebox

# Sample modules and their completed topics
modules = {
    "Python Basics": [],
    "Data Structures": [],
    "Algorithms": [],
    "Databases": [],
    "Web Development": []
}

current_module = None

def update_progress():
    global current_module
    module = module_combo.get()
    rating = understanding_spinbox.get()

    if module == "":
        messagebox.showwarning("Select Module", "Please select a module.")
        return

    try:
        rating_val = int(rating)
        if rating_val < 1 or rating_val > 10:
            raise ValueError
    except ValueError:
        messagebox.showwarning("Invalid Rating", "Please enter a rating between 1 and 10.")
        return

    current_module = module

    # Add to completed topics if not already added
    topic_desc = f"{module} - Understanding Level: {rating_val}"
    if topic_desc not in modules[module]:
        modules[module].append(topic_desc)
        completed_listbox.insert(tk.END, topic_desc)

    # Update progress bar on canvas
    draw_progress_bar(rating_val)

def draw_progress_bar(level):
    # Clear canvas
    progress_canvas.delete("all")

    # Canvas size
    width = 300
    height = 30
    margin = 10

    # Draw border rectangle
    progress_canvas.create_rectangle(margin, margin, width + margin, height + margin, outline="black", width=2)

    # Fill rectangle according to rating (level/10)
    fill_width = (level / 10) * width
    progress_canvas.create_rectangle(margin, margin, margin + fill_width, height + margin, fill="green")

    # Text showing percentage
    progress_canvas.create_text(width//2 + margin, height//2 + margin, text=f"{level*10}%", fill="white", font=("Arial", 14, "bold"))

# === Main Window ===
root = tk.Tk()
root.title("Tkinter Learning Dashboard")
root.geometry("450x400")
root.configure(padx=20, pady=20)

# Module selection
tk.Label(root, text="Select Module:").pack(anchor="w")
module_combo = ttk.Combobox(root, values=list(modules.keys()), state="readonly", width=30)
module_combo.pack(pady=5)

# Understanding rating
tk.Label(root, text="Rate Understanding Level (1-10):").pack(anchor="w")
understanding_spinbox = tk.Spinbox(root, from_=1, to=10, width=5)
understanding_spinbox.pack(pady=5)
understanding_spinbox.delete(0, tk.END)
understanding_spinbox.insert(0, "5")

# Update button
update_btn = tk.Button(root, text="Update Progress", command=update_progress)
update_btn.pack(pady=10)

# Progress Canvas
progress_canvas = tk.Canvas(root, width=320, height=50, bg="white", bd=2, relief="sunken")
progress_canvas.pack(pady=10)

# Completed Topics Listbox with scrollbar
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

completed_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set, height=8)
completed_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=completed_listbox.yview)

root.mainloop()
