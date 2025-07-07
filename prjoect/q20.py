import tkinter as tk
from tkinter import ttk, messagebox

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🧮 Simple Calculator")
        self.geometry("350x220")
        self.resizable(False, False)

        # First number
        ttk.Label(self, text="Number 1:").pack(anchor="w", padx=20, pady=(20, 0))
        self.num1_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.num1_var).pack(fill="x", padx=20)

        # Second number
        ttk.Label(self, text="Number 2:").pack(anchor="w", padx=20, pady=(10, 0))
        self.num2_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.num2_var).pack(fill="x", padx=20)

        # Operator combobox
        ttk.Label(self, text="Operator:").pack(anchor="w", padx=20, pady=(10, 0))
        self.operator_var = tk.StringVar()
        operators = ["+", "-", "*", "/"]
        self.op_combo = ttk.Combobox(self, textvariable=self.operator_var, values=operators, state="readonly")
        self.op_combo.current(0)
        self.op_combo.pack(fill="x", padx=20)

        # Calculate button
        ttk.Button(self, text="Calculate", command=self.calculate).pack(pady=15)

        # Result Label
        self.result_label = ttk.Label(self, text="Result: ", font=("Arial", 14))
        self.result_label.pack(padx=20)

    def calculate(self):
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            op = self.operator_var.get()

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator")

            self.result_label.config(text=f"Result: {result:.4g}")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
        except ZeroDivisionError as e:
            messagebox.showerror("Math Error", str(e))

if __name__ == "__main__":
    CalculatorApp().mainloop()
