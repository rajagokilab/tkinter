import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())
        if height_cm <= 0 or weight_kg <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter positive numbers for height and weight.")
        return
    
    height_m = height_cm / 100  # convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    bmi_label.config(text=f"BMI: {bmi:.2f}")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

tk.Label(root, text="Height (cm):").pack(anchor='w', padx=10, pady=(10,0))
height_entry = tk.Entry(root, width=30)
height_entry.pack(padx=10)

tk.Label(root, text="Weight (kg):").pack(anchor='w', padx=10, pady=(10,0))
weight_entry = tk.Entry(root, width=30)
weight_entry.pack(padx=10)

calc_btn = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_btn.pack(pady=15)

bmi_label = tk.Label(root, text="BMI: ", font=("Arial", 14))
bmi_label.pack()

root.mainloop()
