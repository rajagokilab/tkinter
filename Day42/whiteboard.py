import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ── main window ───────────────────────────────────────────────
root = tk.Tk()
root.title("Canvas Whiteboard with Shape Insertion")
root.geometry("900x550")

# ── data structures ───────────────────────────────────────────
drawn_items   = []           # parallel to log_listbox: [{'id', 'shape', 'coords', 'color'}]
undo_stack    = []           # list of actions; each action is dict
redo_stack    = []

# ── helper: create shape on canvas ────────────────────────────
def create_shape(shape_type, x, y, color, size=50):
    if shape_type == "Circle":
        return canvas.create_oval(
            x - size, y - size, x + size, y + size, fill=color, outline="black"
        )
    else:  # Rectangle
        return canvas.create_rectangle(
            x - size, y - size, x + size, y + size, fill=color, outline="black"
        )

# ── draw callback ─────────────────────────────────────────────
def draw(event):
    if not shape_listbox.curselection():
        messagebox.showwarning("Select Shape", "Choose a shape in the list first.")
        return

    shape_type = shape_listbox.get(shape_listbox.curselection())
    color      = color_cb.get()
    cid        = create_shape(shape_type, event.x, event.y, color)

    info = {
        "id": cid,
        "shape": shape_type,
        "coords": canvas.coords(cid),   # (x1, y1, x2, y2)
        "color": color,
    }
    drawn_items.append(info)
    log_listbox.insert(tk.END, f"{shape_type} @ ({event.x},{event.y})")
    log_listbox.itemconfig(tk.END, fg=color)

    # register action for undo
    undo_stack.append({"act": "draw", "info": info})
    redo_stack.clear()

# ── delete selected shape ─────────────────────────────────────
def delete_selected():
    sel = log_listbox.curselection()
    if not sel:
        return
    idx = sel[0]
    info = drawn_items.pop(idx)
    canvas.delete(info["id"])
    log_listbox.delete(idx)

    undo_stack.append({"act": "delete", "info": info, "index": idx})
    redo_stack.clear()

# ── undo / redo logic ─────────────────────────────────────────
def undo():
    if not undo_stack:
        return
    action = undo_stack.pop()
    if action["act"] == "draw":
        # simply remove last drawn
        info = action["info"]
        idx  = drawn_items.index(info)
        canvas.delete(info["id"])
        log_listbox.delete(idx)
        drawn_items.remove(info)
        redo_stack.append(action)
    elif action["act"] == "delete":
        info, idx = action["info"], action["index"]
        cid = create_shape(info["shape"], (info["coords"][0] + info["coords"][2]) / 2,
                           (info["coords"][1] + info["coords"][3]) / 2, info["color"])
        info["id"] = cid
        drawn_items.insert(idx, info)
        log_listbox.insert(idx, f"{info['shape']} @ (? , ?)")
        log_listbox.itemconfig(idx, fg=info["color"])
        redo_stack.append(action)

def redo():
    if not redo_stack:
        return
    action = redo_stack.pop()
    # perform the same steps as original, pushing back onto undo_stack
    if action["act"] == "draw":
        info = action["info"]
        cid = create_shape(info["shape"],
                           (info["coords"][0] + info["coords"][2]) / 2,
                           (info["coords"][1] + info["coords"][3]) / 2,
                           info["color"])
        info["id"] = cid
        drawn_items.append(info)
        log_listbox.insert(tk.END, f"{info['shape']} @ (? , ?)")
        log_listbox.itemconfig(tk.END, fg=info["color"])
        undo_stack.append(action)
    elif action["act"] == "delete":
        delete_selected()
        undo_stack.append(action)

# ── optional: save canvas ─────────────────────────────────────
def save_canvas():
    file = filedialog.asksaveasfilename(defaultextension=".ps",
                                        filetypes=[("PostScript files", "*.ps")])
    if file:
        canvas.postscript(file=file)
        messagebox.showinfo("Saved", f"Canvas saved to {file}")

# ── UI layout ─────────────────────────────────────────────────
top = tk.Frame(root)
top.pack(pady=5)

# Combobox for colors
tk.Label(top, text="Color:").pack(side=tk.LEFT, padx=4)
color_cb = ttk.Combobox(top, values=["red", "green", "blue", "orange",
                                     "purple", "black"], state="readonly", width=10)
color_cb.current(0)
color_cb.pack(side=tk.LEFT)

# Action buttons
for txt, cmd in [("Undo", undo), ("Redo", redo),
                 ("Delete", delete_selected), ("Save", save_canvas)]:
    tk.Button(top, text=txt, command=cmd).pack(side=tk.LEFT, padx=4)

main = tk.Frame(root)
main.pack(fill=tk.BOTH, expand=True, pady=8)

# Left: shape‑chooser Listbox
left = tk.Frame(main)
left.pack(side=tk.LEFT, padx=8, fill=tk.Y)

tk.Label(left, text="Shapes").pack()
shape_listbox = tk.Listbox(left, height=4, exportselection=False)
shape_listbox.pack()
for s in ("Circle", "Rectangle"):
    shape_listbox.insert(tk.END, s)
shape_listbox.selection_set(0)

# Centre: Canvas
canvas = tk.Canvas(main, bg="white", width=600, height=450)
canvas.pack(side=tk.LEFT, padx=8)
canvas.bind("<Button-1>", draw)

# Right: log Listbox with scrollbar
right = tk.Frame(main)
right.pack(side=tk.LEFT, padx=8, fill=tk.Y)

tk.Label(right, text="Drawn Shapes").pack()
sb = tk.Scrollbar(right, orient=tk.VERTICAL)
log_listbox = tk.Listbox(right, height=25, width=25, yscrollcommand=sb.set)
sb.config(command=log_listbox.yview)
sb.pack(side=tk.RIGHT, fill=tk.Y)
log_listbox.pack(side=tk.LEFT)

root.mainloop()
