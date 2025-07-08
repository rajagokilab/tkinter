import tkinter as tk
from tkinter import messagebox

class EventLoggerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Logger Tool")
        self.root.geometry("500x400")

        self.logging = False

        self.create_menu()
        self.create_toolbar()
        self.create_text_area()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        events_menu = tk.Menu(menubar, tearoff=0)
        events_menu.add_command(label="Start Logging", command=self.start_logging)
        events_menu.add_command(label="Stop Logging", command=self.stop_logging)
        menubar.add_cascade(label="Events", menu=events_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief="raised")
        toolbar.pack(side="top", fill="x")

        clear_btn = tk.Button(toolbar, text="Clear Log", command=self.clear_log)
        clear_btn.pack(side="left", padx=2, pady=2)

    def create_text_area(self):
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=5, pady=5)

        self.text = tk.Text(frame, wrap="word", state="disabled")
        self.text.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, command=self.text.yview)
        scrollbar.pack(side="right", fill="y")

        self.text.config(yscrollcommand=scrollbar.set)

    def start_logging(self):
        if self.logging:
            messagebox.showinfo("Already Logging", "Event logging is already active.")
            return
        self.logging = True
        self.log_event("Event logging started.\n")
        self.root.bind("<Key>", self.log_key)
        self.root.bind("<Button-1>", self.log_click)

    def stop_logging(self):
        if not self.logging:
            messagebox.showinfo("Not Logging", "Event logging is not currently active.")
            return
        self.logging = False
        self.log_event("Event logging stopped.\n")
        self.root.unbind("<Key>")
        self.root.unbind("<Button-1>")

    def clear_log(self):
        self.text.config(state="normal")
        self.text.delete("1.0", "end")
        self.text.config(state="disabled")

    def log_event(self, event_str):
        self.text.config(state="normal")
        self.text.insert("end", event_str)
        self.text.see("end")
        self.text.config(state="disabled")

    def log_key(self, event):
        self.log_event(f"Key pressed: '{event.keysym}' (char: '{event.char}')\n")

    def log_click(self, event):
        self.log_event(f"Mouse click at ({event.x}, {event.y})\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = EventLoggerApp(root)
    root.mainloop()
