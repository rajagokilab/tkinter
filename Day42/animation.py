import tkinter as tk

# Main window
root = tk.Tk()
root.title("Animation Playground")
root.geometry("500x400")

# === Control Frame ===
controls = tk.Frame(root)
controls.pack(pady=10)

# Speed Control Spinbox
tk.Label(controls, text="Speed (ms):").pack(side=tk.LEFT)
speed_var = tk.IntVar(value=50)
speed_spin = tk.Spinbox(controls, from_=10, to=500, increment=10, textvariable=speed_var, width=5)
speed_spin.pack(side=tk.LEFT, padx=5)

# Pause / Resume Buttons
is_paused = False

def pause():
    global is_paused
    is_paused = True

def resume():
    global is_paused
    is_paused = False

tk.Button(controls, text="Pause", command=pause).pack(side=tk.LEFT, padx=5)
tk.Button(controls, text="Resume", command=resume).pack(side=tk.LEFT)

# === Canvas ===
canvas = tk.Canvas(root, bg="lightyellow", width=480, height=250)
canvas.pack(pady=10)

# Draw a rectangle
rect = canvas.create_rectangle(10, 100, 60, 150, fill="blue")

# === Coordinates Label ===
coord_label = tk.Label(root, text="X: 10, Y: 100", font=("Arial", 12))
coord_label.pack()

# === Animation Function ===
dx = 5  # Movement step

def animate():
    global is_paused
    if not is_paused:
        canvas.move(rect, dx, 0)
        x1, y1, x2, y2 = canvas.coords(rect)

        # Bounce back if hitting the wall
        if x2 >= canvas.winfo_width() or x1 <= 0:
            global dx
            dx = -dx

        coord_label.config(text=f"X: {int(x1)}, Y: {int(y1)}")
    root.after(speed_var.get(), animate)

animate()

root.mainloop()
