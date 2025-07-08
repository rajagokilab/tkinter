import tkinter as tk
from tkinter import ttk, messagebox

class SettingsManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Settings Manager")
        self.root.geometry("600x400")

        self.create_panedwindow()
        self.create_categories()
        self.create_settings_frames()

    def create_panedwindow(self):
        self.paned = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned.pack(fill="both", expand=True)

        # Left pane: categories list
        left_frame = tk.Frame(self.paned, bd=2, relief=tk.SUNKEN)
        self.paned.add(left_frame, minsize=150)

        tk.Label(left_frame, text="Categories", font=("Arial", 12, "bold")).pack(pady=10)

        self.category_listbox = tk.Listbox(left_frame)
        self.category_listbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.category_listbox.bind("<<ListboxSelect>>", self.on_category_select)

        # Right pane: settings area
        self.right_frame = tk.Frame(self.paned, bd=2, relief=tk.SUNKEN)
        self.paned.add(self.right_frame, minsize=400)

    def create_categories(self):
        self.categories = ["Account Settings", "Theme & Appearance", "Notifications"]
        for cat in self.categories:
            self.category_listbox.insert(tk.END, cat)
        self.category_listbox.select_set(0)  # Select first by default

    def create_settings_frames(self):
        # Create frames for each category, hidden by default
        self.frames = {}

        # Account Settings
        frame1 = tk.Frame(self.right_frame)
        tk.Label(frame1, text="Account Settings", font=("Arial", 14)).pack(pady=10)

        tk.Label(frame1, text="Username:").pack(anchor="w", padx=20)
        self.username_var = tk.StringVar(value="user123")
        tk.Entry(frame1, textvariable=self.username_var).pack(fill="x", padx=20)

        self.newsletter_var = tk.BooleanVar()
        tk.Checkbutton(frame1, text="Subscribe to newsletter", variable=self.newsletter_var).pack(anchor="w", padx=20, pady=10)

        self.frames["Account Settings"] = frame1

        # Theme & Appearance
        frame2 = tk.Frame(self.right_frame)
        tk.Label(frame2, text="Theme & Appearance", font=("Arial", 14)).pack(pady=10)

        tk.Label(frame2, text="Font Size:").pack(anchor="w", padx=20)
        self.fontsize_var = tk.IntVar(value=12)
        tk.Spinbox(frame2, from_=8, to=32, textvariable=self.fontsize_var).pack(padx=20, pady=5, anchor="w")

        self.darkmode_var = tk.BooleanVar()
        tk.Checkbutton(frame2, text="Enable Dark Mode", variable=self.darkmode_var).pack(anchor="w", padx=20, pady=10)

        self.frames["Theme & Appearance"] = frame2

        # Notifications
        frame3 = tk.Frame(self.right_frame)
        tk.Label(frame3, text="Notifications", font=("Arial", 14)).pack(pady=10)

        self.emailnotif_var = tk.BooleanVar()
        tk.Checkbutton(frame3, text="Email Notifications", variable=self.emailnotif_var).pack(anchor="w", padx=20, pady=5)

        self.smsnotif_var = tk.BooleanVar()
        tk.Checkbutton(frame3, text="SMS Notifications", variable=self.smsnotif_var).pack(anchor="w", padx=20, pady=5)

        self.frames["Notifications"] = frame3

        # Save button at bottom of right_frame
        self.save_btn = tk.Button(self.right_frame, text="Save Settings", command=self.save_settings)
        self.save_btn.pack(side="bottom", pady=15)

        # Show first frame initially
        self.show_frame("Account Settings")

    def on_category_select(self, event):
        sel = self.category_listbox.curselection()
        if sel:
            cat = self.categories[sel[0]]
            self.show_frame(cat)

    def show_frame(self, category):
        # Hide all frames
        for f in self.frames.values():
            f.pack_forget()
        # Show selected
        frame = self.frames.get(category)
        if frame:
            frame.pack(fill="both", expand=True, padx=10, pady=10)

    def save_settings(self):
        # Here you could save the settings to a file or database
        messagebox.showinfo("Settings Manager", "Settings saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsManager(root)
    root.mainloop()
