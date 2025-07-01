import tkinter as tk

def button_click(value):
    current = display_var.get()
    display_var.set(current + value)

def clear():
    display_var.set("")

def calculate():
    expression = display_var.get()
    try:
        # Replace × and ÷ with * and / for eval
        expression = expression.replace('×', '*').replace('÷', '/')
        result = eval(expression)
        display_var.set(str(result))
    except Exception:
        display_var.set("Error")

root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")

display_var = tk.StringVar()
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 24), bg="white", anchor='e', relief="sunken", height=2)
display_label.pack(fill='x', padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    '7', '8', '9', '÷',
    '4', '5', '6', '×',
    '1', '2', '3', '-',
    '0', '.', 'C', '+'
]

# Create buttons
for i, btn_text in enumerate(buttons):
    action = lambda x=btn_text: button_click(x) if x not in ['C'] else clear()
    tk.Button(btn_frame, text=btn_text, width=5, height=2, font=("Arial", 18), command=action).grid(row=i//4, column=i%4, padx=5, pady=5)

# Equals button spans across bottom
equal_btn = tk.Button(root, text='=', width=22, height=2, font=("Arial", 18), command=calculate)
equal_btn.pack(padx=10, pady=10)

root.mainloop()
