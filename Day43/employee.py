import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class ShiftScheduler:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Shift Scheduler")
        self.root.geometry("600x400")

        self.create_menu()
        self.create_toolbar()
        self.create_frames()

        self.employees = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
        self.shifts = ["Morning", "Afternoon", "Night"]
        self.assignments = {}  # employee -> shift

        self.load_employees()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Export Schedule", command=self.export_schedule)
        menubar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        assign_btn = tk.Button(toolbar, text="Assign", command=self.assign_shift)
        assign_btn.pack(side="left", padx=5, pady=5)

        clear_btn = tk.Button(toolbar, text="Clear", command=self.clear_assignment)
        clear_btn.pack(side="left", padx=5, pady=5)

    def create_frames(self):
        container = tk.Frame(self.root)
        container.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame 1: Employee list (left)
        self.frame_employees = tk.Frame(container, bd=2, relief=tk.SUNKEN)
        self.frame_employees.pack(side="left", fill="both", expand=True, padx=(0, 5))

        tk.Label(self.frame_employees, text="Employees").pack(pady=5)
        self.employee_listbox = tk.Listbox(self.frame_employees, exportselection=False)
        self.employee_listbox.pack(fill="both", expand=True, padx=5, pady=5)

        # Frame 2: Shift assignment (right)
        self.frame_shift = tk.Frame(container, bd=2, relief=tk.SUNKEN)
        self.frame_shift.pack(side="left", fill="both", expand=True, padx=(5,0))

        tk.Label(self.frame_shift, text="Assign Shift").pack(pady=5)
        self.shift_var = tk.StringVar()
        self.shift_combo = ttk.Combobox(self.frame_shift, textvariable=self.shift_var, values=self.shifts, state="readonly")
        self.shift_combo.pack(pady=10, padx=10)

        self.assigned_label = tk.Label(self.frame_shift, text="No shift assigned yet.", fg="blue")
        self.assigned_label.pack(pady=10)

    def load_employees(self):
        self.employee_listbox.delete(0, tk.END)
        for emp in self.employees:
            self.employee_listbox.insert(tk.END, emp)
        self.employee_listbox.bind("<<ListboxSelect>>", self.show_assignment)

    def show_assignment(self, event=None):
        sel = self.employee_listbox.curselection()
        if not sel:
            self.assigned_label.config(text="No shift assigned yet.")
            return
        emp = self.employee_listbox.get(sel[0])
        shift = self.assignments.get(emp, "None")
        self.assigned_label.config(text=f"{emp} is assigned to: {shift}")

    def assign_shift(self):
        sel = self.employee_listbox.curselection()
        shift = self.shift_var.get()
        if not sel:
            messagebox.showwarning("Assign Shift", "Select an employee first.")
            return
        if not shift:
            messagebox.showwarning("Assign Shift", "Select a shift first.")
            return
        emp = self.employee_listbox.get(sel[0])
        self.assignments[emp] = shift
        self.show_assignment()
        messagebox.showinfo("Assign Shift", f"Assigned {emp} to {shift} shift.")

    def clear_assignment(self):
        sel = self.employee_listbox.curselection()
        if not sel:
            messagebox.showwarning("Clear Assignment", "Select an employee first.")
            return
        emp = self.employee_listbox.get(sel[0])
        if emp in self.assignments:
            del self.assignments[emp]
        self.show_assignment()
        messagebox.showinfo("Clear Assignment", f"Cleared shift assignment for {emp}.")

    def export_schedule(self):
        if not self.assignments:
            messagebox.showinfo("Export Schedule", "No assignments to export.")
            return
        if not messagebox.askyesno("Export Schedule", "Export current schedule to file?"):
            return
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                                                     title="Save Schedule")
            if file_path:
                with open(file_path, "w") as f:
                    for emp in self.employees:
                        shift = self.assignments.get(emp, "None")
                        f.write(f"{emp}: {shift}\n")
                messagebox.showinfo("Export Schedule", f"Schedule saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Export Error", f"Failed to save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShiftScheduler(root)
    root.mainloop()
