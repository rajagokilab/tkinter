import tkinter as tk

class FormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Form Submission Dialog")
        self.geometry("300x250")

        tk.Label(self, text="Name:").pack(pady=(20,0))
        self.name_entry = tk.Entry(self)
        self.name_entry.pack(pady=5, padx=20, fill="x")

        tk.Label(self, text="Email:").pack(pady=(10,0))
        self.email_entry = tk.Entry(self)
        self.email_entry.pack(pady=5, padx=20, fill="x")

        tk.Label(self, text="Age:").pack(pady=(10,0))
        self.age_entry = tk.Entry(self)
        self.age_entry.pack(pady=5, padx=20, fill="x")

        submit_btn = tk.Button(self, text="Submit", command=self.open_dialog)
        submit_btn.pack(pady=20)

    def open_dialog(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        age = self.age_entry.get()

        dialog = tk.Toplevel(self)
        dialog.title("Submitted Data")
        dialog.geometry("280x180")
        dialog.grab_set()  # Modal dialog

        tk.Label(dialog, text="Form Data Submitted:", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(dialog, text=f"Name: {name}").pack(pady=5)
        tk.Label(dialog, text=f"Email: {email}").pack(pady=5)
        tk.Label(dialog, text=f"Age: {age}").pack(pady=5)

        close_btn = tk.Button(dialog, text="Close", command=dialog.destroy)
        close_btn.pack(pady=15)

if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
