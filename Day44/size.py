import tkinter as tk

class Panel(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.entries = []
        self.buttons = []

        # Create some Entry widgets
        for i in range(3):
            e = tk.Entry(self)
            e.grid(row=i, column=0, padx=5, pady=5, sticky="ew")
            self.entries.append(e)

        # Create some Buttons
        for i in range(3):
            b = tk.Button(self, text=f"Button {i+1}")
            b.grid(row=i, column=1, padx=5, pady=5)
            self.buttons.append(b)

        # Make columns resize nicely
        self.grid_columnconfigure(0, weight=1)

    def set_state(self, state):
        # Disable/enable all entries and buttons
        for widget in self.entries + self.buttons:
            widget.config(state=state)

def toggle_panel():
    global panel_enabled
    panel_enabled = not panel_enabled
    new_state = "normal" if panel_enabled else "disabled"
    panel.set_state(new_state)
    toggle_btn.config(text="Disable Panel" if panel_enabled else "Enable Panel")

root = tk.Tk()
root.title("Resizable Panel with State Controls")
root.geometry("300x180")

panel_enabled = True
panel = Panel(root, borderwidth=2, relief="groove")
panel.pack(fill="x", padx=20, pady=20)

toggle_btn = tk.Button(root, text="Disable Panel", command=toggle_panel)
toggle_btn.pack(pady=10)

root.mainloop()
