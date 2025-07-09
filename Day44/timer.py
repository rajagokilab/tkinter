import tkinter as tk

class TimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timer with Start/Stop")
        self.time = 0  # seconds
        self.running = False
        self.timer_id = None

        self.label = tk.Label(master, text="00:00", font=("Arial", 30))
        self.label.pack(pady=20)

        btn_frame = tk.Frame(master)
        btn_frame.pack()

        self.start_btn = tk.Button(btn_frame, text="Start", command=self.start)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop, state="disabled")
        self.stop_btn.grid(row=0, column=1, padx=5)

        self.reset_btn = tk.Button(btn_frame, text="Reset", command=self.reset)
        self.reset_btn.grid(row=0, column=2, padx=5)

    def update_timer(self):
        if self.running:
            self.time += 1
            mins, secs = divmod(self.time, 60)
            self.label.config(text=f"{mins:02d}:{secs:02d}")
            self.timer_id = self.master.after(1000, self.update_timer)

    def start(self):
        if not self.running:
            self.running = True
            self.update_timer()
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")

    def stop(self):
        if self.running:
            self.running = False
            if self.timer_id:
                self.master.after_cancel(self.timer_id)
                self.timer_id = None
            self.start_btn.config(state="normal")
            self.stop_btn.config(state="disabled")

    def reset(self):
        self.stop()
        self.time = 0
        self.label.config(text="00:00")

root = tk.Tk()
app = TimerApp(root)
root.mainloop()
