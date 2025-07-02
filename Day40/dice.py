import tkinter as tk
import random

def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f"Rolled: {result}")

root = tk.Tk()
root.title("Dice Roller Simulator")
root.geometry("300x200")

# Roll button
roll_button = tk.Button(root, text="Roll Dice", command=roll_dice)
roll_button.place(relx=0.5, rely=0.4, anchor="center")

# Result label
result_label = tk.Label(root, text="Roll the dice!", font=("Arial", 16))
result_label.place(relx=0.5, rely=0.6, anchor="center")

root.mainloop()
