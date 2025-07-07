import tkinter as tk
from tkinter import ttk, messagebox

class AttendanceMarker(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎓 Student Attendance Marker")
        self.geometry("350x400")
        self.resizable(False, False)

        # Sample students list
        self.students = [
            "Alice Johnson", "Bob Smith", "Charlie Brown", "Diana Prince",
            "Ethan Hunt", "Fiona Glenanne", "George Costanza", "Hannah Baker",
            "Ian Fleming", "Jessica Jones", "Kevin Hart", "Laura Palmer"
        ]

        # -------- Listbox with scrollbar --------
        frame = ttk.Frame(self)
        frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.listbox = tk.Listbox(frame, selectmode=tk.SINGLE, height=15, font=("Arial", 12))
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Populate listbox
        for student in self.students:
            self.listbox.insert(tk.END, student)

        # -------- Buttons --------
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Mark Present ✓", command=self.mark_present).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Mark Absent ✗", command=self.mark_absent).grid(row=0, column=1, padx=10)

    def mark_present(self):
        self.update_attendance("present")

    def mark_absent(self):
        self.update_attendance("absent")

    def update_attendance(self, status):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Select Student", "Please select a student from the list.")
            return

        index = selected[0]
        current_text = self.listbox.get(index)

        # Remove any existing prefix (✓ or ✗)
        clean_name = current_text.lstrip("✓✗ ").strip()

        if status == "present":
            new_text = f"✓ {clean_name}"
        else:
            new_text = f"✗ {clean_name}"

        self.listbox.delete(index)
        self.listbox.insert(index, new_text)
        self.listbox.selection_set(index)  # keep selection

if __name__ == "__main__":
    AttendanceMarker().mainloop()
