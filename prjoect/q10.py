import tkinter as tk
from tkinter import ttk, messagebox

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📇 Contact Book Manager")
        self.geometry("400x450")
        self.resizable(False, False)

        # -------- Input Frame --------
        input_frame = ttk.LabelFrame(self, text="Add New Contact", padding=10)
        input_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.name_var, width=30).grid(row=0, column=1, pady=5)

        ttk.Label(input_frame, text="Phone:").grid(row=1, column=0, sticky="w")
        self.phone_var = tk.StringVar()
        ttk.Entry(input_frame, textvariable=self.phone_var, width=30).grid(row=1, column=1, pady=5)

        ttk.Button(input_frame, text="Add Contact", command=self.add_contact).grid(row=2, column=0, columnspan=2, pady=10)

        # -------- Listbox + Scrollbar --------
        list_frame = ttk.LabelFrame(self, text="Contacts", padding=10)
        list_frame.pack(padx=10, pady=5, fill="both", expand=True)

        self.listbox = tk.Listbox(list_frame, height=15)
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # -------- Buttons --------
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Delete Selected ❌", command=self.delete_contact).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Clear All 🧹", command=self.clear_all).grid(row=0, column=1, padx=5)

    def add_contact(self):
        name = self.name_var.get().strip()
        phone = self.phone_var.get().strip()

        if not name or not phone:
            messagebox.showwarning("Missing Info", "Please enter both name and phone number.")
            return

        # Simple phone number validation (digits and basic symbols)
        if not all(c.isdigit() or c in "+- ()" for c in phone):
            messagebox.showerror("Invalid Phone", "Please enter a valid phone number.")
            return

        contact_entry = f"{name} - {phone}"
        self.listbox.insert(tk.END, contact_entry)
        self.name_var.set("")
        self.phone_var.set("")

    def delete_contact(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select a contact to delete.")
            return
        self.listbox.delete(selected[0])

    def clear_all(self):
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all contacts?"):
            self.listbox.delete(0, tk.END)

if __name__ == "__main__":
    ContactBook().mainloop()
