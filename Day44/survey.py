import tkinter as tk

def check_all_answered(*args):
    if q1_var.get() != 0 and q2_var.get() != 0:
        next_button.config(state="normal")
    else:
        next_button.config(state="disabled")

# Window setup
root = tk.Tk()
root.title("Survey Form")
root.geometry("350x300")

# Question 1
tk.Label(root, text="1. How satisfied are you with our service?").pack(anchor="w", padx=10, pady=(10, 0))
q1_var = tk.IntVar(value=0)  # 0 = not answered

for val, text in enumerate(["Very Satisfied", "Satisfied", "Neutral", "Unsatisfied"], start=1):
    tk.Radiobutton(root, text=text, variable=q1_var, value=val, command=check_all_answered).pack(anchor="w", padx=20)

# Question 2
tk.Label(root, text="2. Would you recommend us to others?").pack(anchor="w", padx=10, pady=(20, 0))
q2_var = tk.IntVar(value=0)  # 0 = not answered

for val, text in enumerate(["Yes", "Maybe", "No"], start=1):
    tk.Radiobutton(root, text=text, variable=q2_var, value=val, command=check_all_answered).pack(anchor="w", padx=20)

# Next button (initially disabled)
next_button = tk.Button(root, text="Next", state="disabled", command=lambda: print("Proceeding..."))
next_button.pack(pady=30)

root.mainloop()
