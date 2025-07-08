import tkinter as tk
from tkinter import messagebox

class ThemeSwitcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Theme Switcher App")
        self.root.geometry("400x300")

        self.current_theme = "Light"

        self.create_menu()
        self.create_toolbar()
        self.create_main_frame()
        self.apply_theme(self.current_theme)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Light Theme", command=lambda: self.change_theme("Light"))
        view_menu.add_command(label="Dark Theme", command=lambda: self.change_theme("Dark"))
        menubar.add_cascade(label="View", menu=view_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED)
        toolbar.pack(side="top", fill="x")

        self.theme_btn = tk.Button(toolbar, text="Switch Theme", command=self.toggle_theme)
        self.theme_btn.pack(side="left", padx=5, pady=5)

    def create_main_frame(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.label = tk.Label(self.main_frame, text="Welcome to Theme Switcher!", font=("Arial", 14))
        self.label.pack(pady=20)

        self.text = tk.Text(self.main_frame, height=5)
        self.text.pack(fill="x")

    def apply_theme(self, theme):
        if theme == "Light":
            bg_color = "white"
            fg_color = "black"
            entry_bg = "white"
            entry_fg = "black"
            text_bg = "white"
            text_fg = "black"
            btn_bg = "#e0e0e0"
        else:  # Dark
            bg_color = "#2e2e2e"
            fg_color = "white"
            entry_bg = "#3c3f41"
            entry_fg = "white"
            text_bg = "#3c3f41"
            text_fg = "white"
            btn_bg = "#5a5a5a"

        self.root.config(bg=bg_color)
        self.main_frame.config(bg=bg_color)

        self.label.config(bg=bg_color, fg=fg_color)
        self.text.config(bg=text_bg, fg=text_fg, insertbackground=fg_color)

        self.theme_btn.config(bg=btn_bg, fg=fg_color, activebackground=btn_bg)

    def change_theme(self, theme):
        self.current_theme = theme
        self.apply_theme(theme)

    def toggle_theme(self):
        new_theme = "Dark" if self.current_theme == "Light" else "Light"
        self.change_theme(new_theme)

if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeSwitcherApp(root)
    root.mainloop()
