import tkinter as tk
from tkinter import ttk, messagebox

class FeedbackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Feedback Collector")

        # Data store for feedback: list of tuples (category, name, message)
        self.feedbacks = []

        # --- Input Frame ---
        input_frame = ttk.Frame(root, padding=10)
        input_frame.grid(row=0, column=0, sticky="ew")

        # Feedback category Combobox
        ttk.Label(input_frame, text="Category:").grid(row=0, column=0, sticky="w")
        self.category_var = tk.StringVar()
        self.category_cb = ttk.Combobox(input_frame, textvariable=self.category_var, state="readonly",
                                        values=["Service", "Product", "Delivery"])
        self.category_cb.grid(row=0, column=1, sticky="ew")
        self.category_cb.current(0)

        # Name entry
        ttk.Label(input_frame, text="Name:").grid(row=1, column=0, sticky="w")
        self.name_entry = ttk.Entry(input_frame)
        self.name_entry.grid(row=1, column=1, sticky="ew")

        # Message entry
        ttk.Label(input_frame, text="Message:").grid(row=2, column=0, sticky="nw")
        self.message_entry = tk.Text(input_frame, width=40, height=5)
        self.message_entry.grid(row=2, column=1, sticky="ew")

        # Submit button
        self.submit_btn = ttk.Button(input_frame, text="Submit Feedback", command=self.submit_feedback)
        self.submit_btn.grid(row=3, column=0, columnspan=2, pady=5)

        input_frame.columnconfigure(1, weight=1)

        # --- Filter Frame ---
        filter_frame = ttk.Frame(root, padding=10)
        filter_frame.grid(row=1, column=0, sticky="ew")

        ttk.Label(filter_frame, text="Filter by category:").grid(row=0, column=0, sticky="w")
        self.filter_var = tk.StringVar()
        self.filter_cb = ttk.Combobox(filter_frame, textvariable=self.filter_var, state="readonly",
                                      values=["All", "Service", "Product", "Delivery"])
        self.filter_cb.grid(row=0, column=1, sticky="w")
        self.filter_cb.current(0)
        self.filter_cb.bind("<<ComboboxSelected>>", self.update_listbox)

        # --- Listbox Frame ---
        listbox_frame = ttk.Frame(root, padding=10)
        listbox_frame.grid(row=2, column=0, sticky="nsew")

        self.feedback_listbox = tk.Listbox(listbox_frame, height=15)
        self.feedback_listbox.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(listbox_frame, orient="vertical", command=self.feedback_listbox.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.feedback_listbox.config(yscrollcommand=self.scrollbar.set)

        listbox_frame.rowconfigure(0, weight=1)
        listbox_frame.columnconfigure(0, weight=1)

        root.rowconfigure(2, weight=1)
        root.columnconfigure(0, weight=1)

    def submit_feedback(self):
        category = self.category_var.get()
        name = self.name_entry.get().strip()
        message = self.message_entry.get("1.0", "end").strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        if not message:
            messagebox.showwarning("Input Error", "Please enter your message.")
            return

        # Save feedback
        self.feedbacks.append((category, name, message))

        # Clear inputs
        self.name_entry.delete(0, "end")
        self.message_entry.delete("1.0", "end")

        # Update listbox display according to current filter
        self.update_listbox()

    def update_listbox(self, event=None):
        filter_cat = self.filter_var.get()
        self.feedback_listbox.delete(0, "end")

        for cat, name, msg in self.feedbacks:
            if filter_cat == "All" or cat == filter_cat:
                display_text = f"[{cat}] {name}: {msg}"
                self.feedback_listbox.insert("end", display_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = FeedbackApp(root)
    root.mainloop()
