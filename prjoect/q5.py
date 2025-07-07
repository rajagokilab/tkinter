import tkinter as tk
from tkinter import ttk

class ObjectMover(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Animated Object Mover")
        self.geometry("500x300")

        # ---------- Canvas ----------
        self.canvas = tk.Canvas(self, width=460, height=150, bg="white")
        self.canvas.pack(pady=20)
        
        # Create a rectangle
        self.rect = self.canvas.create_rectangle(10, 60, 60, 110, fill="tomato")

        # ---------- Controls ----------
        control_frame = ttk.Frame(self)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="Speed (ms):").grid(row=0, column=0, padx=5)

        self.speed_var = tk.IntVar(value=20)
        self.speed_spin = ttk.Spinbox(control_frame, from_=1, to=1000, textvariable=self.speed_var, width=6)
        self.speed_spin.grid(row=0, column=1, padx=5)

        self.start_btn = ttk.Button(control_frame, text="Start ▶", command=self.start_animation)
        self.start_btn.grid(row=0, column=2, padx=10)

        self.stop_btn = ttk.Button(control_frame, text="Stop ⏸", command=self.stop_animation, state="disabled")
        self.stop_btn.grid(row=0, column=3, padx=10)

        # ---------- Animation control ----------
        self.animating = False
        self.direction = 1  # 1 = right, -1 = left

    def start_animation(self):
        if not self.animating:
            self.animating = True
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            self.animate()

    def stop_animation(self):
        self.animating = False
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")

    def animate(self):
        if not self.animating:
            return

        speed = self.speed_var.get()
        dx = 5 * self.direction
        self.canvas.move(self.rect, dx, 0)

        # Bounce logic
        x1, y1, x2, y2 = self.canvas.coords(self.rect)
        if x2 >= self.canvas.winfo_width() or x1 <= 0:
            self.direction *= -1  # reverse direction

        self.after(speed, self.animate)

if __name__ == "__main__":
    ObjectMover().mainloop()
