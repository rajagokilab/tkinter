import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk

class EmailClientUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Client")
        self.root.geometry("800x500")

        self.create_menu()
        self.create_toolbar()
        self.create_panes()

    # Menu Bar
    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Compose", command=self.open_compose_dialog)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    # Toolbar
    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#e0e0e0")
        toolbar.pack(side="top", fill="x")

        tk.Button(toolbar, text="Reply", command=lambda: self.show_action("Reply")).pack(side="left", padx=5, pady=4)
        tk.Button(toolbar, text="Forward", command=lambda: self.show_action("Forward")).pack(side="left", padx=5)
        tk.Button(toolbar, text="Delete", command=lambda: self.show_action("Delete")).pack(side="left", padx=5)

    # PanedWindow: Left (Inbox), Right (Message Preview)
    def create_panes(self):
        paned = tk.PanedWindow(self.root, sashrelief=tk.RAISED)
        paned.pack(fill="both", expand=True)

        # Left Pane: Inbox List
        inbox_frame = tk.Frame(paned)
        tk.Label(inbox_frame, text="Inbox", font=("Arial", 12, "bold")).pack(pady=5)
        self.inbox_list = tk.Listbox(inbox_frame)
        self.inbox_list.pack(fill="both", expand=True, padx=10, pady=5)
        self.inbox_list.bind("<<ListboxSelect>>", self.preview_message)

        # Dummy inbox items
        for i in range(1, 11):
            self.inbox_list.insert(tk.END, f"Email {i}: Subject Line")

        paned.add(inbox_frame)

        # Right Pane: Message Preview
        preview_frame = tk.Frame(paned)
        tk.Label(preview_frame, text="Message Preview", font=("Arial", 12, "bold")).pack(pady=5)
        self.preview_text = tk.Text(preview_frame, wrap="word")
        self.preview_text.pack(fill="both", expand=True, padx=10, pady=5)
        paned.add(preview_frame)

    # Show selected email content
    def preview_message(self, event):
        selection = self.inbox_list.curselection()
        if selection:
            index = selection[0]
            self.preview_text.delete("1.0", tk.END)
            self.preview_text.insert(tk.END, f"This is the content of Email {index+1}.\n\n(Placeholder content here)")

    # Dummy button actions
    def show_action(self, action):
        messagebox.showinfo(action, f"{action} action triggered.")

    # Compose dialog
    def open_compose_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Compose Email")
        dialog.geometry("500x400")
        dialog.grab_set()

        # Layout
        tk.Label(dialog, text="To:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        to_entry = tk.Entry(dialog, width=50)
        to_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(dialog, text="Subject:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        subject_entry = tk.Entry(dialog, width=50)
        subject_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(dialog, text="Body:").grid(row=2, column=0, sticky="ne", padx=5, pady=5)
        body_text = tk.Text(dialog, height=15, width=50)
        body_text.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        def send_email():
            to = to_entry.get()
            subject = subject_entry.get()
            body = body_text.get("1.0", tk.END).strip()
            if not to:
                messagebox.showwarning("Missing Info", "Please enter recipient email.")
                return
            messagebox.showinfo("Email Sent", f"To: {to}\nSubject: {subject}")
            dialog.destroy()

        btn_frame = tk.Frame(dialog)
        btn_frame.grid(row=3, column=1, sticky="e", pady=10)
        tk.Button(btn_frame, text="Send", command=send_email).pack(side="right", padx=5)
        tk.Button(btn_frame, text="Cancel", command=dialog.destroy).pack(side="right")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EmailClientUI(root)
    root.mainloop()
