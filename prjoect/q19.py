import tkinter as tk
from tkinter import ttk

class CountdownTimer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("⏳ Countdown Timer")
        self.geometry("400x250")
        self.resizable(False, False)

        # Variables
        self.total_time = tk.IntVar(value=30)  # seconds
        self.remaining = 0
        self.timer_running = False
        self.timer_id = None

        # Duration Spinbox
        ttk.Label(self, text="Set Duration (seconds):").pack(pady=(20, 5))
        self.spin = ttk.Spinbox(self, from_=5, to=600, textvariable=self.total_time, width=10)
        self.spin.pack()

        # Canvas for bar
        self.canvas_width = 350
        self.canvas_height = 30
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg="lightgray")
        self.canvas.pack(pady=20)
        self.bar = self.canvas.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="green")

        # Remaining time label
        self.time_label = ttk.Label(self, text="Time Remaining: 00:00", font=("Arial", 14))
        self.time_label.pack()

        # Buttons frame
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)

        self.start_btn = ttk.Button(btn_frame, text="Start", command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = ttk.Button(btn_frame, text="Pause", command=self.pause, state="disabled")
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = ttk.Button(btn_frame, text="Reset", command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def start(self):
        if not self.timer_running:
            if self.remaining == 0:
                self.remaining = self.total_time.get()
                if self.remaining <= 0:
                    return
            self.timer_running = True
            self.start_btn.config(state="disabled")
            self.pause_btn.config(state="normal")
            self.spin.config(state="disabled")
            self.countdown()

    def pause(self):
        if self.timer_running:
            self.timer_running = False
            if self.timer_id:
                self.after_cancel(self.timer_id)
            self.start_btn.config(state="normal")
            self.pause_btn.config(state="disabled")
            self.spin.config(state="normal")

    def reset(self):
        self.timer_running = False
        if self.timer_id:
            self.after_cancel(self.timer_id)
        self.remaining = 0
        self.start_btn.config(state="normal")
        self.pause_btn.config(state="disabled")
        self.spin.config(state="normal")
        self.time_label.config(text="Time Remaining: 00:00")
        # Reset bar to full width
        self.canvas.coords(self.bar, 0, 0, self.canvas_width, self.canvas_height)

    def countdown(self):
        if self.remaining > 0 and self.timer_running:
            minutes = self.remaining // 60
            seconds = self.remaining % 60
            self.time_label.config(text=f"Time Remaining: {minutes:02d}:{seconds:02d}")

            # Calculate bar length proportional to remaining time
            bar_length = (self.remaining / self.total_time.get()) * self.canvas_width
            self.canvas.coords(self.bar, 0, 0, bar_length, self.canvas_height)

            self.remaining -= 1
            self.timer_id = self.after(1000, self.countdown)
        else:
            self.timer_running = False
            self.start_btn.config(state="normal")
            self.pause_btn.config(state="disabled")
            self.spin.config(state="normal")
            if self.remaining == 0:
                self.time_label.config(text="Time's up!")
                # Bar fully shrunk
                self.canvas.coords(self.bar, 0, 0, 0, self.canvas_height)

if __name__ == "__main__":
    CountdownTimer().mainloop()
