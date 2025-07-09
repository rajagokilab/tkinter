import tkinter as tk

class Tooltip:
    def __init__(self, widget, text, bg="yellow"):
        self.widget = widget
        self.text = text
        self.bg = bg
        self.tipwindow = None

        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tipwindow or not self.text:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 10

        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Remove window decorations
        tw.wm_geometry(f"+{x}+{y}")

        label = tk.Label(tw, text=self.text, justify="left",
                         background=self.bg, relief="solid", borderwidth=1,
                         font=("Arial", 10))
        label.pack(ipadx=5, ipady=3)

    def hide_tip(self, event=None):
        if self.tipwindow:
            self.tipwindow.destroy()
            self.tipwindow = None

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x200")

    btn = tk.Button(root, text="Hover me")
    btn.pack(pady=50)

    Tooltip(btn, "This is a tooltip message!")

    root.mainloop()
