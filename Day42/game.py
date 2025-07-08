import tkinter as tk
from tkinter import ttk
import math

# ── helper ────────────────────────────────────────────────────
def create_star(canvas, cx, cy, r, **kwargs):
    """Draw a 5‑point star centred at (cx,cy) with outer‑radius r."""
    points = []
    for i in range(10):
        angle = math.radians(18 + i * 36)          # start at 18°
        radius = r if i % 2 == 0 else r * 0.4       # outer / inner
        x = cx + radius * math.cos(angle)
        y = cy - radius * math.sin(angle)
        points.extend((x, y))
    return canvas.create_polygon(points, **kwargs)

# ── main window ───────────────────────────────────────────────
root = tk.Tk()
root.title("Simple Drawing Game")
root.geometry("700x500")

# ── top controls ──────────────────────────────────────────────
ctrl = tk.Frame(root, pady=6)
ctrl.pack()

tk.Label(ctrl, text="Object:").grid(row=0, column=0, padx=4)
shape_cb = ttk.Combobox(
    ctrl, values=["Star", "Ball", "Square"], state="readonly", width=8
)
shape_cb.current(0)
shape_cb.grid(row=0, column=1, padx=4)

undo_btn = tk.Button(ctrl, text="Undo")
undo_btn.grid(row=0, column=2, padx=8)

# ── canvas ────────────────────────────────────────────────────
CANVAS_W, CANVAS_H = 480, 400
canvas = tk.Canvas(root, bg="white", width=CANVAS_W, height=CANVAS_H)
canvas.pack(side=tk.LEFT, padx=10, pady=10)

# ── log listbox + scrollbar ──────────────────────────────────
log_frame = tk.Frame(root)
log_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=10)

tk.Label(log_frame, text="Draw Log").pack()

log_scroll = tk.Scrollbar(log_frame)
log_scroll.pack(side=tk.RIGHT, fill=tk.Y)

log_box = tk.Listbox(
    log_frame, height=10, width=30, yscrollcommand=log_scroll.set, exportselection=False
)
log_box.pack(side=tk.LEFT, fill=tk.BOTH)
log_scroll.config(command=log_box.yview)

# ── state ─────────────────────────────────────────────────────
drawn_stack = []   # list of canvas item IDs (for undo ↩)

# ── drawing callback ─────────────────────────────────────────
def draw_object(event):
    shape = shape_cb.get()
    x, y = event.x, event.y
    size = 25                              # half‑size / radius
    colour = "black"

    if shape == "Ball":                    # circle
        cid = canvas.create_oval(
            x - size, y - size, x + size, y + size, fill="lightblue", outline=colour
        )
    elif shape == "Square":
        cid = canvas.create_rectangle(
            x - size, y - size, x + size, y + size, fill="lightgreen", outline=colour
        )
    else:                                  # Star
        cid = create_star(canvas, x, y, size, fill="gold", outline=colour)

    drawn_stack.append(cid)
    log_box.insert(tk.END, f"{shape} at ({x}, {y})")
    log_box.see(tk.END)                    # auto‑scroll to latest

# ── undo callback ────────────────────────────────────────────
def undo_last():
    if drawn_stack:
        cid = drawn_stack.pop()
        canvas.delete(cid)
        log_box.delete(tk.END)

# ── bind & configure ─────────────────────────────────────────
canvas.bind("<Button-1>", draw_object)
undo_btn.config(command=undo_last)

root.mainloop()
