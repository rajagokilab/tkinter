import tkinter as tk
from tkinter import ttk
import time
import threading
import platform

try:
    import winsound  # For Windows beep
except ImportError:
    winsound = None

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        # Variables
        self.total_time = 10  # default seconds
        self.remaining = 0
        self.running = False
        self.paused = False

        # Spinbox to set time in seconds (1 to 300)
        ttk.Label(root, text="Set time (seconds):").pack(pady=5)
        self.time_var = tk.IntVar(value=10)
        self.spinbox = ttk.Spinbox(root, from_=1, to=300, textvariable=self.time_var, width=5)
        self.spinbox.pack()

        # Canvas for drawing circle and text
        self.canvas_size = 200
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size)
        self.canvas.pack(pady=10)

        # Draw full circle initially
        self.circle = self.canvas.create_oval(10, 10, self.canvas_size - 10, self.canvas_size - 10, fill="skyblue")

        # Text for countdown seconds
        self.text = self.canvas.create_text(self.canvas_size//2, self.canvas_size//2, text=str(self.total_time), font=("Helvetica", 36))

        # Start/Pause button
        self.btn_text = tk.StringVar(value="Start")
        self.start_pause_btn = ttk.Button(root, textvariable=self.btn_text, command=self.start_pause)
        self.start_pause_btn.pack(pady=5)

        # For animation timing
        self.start_time = None

    def start_pause(self):
        if not self.running:
            # Start timer
            self.total_time = self.time_var.get()
            self.remaining = self.total_time
            self.running = True
            self.paused = False
            self.btn_text.set("Pause")
            self.start_time = time.time()
            self.update_timer()
        elif self.running and not self.paused:
            # Pause timer
            self.paused = True
            self.btn_text.set("Resume")
        elif self.running and self.paused:
            # Resume timer
            self.paused = False
            self.btn_text.set("Pause")
            # Adjust start_time to account for pause duration
            self.start_time = time.time() - (self.total_time - self.remaining)
            self.update_timer()

    def update_timer(self):
        if self.running and not self.paused:
            elapsed = time.time() - self.start_time
            self.remaining = max(self.total_time - elapsed, 0)
            self.canvas.itemconfig(self.text, text=str(int(self.remaining)+1))  # +1 to show better countdown

            # Update circle shrinking
            fraction = self.remaining / self.total_time if self.total_time > 0 else 0
            margin = 10 + (1 - fraction) * (self.canvas_size//2 - 10)
            self.canvas.coords(self.circle, margin, margin, self.canvas_size - margin, self.canvas_size - margin)

            if self.remaining <= 0:
                self.running = False
                self.btn_text.set("Start")
                self.alert_sound()
                return
            self.root.after(50, self.update_timer)

    def alert_sound(self):
        # Cross-platform simple beep
        if platform.system() == "Windows" and winsound:
            winsound.Beep(1000, 500)  # frequency, duration(ms)
        else:
            # Mac/Linux terminal beep
            print('\a')

if __name__ == "__main__":
    root = tk.Tk()
    TimerApp(root)
    root.mainloop()
