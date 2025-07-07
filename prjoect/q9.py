import tkinter as tk
from tkinter import ttk, messagebox

class BMICalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧮 BMI Calculator")
        self.geometry("350x250")
        self.resizable(False, False)

        # ---------- Height ----------
        ttk.Label(self, text="Height (cm):", font=("Arial", 10)).pack(pady=(20, 5))
        self.height_var = tk.IntVar(value=170)
        tk.Spinbox(self, from_=100, to=250, textvariable=self.height_var, width=10).pack()

        # ---------- Weight ----------
        ttk.Label(self, text="Weight (kg):", font=("Arial", 10)).pack(pady=(10, 5))
        self.weight_var = tk.IntVar(value=70)
        tk.Spinbox(self, from_=30, to=200, textvariable=self.weight_var, width=10).pack()

        # ---------- Calculate Button ----------
        ttk.Button(self, text="Calculate BMI", command=self.calculate_bmi).pack(pady=15)

        # ---------- Result Label ----------
        self.result_label = ttk.Label(self, text="", font=("Arial", 11, "bold"))
        self.result_label.pack(pady=5)

    def calculate_bmi(self):
        try:
            height_cm = self.height_var.get()
            weight_kg = self.weight_var.get()

            if height_cm <= 0 or weight_kg <= 0:
                raise ValueError

            height_m = height_cm / 100
            bmi = weight_kg / (height_m ** 2)
            category = self.get_bmi_category(bmi)

            self.result_label.config(
                text=f"BMI: {bmi:.2f} ({category})",
                foreground=self.get_color(category)
            )

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid height and weight.")

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"

    def get_color(self, category):
        return {
            "Underweight": "blue",
            "Normal": "green",
            "Overweight": "orange",
            "Obese": "red"
        }.get(category, "black")

if __name__ == "__main__":
    BMICalculator().mainloop()
