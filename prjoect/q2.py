import tkinter as tk
from tkinter import messagebox

class PortfolioApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Portfolio Dashboard")
        
        # Set window icon (use a valid .ico path on your machine)
        try:
            self.iconbitmap("icon.ico")  # Replace with a valid icon path
        except:
            print("Icon not found or unsupported on this OS.")

        self.geometry("500x400")
        self.configure(bg="#f5f5f5")

        # ---------- Static labels ----------
        tk.Label(self, text="Full Name:", bg="#f5f5f5").place(x=30, y=30)
        tk.Label(self, text="Email:", bg="#f5f5f5").place(x=30, y=70)
        tk.Label(self, text="Bio:", bg="#f5f5f5").place(x=30, y=110)

        # ---------- Entry fields ----------
        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        self.name_entry = tk.Entry(self, textvariable=self.name_var, width=30)
        self.email_entry = tk.Entry(self, textvariable=self.email_var, width=30)
        self.bio_text = tk.Text(self, height=5, width=38)

        self.name_entry.place(x=100, y=30)
        self.email_entry.place(x=100, y=70)
        self.bio_text.place(x=100, y=110)

        # ---------- Dynamic Labels ----------
        self.display_label = tk.Label(self, text="Your info will appear here...", bg="#e0f7fa", wraplength=400, justify="left")
        self.display_label.place(x=30, y=250)

        # ---------- Button ----------
        tk.Button(self, text="Update Info", command=self.update_display).place(x=200, y=210)

    def update_display(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        bio = self.bio_text.get("1.0", tk.END).strip()

        if not name or not email or not bio:
            messagebox.showwarning("Incomplete", "Please fill out all fields.")
            return

        display_text = f"👤 Name: {name}\n📧 Email: {email}\n📝 Bio: {bio}"
        self.display_label.config(text=display_text)

if __name__ == "__main__":
    PortfolioApp().mainloop()
