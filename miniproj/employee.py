import tkinter as tk
from tkinter import ttk, messagebox

class ShiftScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Shift Scheduler")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.grid(row=0, column=0)

        # Employee Name
        tk.Label(frame, text="Employee Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.entry_name = tk.Entry(frame, width=30)
        self.entry_name.grid(row=0, column=1, pady=5)

        # Shift Type Combobox
        tk.Label(frame, text="Shift Type:").grid(row=1, column=0, sticky="e", pady=5)
        self.shift_types = ["Morning", "Afternoon", "Night"]
        self.combo_shift = ttk.Combobox(frame, values=self.shift_types, state="readonly", width=28)
        self.combo_shift.grid(row=1, column=1, pady=5)
        self.combo_shift.current(0)

        # Working Hours Spinbox
        tk.Label(frame, text="Working Hours:").grid(row=2, column=0, sticky="e", pady=5)
        self.spin_hours = tk.Spinbox(frame, from_=1, to=24, width=5)
        self.spin_hours.grid(row=2, column=1, sticky="w", pady=5)

        # Add Button
        self.btn_add = tk.Button(frame, text="Add Shift", command=self.add_shift)
        self.btn_add.grid(row=3, column=0, columnspan=2, pady=10)

        # Listbox with Scrollbar
        list_frame = tk.Frame(frame)
        list_frame.grid(row=4, column=0, columnspan=2, pady=5)

        self.scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(list_frame, width=50, height=10, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    def add_shift(self):
        name = self.entry_name.get().strip()
        shift = self.combo_shift.get()
        hours = self.spin_hours.get()

        if not name:
            messagebox.showwarning("Input Error", "Please enter employee name.")
            return

        entry = f"{name} | Shift: {shift} | Hours: {hours}"
        self.listbox.insert(tk.END, entry)
        self.entry_name.delete(0, tk.END)
        self.combo_s_
