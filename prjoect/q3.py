import re
import tkinter as tk
from tkinter import messagebox, ttk

EMAIL_PATTERN = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$")  # simple RFC‑ish check

class FeedbackApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Feedback Collector")
        self.geometry("550x400")
        self.resizable(False, False)

        # ---------- Input frame ----------
        input_frm = ttk.LabelFrame(self, text="Leave your feedback", padding=10)
        input_frm.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        ttk.Label(input_frm, text="Name").grid(row=0, column=0, sticky="w")
        ttk.Label(input_frm, text="E‑mail").grid(row=1, column=0, sticky="w")
        ttk.Label(input_frm, text="Comments").grid(row=2, column=0, sticky="nw")

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()

        ttk.Entry(input_frm, textvariable=self.name_var, width=40).grid(row=0, column=1, padx=5, pady=2)
        ttk.Entry(input_frm, textvariable=self.email_var, width=40).grid(row=1, column=1, padx=5, pady=2)
        self.comment_txt = tk.Text(input_frm, width=42, height=5)
        self.comment_txt.grid(row=2, column=1, padx=5, pady=2)

        # ---------- Buttons ----------
        btn_frm = ttk.Frame(input_frm)
        btn_frm.grid(row=3, column=1, pady=5, sticky="e")

        ttk.Button(btn_frm, text="Add Feedback ➜", command=self.add_feedback).grid(row=0, column=0, padx=(0,10))
        ttk.Button(btn_frm, text="Clear Selected ✖", command=self.clear_selected).grid(row=0, column=1)

        # ---------- Listbox + Scrollbar ----------
        list_frm = ttk.LabelFrame(self, text="Submitted feedback", padding=10)
        list_frm.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")
        self.rowconfigure(1, weight=1)               # listbox expands vertically
        list_frm.rowconfigure(0, weight=1)
        list_frm.columnconfigure(0, weight=1)

        self.lb = tk.Listbox(list_frm, height=10)
        sc = ttk.Scrollbar(list_frm, orient="vertical", command=self.lb.yview)
        self.lb.config(yscrollcommand=sc.set)

        self.lb.grid(row=0, column=0, sticky="nsew")
        sc.grid(row=0, column=1, sticky="ns")

    # ---------- callbacks ----------
    def add_feedback(self):
        name = self.name_var.get().strip()
        email = self.email_var.get().strip()
        comment = self.comment_txt.get("1.0", tk.END).strip()

        # Validation
        if not name or not email or not comment:
            messagebox.showwarning("Incomplete", "Please fill out all fields.")
            return
        if not EMAIL_PATTERN.match(email):
            messagebox.showerror("Invalid e‑mail", "Please enter a valid e‑mail address.")
            return

        # Compose one‑line preview (first 60 chars of comment)
        comment_preview = comment.replace("\n", " ")[:60] + ("…" if len(comment) > 60 else "")
        self.lb.insert(tk.END, f"{name} ({email}): {comment_preview}")

        # Clear inputs
        self.name_var.set("")
        self.email_var.set("")
        self.comment_txt.delete("1.0", tk.END)

    def clear_selected(self):
        sel = self.lb.curselection()
        if not sel:
            messagebox.showinfo("Nothing selected", "Select a feedback entry to clear.")
            return
        self.lb.delete(sel[0])

if __name__ == "__main__":
    FeedbackApp().mainloop()
