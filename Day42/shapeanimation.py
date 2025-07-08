import tkinter as tk
from tkinter import ttk
import random

# ── main window ────────────────────────────────────────────────
root = tk.Tk()
root.title("Shape Animation Editor")
root.geometry("700x500")

# ── control panel ──────────────────────────────────────────────
ctrl = tk.Frame(root, pady=5)
ctrl.pack()

tk.Label(ctrl, text="Shape:").grid(row=0, column=0, padx=4)
shape_cb = ttk.Combobox(
    ctrl, values=["Rectangle", "Circle", "Triangle"], state="readonly", width=10
)
shape_cb.current(0)
shape_cb.grid(row=0, column=1)

tk.Label(ctrl, text="Direction:").grid(row=0, column=2, padx=4)
dir_cb = ttk.Combobox(
    ctrl, values=["Right", "Left", "Up", "Down"], state="readonly", width=8
)
dir_cb.current(0)
dir_cb.grid(row=0, column=3)

tk.Label(ctrl, text="Delay (ms):").grid(row=0, column=4, padx=4)
delay_spin = tk.Spinbox(ctrl, from_=10, to=400, increment=10, width=5)
delay_spin.delete(0, tk.END)
delay_spin.insert(0, "50")
delay_spin.grid(row=0, column=5)

add_btn = tk.Button(ctrl, text="Add Shape")
add_btn.grid(row=0, column=6, padx=6)

pause_btn = tk.Button(ctrl, text="Pause All")
pause_btn.grid(row=0, column=7, padx=2)
resume_btn = tk.Button(ctrl, text="Resume All")
resume_btn.grid(row=0, column=8, padx=2)

# ── canvas ─────────────────────────────────────────────────────
CANVAS_W, CANVAS_H = 680, 400
canvas = tk.Canvas(root, bg="white", width=CANVAS_W, height=CANVAS_H)
canvas.pack(pady=8)

# ── data structures ───────────────────────────────────────────
shapes = []   # list of dicts {id, dx, dy, delay, after_id}
paused = False

# ── helpers ────────────────────────────────────────────────────
def make_shape():
    """Create a canvas item according to current combobox choices."""
    size = 40
    x = random.randint(size, CANVAS_W - size)
    y = random.randint(size, CANVAS_H - size)
    shape_type = shape_cb.get()

    if shape_type == "Rectangle":
        item = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill=random_color())
    elif shape_type == "Circle":
        item = canvas.create_oval(x - size, y - size, x + size, y + size, fill=random_color())
    else:  # Triangle
        item = canvas.create_polygon(
            x, y - size,
            x + size, y + size,
            x - size, y + size,
            fill=random_color()
        )
    return item

def vector_from_direction(direction, step=4):
    return {
        "Right": (step, 0),
        "Left": (-step, 0),
        "Up": (0, -step),
        "Down": (0, step),
    }[direction]

def random_color():
    return random.choice(["lightcoral", "lightskyblue", "khaki",
                          "palegreen", "plum", "salmon"])

# ── animation logic ────────────────────────────────────────────
def animate(idx):
    """Move one shape, then reschedule itself."""
    global paused
    shp = shapes[idx]
    if not paused:
        canvas.move(shp["id"], shp["dx"], shp["dy"])
        bounce_if_needed(shp["id"], shp)
    shp["after_id"] = root.after(shp["delay"], lambda i=idx: animate(i))

def bounce_if_needed(item_id, shp):
    x1, y1, x2, y2 = canvas.coords(item_id)
    if x1 <= 0 or x2 >= CANVAS_W:
        shp["dx"] = -shp["dx"]
    if y1 <= 0 or y2 >= CANVAS_H:
        shp["dy"] = -shp["dy"]

# ── callbacks ──────────────────────────────────────────────────
def add_shape():
    item = make_shape()
    dx, dy = vector_from_direction(dir_cb.get())
    delay = int(delay_spin.get())
    shp = {"id": item, "dx": dx, "dy": dy, "delay": delay, "after_id": None}
    shapes.append(shp)
    idx = len(shapes) - 1
    animate(idx)

def pause_all():
    global paused
    paused = True

def resume_all():
    global paused
    paused = False

# ── bind buttons ───────────────────────────────────────────────
add_btn.config(command=add_shape)
pause_btn.config(command=pause_all)
resume_btn.config(command=resume_all)

# ── run ────────────────────────────────────────────────────────
root.mainloop()
