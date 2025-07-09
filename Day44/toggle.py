import tkinter as tk

class ToggleSwitch(tk.Frame):
    def __init__(self, master, initial=False, **kwargs):
        super().__init__(master, **kwargs)
        self.state = initial
        self.label = tk.Label(self, text="ON" if self.state else "OFF", width=5, font=("Arial", 12))
        self.btn = tk.Button(self, text="Toggle", command=self.toggle)
        self.label.pack(side="left", padx=5)
        self.btn.pack(side="left")

    def toggle(self):
        self.state = not self.state
        self.label.config(text="ON" if self.state else "OFF")

# Example usage:
root = tk.Tk()
root.title("Custom Toggle Switch Widget")

toggle1 = ToggleSwitch(root)
toggle1.pack(pady=10)

toggle2 = ToggleSwitch(root, initial=True)
toggle2.pack(pady=10)

root.mainloop()
