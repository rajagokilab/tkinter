import tkinter as tk
from tkinter import font

root = tk.Tk()
root.title("Widget Functionality & Dynamic Behavior")
root.geometry("500x500")

# Task 46: Label that changes color when clicked
def change_label_color(event):
    color_label.config(bg="lightblue" if color_label.cget("bg") != "lightblue" else "lightgreen")

color_label = tk.Label(root, text="Click me to change color", bg="lightgreen", font=("Arial", 14))
color_label.pack(pady=10)
color_label.bind("<Button-1>", change_label_color)

# Task 47: Resize font on hover
def enlarge_font(event):
    hover_label.config(font=hover_big_font)

def reset_font(event):
    hover_label.config(font=hover_normal_font)

hover_normal_font = font.Font(family="Arial", size=12)
hover_big_font = font.Font(family="Arial", size=18)

hover_label = tk.Label(root, text="Hover over me!", font=hover_normal_font)
hover_label.pack(pady=10)
hover_label.bind("<Enter>", enlarge_font)
hover_label.bind("<Leave>", reset_font)

# Task 48: Password entry with visibility toggle
def toggle_password():
    if password_entry.cget("show") == "":
        password_entry.config(show="*")
        toggle_button.config(text="Show")
    else:
        password_entry.config(show="")
        toggle_button.config(text="Hide")

tk.Label(root, text="Password Entry").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
toggle_button = tk.Button(root, text="Show", command=toggle_password)
toggle_button.pack(pady=5)

# Task 49: Progress tracker
progress = ""
def update_progress():
    global progress
    if len(progress) < 10:
        progress += "■"
        progress_label.config(text=progress)

tk.Label(root, text="Progress Tracker (Click to Fill)").pack()
progress_label = tk.Label(root, text="", font=("Courier", 18))
progress_label.pack()
progress_button = tk.Button(root, text="Click to Fill Progress", command=update_progress)
progress_button.pack(pady=5)

# Task 50: Real-time character counter
def update_count(event=None):
    text = input_entry.get()
    counter_label.config(text=f"Characters: {len(text)}")

tk.Label(root, text="Text Entry with Counter").pack()
input_entry = tk.Entry(root)
input_entry.pack()
input_entry.bind("<KeyRelease>", update_count)
counter_label = tk.Label(root, text="Characters: 0")
counter_label.pack()

root.mainloop()
