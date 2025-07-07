import tkinter as tk
from tkinter import ttk

class EventLogger(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📝 Event Logger Tool")
        self.geometry("500x400")
        self.resizable(False, False)

        # -------- Text widget with Scrollbar --------
        frame = ttk.Frame(self, padding=10)
        frame.pack(fill="both", expand=True)

        self.log_text = tk.Text(frame, wrap="word", state="disabled", height=20)
        self.log_text.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.log_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_text.config(yscrollcommand=scrollbar.set)

        # -------- Clear Button --------
        ttk.Button(self, text="Clear Logs", command=self.clear_logs).pack(pady=10)

        # -------- Bind Events --------
        self.bind_all("<Button-1>", self.log_mouse_click)
        self.bind_all("<Key>", self.log_key_press)

    def log_mouse_click(self, event):
        msg = f"Mouse Click at (x={event.x}, y={event.y})\n"
        self.append_log(msg)

    def log_key_press(self, event):
        # Printable characters or special keys (e.g., Return, Space, Escape)
        key = event.keysym if len(event.char) == 0 else event.char
        msg = f"Key Pressed: {key}\n"
        self.append_log(msg)

    def append_log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message)
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

    def clear_logs(self):
        self.log_text.config(state="normal")
        self.log_text.delete("1.0", tk.END)
        self.log_text.config(state="disabled")

if __name__ == "__main__":
    EventLogger().mainloop()
