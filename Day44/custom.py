import tkinter as tk

class Notification(tk.Frame):
    def __init__(self, master, message, bg_color="lightblue", icon="ℹ️", duration=5000, **kwargs):
        super().__init__(master, bg=bg_color, **kwargs)
        self.duration = duration

        self.icon_label = tk.Label(self, text=icon, bg=bg_color, font=("Arial", 16))
        self.icon_label.pack(side="left", padx=(10,5), pady=5)

        self.msg_label = tk.Label(self, text=message, bg=bg_color, font=("Arial", 14))
        self.msg_label.pack(side="left", padx=5, pady=5)

        self.close_btn = tk.Button(self, text="✖", bg=bg_color, relief="flat",
                                   command=self.destroy, font=("Arial", 12), bd=0)
        self.close_btn.pack(side="right", padx=10, pady=5)

        # Place notification at top and fill width
        self.pack(side="top", fill="x")

        # Auto destroy after duration ms
        self.after(self.duration, self.destroy)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    root.title("Notification Demo")

    def show_notification():
        Notification(root, "This is a notification!", bg_color="#90caf9", icon="🔔")

    tk.Button(root, text="Show Notification", command=show_notification).pack(pady=50)

    root.mainloop()
