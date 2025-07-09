import tkinter as tk

class Counter(tk.Frame):
    def __init__(self, master, start=0, **kwargs):
        super().__init__(master, **kwargs)
        self.count = start

        self.label = tk.Label(self, text=str(self.count), font=("Arial", 16), width=5)
        self.label.grid(row=0, column=1, padx=10)

        self.inc_btn = tk.Button(self, text="+", command=self.increment, width=3)
        self.inc_btn.grid(row=0, column=2)

        self.dec_btn = tk.Button(self, text="-", command=self.decrement, width=3)
        self.dec_btn.grid(row=0, column=0)

        self.reset_btn = tk.Button(self, text="Reset", command=self.reset)
        self.reset_btn.grid(row=1, column=0, columnspan=3, pady=5)

    def increment(self):
        self.count += 1
        self.label.config(text=str(self.count))

    def decrement(self):
        self.count -= 1
        self.label.config(text=str(self.count))

    def reset(self):
        self.count = 0
        self.label.config(text=str(self.count))

# Example usage
root = tk.Tk()
root.title("Counter Widget")

counter = Counter(root)
counter.pack(pady=20)

root.mainloop()
