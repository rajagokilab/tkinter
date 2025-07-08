import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, filedialog

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("700x400")

        self.contacts = []  # Store contacts as dicts
        self.selected_index = None

        self.create_menu()
        self.create_toolbar()
        self.create_paned_window()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Export", command=self.export_contacts)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        tk.Button(toolbar, text="Add", command=self.add_contact).pack(side="left", padx=5, pady=4)
        tk.Button(toolbar, text="Edit", command=self.edit_contact).pack(side="left", padx=5)
        tk.Button(toolbar, text="Delete", command=self.delete_contact).pack(side="left", padx=5)

    def create_paned_window(self):
        paned = tk.PanedWindow(self.root, sashrelief=tk.RAISED)
        paned.pack(fill="both", expand=True)

        # Left pane: Contact List
        left_frame = tk.Frame(paned)
        tk.Label(left_frame, text="Contacts", font=("Arial", 12, "bold")).pack(pady=5)

        self.contact_listbox = tk.Listbox(left_frame)
        self.contact_listbox.pack(fill="both", expand=True, padx=10, pady=5)
        self.contact_listbox.bind("<<ListboxSelect>>", self.on_select)

        paned.add(left_frame, minsize=200)

        # Right pane: Contact Form
        right_frame = tk.Frame(paned)
        tk.Label(right_frame, text="Contact Details", font=("Arial", 12, "bold")).pack(pady=5)

        form_frame = tk.Frame(right_frame)
        form_frame.pack(padx=10, pady=5, fill="x")

        tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="e")
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(form_frame, text="Phone:").grid(row=1, column=0, sticky="e")
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=2)

        tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="e")
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=2)

        form_frame.columnconfigure(1, weight=1)

        # Disable editing in form initially
        self.set_form_state("disabled")

        paned.add(right_frame)

    def set_form_state(self, state="normal"):
        self.name_entry.config(state=state)
        self.phone_entry.config(state=state)
        self.email_entry.config(state=state)

    def clear_form(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def on_select(self, event):
        if not self.contact_listbox.curselection():
            self.selected_index = None
            self.clear_form()
            self.set_form_state("disabled")
            return
        idx = self.contact_listbox.curselection()[0]
        self.selected_index = idx
        contact = self.contacts[idx]
        self.name_entry.config(state="normal")
        self.phone_entry.config(state="normal")
        self.email_entry.config(state="normal")

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, contact['name'])
        self.phone_entry.delete(0, tk.END)
        self.phone_entry.insert(0, contact['phone'])
        self.email_entry.delete(0, tk.END)
        self.email_entry.insert(0, contact['email'])

        self.set_form_state("disabled")

    def add_contact(self):
        self.clear_form()
        self.set_form_state("normal")
        self.selected_index = None

        def save_new():
            name = self.name_entry.get().strip()
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Name cannot be empty.")
                return
            self.contacts.append({'name': name, 'phone': phone, 'email': email})
            self.refresh_list()
            self.clear_form()
            self.set_form_state("disabled")
            save_btn.destroy()
            cancel_btn.destroy()

        def cancel():
            self.clear_form()
            self.set_form_state("disabled")
            save_btn.destroy()
            cancel_btn.destroy()

        save_btn = tk.Button(self.root, text="Save New", command=save_new)
        cancel_btn = tk.Button(self.root, text="Cancel", command=cancel)
        save_btn.pack(side="bottom", pady=5)
        cancel_btn.pack(side="bottom", pady=5)

    def edit_contact(self):
        if self.selected_index is None:
            messagebox.showinfo("Edit Contact", "Please select a contact to edit.")
            return

        self.set_form_state("normal")

        def save_edit():
            name = self.name_entry.get().strip()
            phone = self.phone_entry.get().strip()
            email = self.email_entry.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Name cannot be empty.")
                return
            self.contacts[self.selected_index] = {'name': name, 'phone': phone, 'email': email}
            self.refresh_list()
            self.set_form_state("disabled")
            save_btn.destroy()
            cancel_btn.destroy()

        def cancel():
            self.on_select(None)
            self.set_form_state("disabled")
            save_btn.destroy()
            cancel_btn.destroy()

        save_btn = tk.Button(self.root, text="Save Edit", command=save_edit)
        cancel_btn = tk.Button(self.root, text="Cancel", command=cancel)
        save_btn.pack(side="bottom", pady=5)
        cancel_btn.pack(side="bottom", pady=5)

    def delete_contact(self):
        if self.selected_index is None:
            messagebox.showinfo("Delete Contact", "Please select a contact to delete.")
            return
        contact = self.contacts[self.selected_index]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete contact '{contact['name']}'?")
        if confirm:
            del self.contacts[self.selected_index]
            self.selected_index = None
            self.refresh_list()
            self.clear_form()
            self.set_form_state("disabled")

    def refresh_list(self):
        self.contact_listbox.delete(0, tk.END)
        for c in self.contacts:
            self.contact_listbox.insert(tk.END, c['name'])

    def export_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Export", "No contacts to export.")
            return

        confirm = messagebox.askyesno("Export Contacts", "Export all contacts to a text file?")
        if confirm:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt")])
            if file_path:
                try:
                    with open(file_path, "w") as f:
                        for c in self.contacts:
                            f.write(f"Name: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\n\n")
                    messagebox.showinfo("Export Successful", f"Contacts exported to:\n{file_path}")
                except Exception as e:
                    messagebox.showerror("Export Failed", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
