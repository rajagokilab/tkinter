import tkinter as tk
from tkinter import ttk, messagebox

class ShiftSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Shift Scheduler")
        self.root.geometry("500x400")

        # Sample employees
        self.employees = ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George", "Hannah", "Ian", "Julia"]

        # Store assignments as list of tuples: (employee, shift_type, hours)
        self.assignments = []

        # --- Employee Listbox + Scrollbar ---
        emp_frame = ttk.LabelFrame(root, text="Employees")
        emp_frame.pack(side="left", fill="both", expand=False, padx=10, pady=10)

        self.emp_listbox = tk.Listbox(emp_frame, height=15, exportselection=False)
        self.emp_listbox.pack(side="left", fill="y")
        self.emp_scrollbar = ttk.Scrollbar(emp_frame, orient="vertical", command=self.emp_listbox.yview)
        self.emp_scrollbar.pack(side="left", fill="y")
        self.emp_listbox.config(yscrollcommand=self.emp_scrollbar.set)

        for emp in self.employees:
            self.emp_listbox.insert("end", emp)

        # --- Shift Assignment Controls ---
        control_frame = ttk.Frame(root)
        control_frame.pack(side="top", fill="x", padx=10, pady=10)

        ttk.Label(control_frame, text="Shift Type:").grid(row=0, column=0, sticky="w")
        self.shift_var = tk.StringVar()
        self.shift_cb = ttk.Combobox(control_frame, textvariable=self.shift_var, state="readonly",
                                     values=["Morning", "Evening", "Night"])
        self.shift_cb.grid(row=0, column=1, sticky="ew", padx=5)
        self.shift_cb.current(0)

        ttk.Label(control_frame, text="Hours Assigned:").grid(row=1, column=0, sticky="w", pady=5)
        self.hours_var = tk.IntVar(value=8)
        self.hours_spinbox = ttk.Spinbox(control_frame, from_=1, to=12, textvariable=self.hours_var, width=5)
        self.hours_spinbox.grid(row=1, column=1, sticky="w", padx=5, pady=5)

        self.assign_btn = ttk.Button(control_frame, text="Assign Shift", command=self.assign_shift)
        self.assign_btn.grid(row=2, column=0, columnspan=2, pady=10)

        control_frame.columnconfigure(1, weight=1)

        # --- Shift Assignments Listbox + Scrollbar ---
        assign_frame = ttk.LabelFrame(root, text="Shift Assignments")
        assign_frame.pack(side="bottom", fill="both", expand=True, padx=10, pady=10)

        self.assign_listbox = tk.Listbox(assign_frame)
        self.assign_listbox.pack(side="left", fill="both", expand=True)
        self.assign_scrollbar = ttk.Scrollbar(assign_frame, orient="vertical", command=self.assign_listbox.yview)
        self.assign_scrollbar.pack(side="left", fill="y")
        self.assign_listbox.config(yscrollcommand=self.assign_scrollbar.set)

    def assign_shift(self):
        selected_indices = self.emp_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("No selection", "Please select an employee.")
            return

        employee = self.emp_listbox.get(selected_indices[0])
        shift = self.shift_var.get()
        hours = self.hours_var.get()

        # Add assignment
        self.assignments.append((employee, shift, hours))
        self.update_assignment_list()

    def update_assignment_list(self):
        self.assign_listbox.delete(0, "end")
        for emp, shift, hrs in self.assignments:
            self.assign_listbox.insert("end", f"{emp} - {shift} Shift - {hrs} hrs")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShiftSchedulerApp(root)
    root.mainloop()
