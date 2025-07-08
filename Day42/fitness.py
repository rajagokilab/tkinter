import tkinter as tk
from tkinter import ttk

class RepCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Repetition Counter")

        # Variables
        self.total_reps = tk.IntVar(value=10)
        self.current_rep = 0
        self.running = False
        self.anim_step = 0

        # Spinbox for reps
        ttk.Label(root, text="Set repetitions:").pack(pady=5)
        self.spinbox = ttk.Spinbox(root, from_=1, to=100, textvariable=self.total_reps, width=5)
        self.spinbox.pack()

        # Canvas setup
        self.canvas_size = 300
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack(pady=10)

        # Start/Stop button
        self.btn_text = tk.StringVar(value="Start")
        self.start_stop_btn = ttk.Button(root, textvariable=self.btn_text, command=self.start_stop)
        self.start_stop_btn.pack(pady=5)

        # Draw initial stick figure
        self.stick_figure = None
        self.count_text = None
        self.draw_stick_figure(jump_offset=0)
        self.draw_count_text()

    def draw_stick_figure(self, jump_offset):
        """Draw a simple stick figure with a vertical offset for jumping"""
        c = self.canvas
        c.delete("figure")

        base_x = self.canvas_size // 2
        base_y = self.canvas_size // 2 + 50 - jump_offset

        # Head (circle)
        c.create_oval(base_x - 20, base_y - 120, base_x + 20, base_y - 80, fill="black", tags="figure")

        # Body (line)
        c.create_line(base_x, base_y - 80, base_x, base_y, width=3, tags="figure")

        # Arms
        c.create_line(base_x, base_y - 60, base_x - 30, base_y - 30, width=3, tags="figure")
        c.create_line(base_x, base_y - 60, base_x + 30, base_y - 30, width=3, tags="figure")

        # Legs
        c.create_line(base_x, base_y, base_x - 30, base_y + 50, width=3, tags="figure")
        c.create_line(base_x, base_y, base_x + 30, base_y + 50, width=3, tags="figure")

    def draw_count_text(self):
        c = self.canvas
        c.delete("count")
        c.create_text(self.canvas_size//2, 30, text=f"Reps: {self.current_rep}/{self.total_reps.get()}",
                      font=("Helvetica", 20), tags="count")

    def start_stop(self):
        if not self.running:
            # Start counting reps
            self.total_reps_value = self.total_reps.get()
            self.current_rep = 0
            self.running = True
            self.btn_text.set("Stop")
            self.spinbox.config(state="disabled")
            self.animate_jump()
        else:
            # Stop counting
            self.running = False
            self.btn_text.set("Start")
            self.spinbox.config(state="normal")

    def animate_jump(self):
        if not self.running:
            # Reset figure and count display when stopped
            self.draw_stick_figure(jump_offset=0)
            self.draw_count_text()
            return

        # Animate jumping: oscillate jump offset between 0 and 40 pixels up
        jump_positions = [0, 20, 40, 20, 0]  # smooth jump up and down
        jump_offset = jump_positions[self.anim_step]

        self.draw_stick_figure(jump_offset)
        self.draw_count_text()

        self.anim_step += 1
        if self.anim_step >= len(jump_positions):
            self.anim_step = 0
            self.current_rep += 1
            self.draw_count_text()
            if self.current_rep >= self.total_reps_value:
                self.running = False
                self.btn_text.set("Start")
                self.spinbox.config(state="normal")
                return

        self.root.after(100, self.animate_jump)  # 100ms per animation frame

if __name__ == "__main__":
    root = tk.Tk()
    RepCounterApp(root)
    root.mainloop()
