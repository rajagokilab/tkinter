import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator with Keyboard Support")
        self.geometry("300x400")
        self.resizable(False, False)

        self.entry = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
        self.entry.pack(fill="x", padx=10, pady=10)
        self.entry.focus_set()

        btns_frame = tk.Frame(self)
        btns_frame.pack(padx=10)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
            ('C',)
        ]

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                btn = tk.Button(btns_frame, text=char, font=("Arial", 18), width=5, height=2,
                                command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, padx=5, pady=5)

        # Bind keys
        self.bind_all("<Key>", self.on_key)

    def on_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            self.calculate()
        else:
            self.entry.insert(tk.END, char)

    def on_key(self, event):
        char = event.char
        keysym = event.keysym

        if char in '0123456789.+-*/':
            self.entry.insert(tk.END, char)
        elif keysym == 'Return':
            self.calculate()
        elif keysym == 'BackSpace':
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])
        elif keysym == 'Escape':
            self.entry.delete(0, tk.END)

    def calculate(self):
        expression = self.entry.get()
        try:
            # Evaluate safely
            result = eval(expression, {"__builtins__": {}})
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Error")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
