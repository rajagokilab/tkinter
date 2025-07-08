import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation & Events")
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack()

# ⚡ 11. Animate a rectangle moving left to right
rect = canvas.create_rectangle(10, 20, 60, 70, fill="blue")

def move_rect():
    canvas.move(rect, 5, 0)
    x1, y1, x2, y2 = canvas.coords(rect)
    if x2 < 500:
        root.after(30, move_rect)

move_rect()

#  ⚡ 12. Animate a circle bouncing off canvas borders
circle = canvas.create_oval(200, 200, 230, 230, fill="red")
dx, dy = 3, 2

def bounce():
    global dx, dy
    x1, y1, x2, y2 = canvas.coords(circle)
    if x1 <= 0 or x2 >= 500:
        dx = -dx
    if y1 <= 0 or y2 >= 400:
        dy = -dy
    canvas.move(circle, dx, dy)
    root.after(20, bounce)

bounce()

# ⚡ 13. Animate multiple shapes at different speeds
oval1 = canvas.create_oval(100, 300, 130, 330, fill="green")
oval2 = canvas.create_oval(300, 300, 330, 330, fill="orange")

def move_oval1():
    canvas.move(oval1, 2, 0)
    root.after(50, move_oval1)

def move_oval2():
    canvas.move(oval2, -3, 0)
    root.after(30, move_oval2)

move_oval1()
move_oval2()

# ⚡ 14. Animate and stop with a button
moving_rect = canvas.create_rectangle(10, 100, 60, 140, fill="purple")
is_animating = True

def move_toggle():
    def animate():
        if is_animating:
            canvas.move(moving_rect, 4, 0)
            root.after(40, animate)
    animate()

def toggle_animation():
    global is_animating
    is_animating = not is_animating
    if is_animating:
        move_toggle()

btn = tk.Button(root, text="Start/Stop Animation", command=toggle_animation)
btn.pack()

move_toggle()

# ⚡ 15. Animate along a diagonal path
diag = canvas.create_rectangle(10, 350, 40, 380, fill="brown")

def move_diag():
    canvas.move(diag, 2, -1.5)
    root.after(25, move_diag)

move_diag()

# 🖱️ 16. Click to draw circle
def draw_circle(event):
    r = 10
    canvas.create_oval(event.x - r, event.y - r, event.x + r, event.y + r, fill="cyan")

canvas.bind("<Button-1>", draw_circle)

# 🖱️ 17. Double-click to draw rectangle
def draw_rectangle(event):
    canvas.create_rectangle(event.x, event.y, event.x + 40, event.y + 30, fill="yellow")

canvas.bind("<Double-1>", draw_rectangle)

# 🖱️ 18. Show mouse coordinates on click
def show_coords(event):
    print(f"Mouse clicked at ({event.x}, {event.y})")

canvas.bind("<Button-3>", show_coords)  # Right click

# 🖱️ 19. Move shape to clicked position
mover = canvas.create_oval(250, 50, 280, 80, fill="pink")

def move_to_click(event):
    x, y = event.x, event.y
    canvas.coords(mover, x-15, y-15, x+15, y+15)

canvas.bind("<Button-2>", move_to_click)  # Middle click

# 🖱️ 20. Change color on hover
hover_shape = canvas.create_rectangle(400, 20, 450, 70, fill="gray")
canvas.tag_bind(hover_shape, "<Enter>", lambda e: canvas.itemconfig(hover_shape, fill="red"))
canvas.tag_bind(hover_shape, "<Leave>", lambda e: canvas.itemconfig(hover_shape, fill="gray"))

root.mainloop()
