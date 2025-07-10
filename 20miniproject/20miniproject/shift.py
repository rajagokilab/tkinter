import tkinter as tk
from tkinter import ttk, messagebox

def add_shift():
    name = name_entry.get().strip()
    shift = shift_combo.get()
    hours = hours_spinbox.get()

    if not name:
        messagebox.showwarning("Input Error", "Please enter the employee's name.")
        return
    if shift == "":
        messagebox.showwarning("Input Error", "Please select a shift type.")
        return

    record = f"Employee: {name} | Shift: {shift} | Hours: {hours}"
    shift_listbox.insert(tk.END, record)

    # Clear inputs
    name_entry.delete(0, tk.END)
    shift_combo.set("")
    hours_spinbox.delete(0, tk.END)
    hours_spinbox.insert(0, "8")

# === Main Window ===
root = tk.Tk()
root.title("Employee Shift Scheduler")
root.geometry("600x400")
root.configure(padx=15, pady=15)

# Input Frame
input_frame = tk.Frame(root)
input_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Employee Name
tk.Label(input_frame, text="Employee Name:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(input_frame, width=40)
name_entry.grid(row=0, column=1, pady=5)

# Shift Type Combobox
tk.Label(input_frame, text="Shift Type:").grid(row=1, column=0, sticky="w", pady=5)
shift_combo = ttk.Combobox(input_frame, values=["Morning", "Afternoon", "Night"], state="readonly", width=37)
shift_combo.grid(row=1, column=1, pady=5)

# Hours Spinbox
tk.Label(input_frame, text="Working Hours:").grid(row=2, column=0, sticky="w", pady=5)
hours_spinbox = tk.Spinbox(input_frame, from_=1, to=12, width=5)
hours_spinbox.grid(row=2, column=1, sticky="w", pady=5)
hours_spinbox.delete(0, tk.END)
hours_spinbox.insert(0, "8")

# Add Shift Button
add_btn = tk.Button(input_frame, text="Add Shift", command=add_shift)
add_btn.grid(row=3, column=0, columnspan=2, pady=15)

# Listbox Frame
list_frame = tk.Frame(root)
list_frame.grid(row=1, column=0, sticky="nsew", padx=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

shift_listbox = tk.Listbox(list_frame, width=80, height=12, yscrollcommand=scrollbar.set)
shift_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=shift_listbox.yview)

# Configure grid weights for resizing
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
