import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    try:
        value = float(input_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return
    
    conv_type = conversion_var.get()
    
    if conv_type == "cm to inches":
        result = value / 2.54
        output_var.set(f"{result:.2f} inches")
    elif conv_type == "inches to cm":
        result = value * 2.54
        output_var.set(f"{result:.2f} cm")
    elif conv_type == "Celsius to Fahrenheit":
        result = (value * 9/5) + 32
        output_var.set(f"{result:.2f} °F")
    elif conv_type == "Fahrenheit to Celsius":
        result = (value - 32) * 5/9
        output_var.set(f"{result:.2f} °C")
    else:
        output_var.set("")

root = tk.Tk()
root.title("Unit Converter")
root.geometry("350x180")

tk.Label(root, text="Enter value:").pack(pady=(10,0))
input_entry = tk.Entry(root, width=30)
input_entry.pack()

conversion_var = tk.StringVar(value="cm to inches")
options = ["cm to inches", "inches to cm", "Celsius to Fahrenheit", "Fahrenheit to Celsius"]
ttk.Combobox(root, textvariable=conversion_var, values=options, state="readonly").pack(pady=10)

convert_btn = tk.Button(root, text="Convert", command=convert)
convert_btn.pack()

output_var = tk.StringVar()
output_label = tk.Label(root, textvariable=output_var, font=("Arial", 14), fg="blue")
output_label.pack(pady=10)

root.mainloop()
