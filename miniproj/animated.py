import tkinter as tk

class AnimatedRectangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Animated Moving Object")

        # Canvas
        self.canvas = tk.Canvas(root, width=400, height=200, bg="white")
        self.canvas.pack(pady=10)

        # Create rectangle
        self.rect_size = 50
        self.x = 0
        self.y = 75
        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.rect_size, self.y + self.rect_size, fill="blue")

        # Controls frame
        control_frame = tk.Frame(root)
        control_frame.pack(pady=5)

        tk.Label(control_frame, text="Speed (ms delay):").grid(row=0, column=0, padx=5)
        self.speed_spinbox = tk.Spinbox(control_frame, from_=10, to=500, width=5)
        self.speed_spinbox.grid(row=0, column=1, padx=5)
        self.speed_spinbox.delete(0, tk.END)
        self.speed_spinbox.insert(0, "50")

        self.start_button = tk.Button(control_frame, text="Start", command=self.start_animation)
        self.start_button.grid(row=0, column=2, padx=5)
        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop_animation, state="disabled")
        self.stop_button.grid(row=0, column=3, padx=5)

        # Coordinates label
        self.coord_label = tk.Label(root, text=f"Coordinates: X={self.x}, Y={self.y}")
        self.coord_label.pack()

        self.animating = False

    def animate(self):
        if not self.animating:
            return

        speed = int(self.speed_spinbox.get())
        self.x += 5
        if self.x > self.canvas.winfo_width():
            self.x = -self.rect_size  # reset to start from left

        self.canvas.coords(self.rect, self.x, self.y, self.x + self.rect_size, self.y + self.rect_size)
        self.coord_label.config(text=f"Coordinates: X={self.x}, Y={self.y}")

        self.root.after(speed, self.animate)

    def start_animation(self):
        if not self.animating:
            self.animating = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.animate()

    def stop_animation(self):
        self.animating = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

root = tk.Tk()
app = AnimatedRectangleApp(root)
root.mainloop()
