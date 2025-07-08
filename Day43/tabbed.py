import tkinter as tk
from tkinter import messagebox

class SettingsPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        self.root.geometry("400x300")

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Preferences", command=self.open_preferences)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        self.root.config(menu=menubar)

    def open_preferences(self):
        pref_window = tk.Toplevel(self.root)
        pref_window.title("Preferences")
        pref_window.geometry("350x400")
        pref_window.grab_set()

        # Frame 1: Account Settings
        account_frame = tk.LabelFrame(pref_window, text="Account Settings", padx=10, pady=10)
        account_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(account_frame, text="Username:").grid(row=0, column=0, sticky="e", pady=2)
        username_entry = tk.Entry(account_frame)
        username_entry.grid(row=0, column=1, pady=2)

        tk.Label(account_frame, text="Email:").grid(row=1, column=0, sticky="e", pady=2)
        email_entry = tk.Entry(account_frame)
        email_entry.grid(row=1, column=1, pady=2)

        tk.Label(account_frame, text="Enable 2FA:").grid(row=2, column=0, sticky="e", pady=2)
        two_fa_var = tk.BooleanVar()
        two_fa_check = tk.Checkbutton(account_frame, variable=two_fa_var)
        two_fa_check.grid(row=2, column=1, sticky="w", pady=2)

        # Frame 2: Theme & Appearance
        theme_frame = tk.LabelFrame(pref_window, text="Theme & Appearance", padx=10, pady=10)
        theme_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(theme_frame, text="Theme Color:").grid(row=0, column=0, sticky="e", pady=2)
        theme_entry = tk.Entry(theme_frame)
        theme_entry.grid(row=0, column=1, pady=2)

        dark_mode_var = tk.BooleanVar()
        dark_mode_check = tk.Checkbutton(theme_frame, text="Dark Mode", variable=dark_mode_var)
        dark_mode_check.grid(row=1, column=0, columnspan=2, sticky="w", pady=2)

        # Frame 3: Notifications
        notif_frame = tk.LabelFrame(pref_window, text="Notifications", padx=10, pady=10)
        notif_frame.pack(fill="x", padx=10, pady=5)

        email_notif_var = tk.BooleanVar()
        email_notif_check = tk.Checkbutton(notif_frame, text="Email Notifications", variable=email_notif_var)
        email_notif_check.grid(row=0, column=0, sticky="w", pady=2)

        sms_notif_var = tk.BooleanVar()
        sms_notif_check = tk.Checkbutton(notif_frame, text="SMS Notifications", variable=sms_notif_var)
        sms_notif_check.grid(row=1, column=0, sticky="w", pady=2)

        # Save Button
        save_btn = tk.Button(pref_window, text="Save", command=lambda: self.save_settings(pref_window))
        save_btn.pack(pady=10)

    def save_settings(self, win):
        # For demo: just close and show a confirmation
        messagebox.showinfo("Settings Saved", "Your preferences have been saved.")
        win.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SettingsPanel(root)
    root.mainloop()
