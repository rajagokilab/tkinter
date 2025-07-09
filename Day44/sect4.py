import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Custom Widgets (Tasks 36–45)")
root.geometry("600x1000")


# Task 36: Label + Button
class LabelButtonWidget(tk.Frame):
    def __init__(self, master, text="Hello"):
        super().__init__(master)
        self.label = tk.Label(self, text=text)
        self.button = tk.Button(self, text="Click Me", command=self.say_hi)
        self.label.pack(side="left", padx=5)
        self.button.pack(side="left", padx=5)

    def say_hi(self):
        self.label.config(text="Clicked!")


# Task 37: Label updates as you type
class LiveLabelEntry(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label = tk.Label(self, text="Type something...")
        self.entry = tk.Entry(self)
        self.entry.bind("<KeyRelease>", self.update_label)
        self.label.pack()
        self.entry.pack()

    def update_label(self, event=None):
        self.label.config(text=self.entry.get())


# Task 38: OK/Cancel buttons with handlers
class OkCancelButtons(tk.Frame):
    def __init__(self, master, on_ok=None, on_cancel=None):
        super().__init__(master)
        self.ok_btn = tk.Button(self, text="OK", command=on_ok)
        self.cancel_btn = tk.Button(self, text="Cancel", command=on_cancel)
        self.ok_btn.pack(side="left", padx=5)
        self.cancel_btn.pack(side="left", padx=5)


# Task 39: SearchBox widget
class SearchBox(tk.Frame):
    def __init__(self, master, on_search=None):
        super().__init__(master)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="Search", command=lambda: on_search(self.entry.get()) if on_search else None)
        self.entry.pack(side="left", fill="x", expand=True)
        self.button.pack(side="left")


# Task 40: Calculator row (2 entries + operator + result)
class CalculatorRow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.num1 = tk.Entry(self, width=5)
        self.num2 = tk.Entry(self, width=5)
        self.operator = ttk.Combobox(self, values=["+", "-", "*", "/"], width=3)
        self.operator.set("+")
        self.result_label = tk.Label(self, text="=")
        self.calc_btn = tk.Button(self, text="=", command=self.calculate)

        self.num1.pack(side="left")
        self.operator.pack(side="left")
        self.num2.pack(side="left")
        self.calc_btn.pack(side="left")
        self.result_label.pack(side="left", padx=5)

    def calculate(self):
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            op = self.operator.get()
            result = eval(f"{a}{op}{b}")
            self.result_label.config(text=f"= {result}")
        except:
            self.result_label.config(text="Error")


# Task 41: Login form
class LoginWidget(tk.Frame):
    def __init__(self, master, on_submit=None):
        super().__init__(master)
        self.username = tk.Entry(self)
        self.password = tk.Entry(self, show="*")
        self.submit_btn = tk.Button(self, text="Login", command=self.submit)

        self.username.insert(0, "Username")
        self.password.insert(0, "Password")

        self.username.pack(pady=2)
        self.password.pack(pady=2)
        self.submit_btn.pack(pady=2)
        self.on_submit = on_submit

    def submit(self):
        if self.on_submit:
            self.on_submit(self.username.get(), self.password.get())


# Task 42: Rating bar (5 stars)
class RatingBar(tk.Frame):
    def __init__(self, master, max_stars=5):
        super().__init__(master)
        self.rating = 0
        self.stars = []
        for i in range(max_stars):
            btn = tk.Button(self, text="☆", command=lambda i=i: self.set_rating(i + 1), font=("Arial", 14))
            btn.pack(side="left")
            self.stars.append(btn)

    def set_rating(self, val):
        self.rating = val
        for i, btn in enumerate(self.stars):
            btn.config(text="★" if i < val else "☆")


# Task 43: Color picker
class ColorPicker(tk.Frame):
    def __init__(self, master, colors=None, on_pick=None):
        super().__init__(master)
        colors = colors or ["red", "green", "blue", "yellow", "black"]
        self.on_pick = on_pick
        for color in colors:
            btn = tk.Button(self, bg=color, width=3, command=lambda c=color: self.pick(c))
            btn.pack(side="left", padx=2)

    def pick(self, color):
        if self.on_pick:
            self.on_pick(color)


# Task 44: Toolbar with configurable buttons
class Toolbar(tk.Frame):
    def __init__(self, master, buttons):
        super().__init__(master)
        for label, command in buttons.items():
            btn = tk.Button(self, text=label, command=command)
            btn.pack(side="left", padx=3)


# Task 45: LabeledEntry via class inheritance
class LabeledEntry(ttk.Frame):
    def __init__(self, master, label_text="Label", **entry_kwargs):
        super().__init__(master)
        self.label = ttk.Label(self, text=label_text)
        self.entry = ttk.Entry(self, **entry_kwargs)
        self.label.pack(side="left", padx=(0, 5))
        self.entry.pack(side="left", fill="x", expand=True)

    def get(self):
        return self.entry.get()


# Now place all widgets in the window
LabelButtonWidget(root, "Task 36").pack(pady=5)
LiveLabelEntry(root).pack(pady=5)
OkCancelButtons(root, on_ok=lambda: print("OK"), on_cancel=lambda: print("Cancel")).pack(pady=5)
SearchBox(root, on_search=lambda text: print(f"Searched: {text}")).pack(pady=5, fill="x")
CalculatorRow(root).pack(pady=5)
LoginWidget(root, on_submit=lambda u, p: print(f"Login: {u} / {p}")).pack(pady=5)
RatingBar(root).pack(pady=5)
ColorPicker(root, on_pick=lambda c: print(f"Color picked: {c}")).pack(pady=5)
Toolbar(root, {"Open": lambda: print("Open"), "Save": lambda: print("Save"), "Exit": root.quit}).pack(pady=5)
LabeledEntry(root, "Task 45:").pack(pady=5, fill="x")

root.mainloop()
