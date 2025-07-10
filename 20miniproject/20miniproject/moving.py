import tkinter as tk

# Initial state variables
moving = False
rect_id = None
x_speed = 5
y_speed = 0

def start_animation():
    global moving
    moving = True
    animate()

def stop_animation():
    global moving
    moving = False

def animate():
    global rect_id
    if not moving:
        return

    delay = int(speed_spinbox.get())
    canvas.move(rect_id, x_speed, y_speed)
    
    # Get new coordinates
    coords = canvas.coords(rect_id)
    x, y = int(coords[0]), int(coords[1])
    coord_label.config(text=f"X: {x}, Y: {y}")

    # Wrap-around when reaching canvas end
    if coords[2] > 500:
        canvas.move(rect_id, -500, 0)

    root.after(delay, animate)

# ==== Main Window ====
root = tk.Tk()
root.title("Animated Moving Object")
root.geometry("550x400")

# ==== Canvas ====
canvas = tk.Canvas(root, width=500, height=250, bg="white")
canvas.pack(pady=10)

# Create rectangle (x1, y1, x2, y2)
rect_id = canvas.create_rectangle(10, 100, 60, 150, fill="blue")

# ==== Controls Frame ====
controls = tk.Frame(root)
controls.pack(pady=10)

# Speed Spinbox
tk.Label(controls, text="Speed (ms delay):").pack(side="left", padx=5)
speed_spinbox = tk.Spinbox(controls, from_=10, to=1000, increment=10, width=5)
speed_spinbox.pack(side="left")
speed_spinbox.delete(0, tk.END)
speed_spinbox.insert(0, "50")

# Start/Stop Buttons
start_btn = tk.Button(controls, text="Start", command=start_animation)
start_btn.pack(side="left", padx=10)

stop_btn = tk.Button(controls, text="Stop", command=stop_animation)
stop_btn.pack(side="left", padx=10)

# ==== Coordinate Label ====
coord_label = tk.Label(root, text="X: 10, Y: 100", font=("Arial", 12))
coord_label.pack()

root.mainloop()
