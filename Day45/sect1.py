import tkinter as tk
from tkinter import ttk
import threading
import time

class ThreadingDemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Multithreading Demo")

        self.status_label = tk.Label(root, text="Ready", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.output_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.output_label.pack()

        self.progress = ttk.Progressbar(root, length=200, mode='determinate')
        self.progress.pack(pady=5)

        self.text_log = tk.Text(root, height=5, width=50)
        self.text_log.pack(pady=5)

        self.stop_flag = threading.Event()

        # Buttons for each task
        tasks = [
            ("1. Start Threaded Task", self.task_1),
            ("2. Show Please Wait", self.task_2),
            ("3. Update Label From Thread", self.task_3),
            ("4. Countdown Timer", self.task_4),
            ("5. Progress Every Second", self.task_5),
            ("6. Simulate File Download", self.task_6),
            ("7. Cancelable Task", self.task_7),
            ("8. Fetch API (Simulated)", self.task_8),
            ("9. Progress Bar Update", self.task_9),
            ("10. Animate Label", self.task_10),
            ("11. UI Freeze Comparison", self.task_11),
            ("12. Thread Logs to Text", self.task_12),
            ("13. Loading Animation", self.task_13),
            ("14. Lambda Thread", self.task_14),
            ("15. Multiple Button Threads", self.task_15),
        ]
        for name, func in tasks:
            tk.Button(root, text=name, command=func, width=30).pack(pady=2)

        tk.Button(root, text="Stop Task", command=self.stop_task, bg="red").pack(pady=5)

    def threaded(self, func, *args):
        t = threading.Thread(target=func, args=args)
        t.daemon = True
        t.start()

    # Task 1
    def task_1(self):
        self.threaded(self.long_task)

    def long_task(self):
        self.update_status("Running long task...")
        time.sleep(5)
        self.update_status("Done!")

    # Task 2
    def task_2(self):
        self.update_status("Please wait...")
        self.threaded(self.fake_work)

    def fake_work(self):
        time.sleep(3)
        self.update_status("Task completed!")

    # Task 3
    def task_3(self):
        def worker():
            time.sleep(2)
            self.root.after(0, lambda: self.output_label.config(text="Fetched Text from Thread"))
        self.threaded(worker)

    # Task 4
    def task_4(self):
        def countdown(n):
            for i in range(n, -1, -1):
                self.root.after(0, lambda i=i: self.output_label.config(text=f"Countdown: {i}"))
                time.sleep(1)
        self.threaded(countdown, 5)

    # Task 5
    def task_5(self):
        def progress_task():
            for i in range(6):
                self.root.after(0, lambda i=i: self.output_label.config(text=f"Progress: {i}/5"))
                time.sleep(1)
        self.threaded(progress_task)

    # Task 6 (Fixed assignment in lambda)
    def task_6(self):
        def download():
            for i in range(1, 101, 10):
                self.root.after(0, lambda i=i: self.progress.config(value=i))
                time.sleep(0.5)
            self.update_status("Download complete!")
        self.threaded(download)

    # Task 7
    def task_7(self):
        self.stop_flag.clear()
        def cancelable():
            for i in range(10):
                if self.stop_flag.is_set():
                    self.update_status("Task canceled.")
                    return
                self.root.after(0, lambda i=i: self.output_label.config(text=f"Running {i}"))
                time.sleep(1)
            self.update_status("Completed cancelable task.")
        self.threaded(cancelable)

    # Task 8
    def task_8(self):
        def fetch_api():
            time.sleep(2)
            data = "Simulated API response"
            self.root.after(0, lambda: self.output_label.config(text=data))
        self.threaded(fetch_api)

    # Task 9 (Fixed assignment in lambda)
    def task_9(self):
        def fill_progress():
            for i in range(101):
                self.root.after(0, lambda i=i: self.progress.config(value=i))
                time.sleep(0.05)
            self.update_status("Progress done.")
        self.threaded(fill_progress)

    # Task 10
    def task_10(self):
        def animate():
            colors = ["red", "green", "blue"]
            for i in range(10):
                self.root.after(0, lambda i=i: self.output_label.config(fg=colors[i % 3]))
                time.sleep(0.3)
            self.update_status("Animation done.")
        self.threaded(animate)

    # Task 11
    def task_11(self):
        def bad_update():
            try:
                self.output_label.config(text="This will freeze")
                time.sleep(3)
                self.output_label.config(text="Updated without after() (WRONG)")
            except Exception as e:
                self.output_label.config(text=str(e))

        def good_update():
            time.sleep(3)
            self.root.after(0, lambda: self.output_label.config(text="Updated with after() (CORRECT)"))

        # Uncomment one at a time to test
        # self.threaded(bad_update)
        self.threaded(good_update)

    # Task 12
    def task_12(self):
        def logger():
            for i in range(5):
                msg = f"Log entry {i}\n"
                self.root.after(0, lambda msg=msg: self.text_log.insert(tk.END, msg))
                time.sleep(1)
        self.threaded(logger)

    # Task 13
    def task_13(self):
        def loading():
            for i in range(6):
                dots = '.' * (i % 4)
                self.root.after(0, lambda d=dots: self.output_label.config(text=f"Loading{d}"))
                time.sleep(0.5)
            self.update_status("Loaded.")
        self.threaded(loading)

    # Task 14
    def task_14(self):
        self.threaded(lambda: (time.sleep(2), self.root.after(0, lambda: self.output_label.config(text="Lambda done"))))

    # Task 15
    def task_15(self):
        def independent_task(n):
            for i in range(3):
                self.root.after(0, lambda i=i, n=n: self.output_label.config(text=f"Button {n}: Step {i}"))
                time.sleep(1)
        for i in range(3):
            self.threaded(independent_task, i + 1)

    def update_status(self, message):
        self.root.after(0, lambda: self.status_label.config(text=message))

    def stop_task(self):
        self.stop_flag.set()
        self.update_status("Stop signal sent.")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = ThreadingDemoApp(root)
    root.mainloop()
