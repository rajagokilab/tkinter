import tkinter as tk
from tkinter import ttk, messagebox

def convert_temp():
    try:
        temp = float(temp_spinbox.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return

    direction = direction_combo.get()
    if direction == "Celsius to Fahrenheit":
        result = (temp * 9/5) + 32
        result_label.config(text=f"{temp} °C = {result:.2f} °F")
    elif direction == "Fahrenheit to Celsius":
        result = (temp - 32) * 5/9
        result_label.config(text=f"{temp} °F = {result:.2f} °C")
    else:
        messagebox.showwarning("Select conversion", "Please select a conversion direction.")

# Main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x180")
root.configure(padx=20, pady=20)

# Temperature Input
tk.Label(root, text="Enter Temperature:").pack(anchor="w")
temp_spinbox = tk.Spinbox(root, from_=-100, to=200, width=10)
temp_spinbox.pack(pady=5)

# Conversion Direction
tk.Label(root, text="Conversion Direction:").pack(anchor="w")
direction_combo = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], state="readonly")
direction_combo.pack()
direction_combo.set("Celsius to Fahrenheit")

# Convert Button
convert_btn = tk.Button(root, text="Convert", command=convert_temp)
convert_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ", font=("Arial", 12))
result_label.pack()

root.mainloop()
