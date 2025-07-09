import tkinter as tk
from tkinter import ttk

def convert_temp():
    try:
        temp = float(temp_spinbox.get())
    except ValueError:
        result_label.config(text="Please enter a valid number")
        return

    direction = direction_combobox.get()
    if direction == "Celsius to Fahrenheit":
        converted = (temp * 9/5) + 32
        result_label.config(text=f"{temp}°C = {converted:.2f}°F")
    elif direction == "Fahrenheit to Celsius":
        converted = (temp - 32) * 5/9
        result_label.config(text=f"{temp}°F = {converted:.2f}°C")
    else:
        result_label.config(text="Select conversion direction")

root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Temperature:").grid(row=0, column=0, padx=10, pady=10)
temp_spinbox = tk.Spinbox(root, from_=-100, to=100, width=10)
temp_spinbox.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Convert:").grid(row=1, column=0, padx=10, pady=10)
direction_combobox = ttk.Combobox(root, values=["Celsius to Fahrenheit", "Fahrenheit to Celsius"], state="readonly", width=18)
direction_combobox.grid(row=1, column=1, padx=10, pady=10)
direction_combobox.current(0)

convert_button = tk.Button(root, text="Convert", command=convert_temp)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
