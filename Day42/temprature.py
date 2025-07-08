import tkinter as tk
from tkinter import ttk

def convert_temperature(*args):
    try:
        temp = float(temp_var.get())
        unit = unit_var.get()
        if unit == "Celsius":
            converted = (temp * 9/5) + 32
            result = f"{converted:.2f} °F"
        else:
            converted = (temp - 32) * 5/9
            result = f"{converted:.2f} °C"
        result_label.config(text=f"Converted: {result}")
    except ValueError:
        result_label.config(text="Invalid input")

# ── Main Window ───────────────────────────────────────
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.resizable(False, False)

# ── Variables ─────────────────────────────────────────
temp_var = tk.StringVar(value="0")
unit_var = tk.StringVar(value="Celsius")

# ── Input Controls ────────────────────────────────────
tk.Label(root, text="Enter Temperature:").pack(pady=(10, 2))
temp_spin = tk.Spinbox(root, from_=-100, to=300, textvariable=temp_var, width=10)
temp_spin.pack()

tk.Label(root, text="Select Unit:").pack(pady=(10, 2))
unit_combo = ttk.Combobox(root, values=["Celsius", "Fahrenheit"], textvariable=unit_var, state="readonly", width=10)
unit_combo.pack()

# ── Convert Button ────────────────────────────────────
convert_btn = tk.Button(root, text="Convert", command=convert_temperature)
convert_btn.pack(pady=10)

# ── Result Label ──────────────────────────────────────
result_label = tk.Label(root, text="Converted: ")
result_label.pack(pady=5)

# ── Dynamic Update Bindings ───────────────────────────
temp_var.trace_add("write", convert_temperature)
unit_var.trace_add("write", convert_temperature)

root.mainloop()
