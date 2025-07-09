import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Mouse Events (Tasks 16–25)")
root.geometry("800x800")

# Task 16: <Button-1> on button prints mouse coordinates
def print_coords(event):
    print(f"Task 16: Clicked at ({event.x}, {event.y})")

btn16 = tk.Button(root, text="Task 16: Click Me")
btn16.bind("<Button-1>", print_coords)
btn16.pack(pady=10)

# Task 17: Label changes color on <Enter> and <Leave>
def on_enter17(e): lbl17.config(bg="lightgreen")
def on_leave17(e): lbl17.config(bg="SystemButtonFace")

lbl17 = tk.Label(root, text="Task 17: Hover Over Me", width=25)
lbl17.bind("<Enter>", on_enter17)
lbl17.bind("<Leave>", on_leave17)
lbl17.pack(pady=10)

# Task 18: Button moves to random location on click
def move_button(event):
    new_x = random.randint(0, root.winfo_width() - 100)
    new_y = random.randint(0, root.winfo_height() - 100)
    btn18.place(x=new_x, y=new_y)

btn18 = tk.Button(root, text="Task 18: Catch Me")
btn18.place(x=50, y=150)
btn18.bind("<Button-1>", move_button)

# Task 19: Right-click to display popup message
def show_popup(event):
    messagebox.showinfo("Task 19", "Right-click detected!")

btn19 = tk.Button(root, text="Task 19: Right-click Me")
btn19.bind("<Button-3>", show_popup)
btn19.pack(pady=10)

# Task 20: Tooltip text using <Enter>/<Leave>
def show_tooltip(e):
    tooltip.place(x=e.widget.winfo_rootx() - root.winfo_rootx() + 100,
                  y=e.widget.winfo_rooty() - root.winfo_rooty() - 20)
def hide_tooltip(e):
    tooltip.place_forget()

btn20 = tk.Button(root, text="Task 20: Hover for Tooltip")
btn20.pack(pady=10)
btn20.bind("<Enter>", show_tooltip)
btn20.bind("<Leave>", hide_tooltip)
tooltip = tk.Label(root, text="Tooltip: This is Task 20", bg="yellow", relief="solid", bd=1)

# Task 21: Double-click label to change its text
def on_double_click(e):
    lbl21.config(text="Double-clicked!")

lbl21 = tk.Label(root, text="Task 21: Double-Click Me", bg="lightgray", width=30)
lbl21.bind("<Double-Button-1>", on_double_click)
lbl21.pack(pady=10)

# Task 22: Click canvas to draw circle
def draw_circle(e):
    r = 5
    canvas22.create_oval(e.x - r, e.y - r, e.x + r, e.y + r, fill="blue")

canvas22 = tk.Canvas(root, bg="white", height=150, width=300)
canvas22.bind("<Button-1>", draw_circle)
canvas22.pack(pady=10)
canvas22.create_text(150, 10, text="Task 22: Click to draw circle", anchor="n")

# Task 23: Draw rectangle from two clicks
rect_start = {}

def start_rect(e):
    rect_start["x"] = e.x
    rect_start["y"] = e.y

def end_rect(e):
    canvas23.create_rectangle(rect_start["x"], rect_start["y"], e.x, e.y, outline="red")

canvas23 = tk.Canvas(root, bg="lightyellow", height=150, width=300)
canvas23.bind("<Button-1>", start_rect)
canvas23.bind("<Button-3>", end_rect)  # Right-click for second point
canvas23.pack(pady=10)
canvas23.create_text(150, 10, text="Task 23: Left=Start, Right=End", anchor="n")

# Task 24: Log all mouse events in Text widget
def log_event(event):
    msg = f"{event.type} at ({event.x},{event.y}) on {event.widget}\n"
    text24.insert("end", msg)
    text24.see("end")

frame24 = tk.Frame(root)
frame24.pack(pady=10)
lbl24 = tk.Label(frame24, text="Task 24: Hover or Click in Box")
lbl24.pack()
text24 = tk.Text(frame24, height=6, width=60)
text24.pack()

for event_name in ["<Enter>", "<Leave>", "<Button-1>", "<Motion>"]:
    text24.bind(event_name, log_event)

# Task 25: Entry changes border color on hover
def entry_hover_in(e): entry25.config(highlightbackground="blue", highlightcolor="blue", highlightthickness=2)
def entry_hover_out(e): entry25.config(highlightthickness=0)

entry25 = tk.Entry(root)
entry25.pack(pady=10)
entry25.insert(0, "Task 25: Hover to see border")
entry25.bind("<Enter>", entry_hover_in)
entry25.bind("<Leave>", entry_hover_out)

root.mainloop()
