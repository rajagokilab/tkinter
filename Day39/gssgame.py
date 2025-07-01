import tkinter as tk
import random

def check_guess():
    try:
        guess = int(guess_entry.get())
    except ValueError:
        hint_label.config(text="Please enter a valid integer.")
        return
    
    if guess < number:
        hint_label.config(text="Too low! Try again.")
    elif guess > number:
        hint_label.config(text="Too high! Try again.")
    else:
        hint_label.config(text=f"Correct! The number was {number}.")
        submit_btn.config(state=tk.DISABLED)

def reset_game():
    global number
    number = random.randint(1, 100)
    hint_label.config(text="Guess a number between 1 and 100")
    guess_entry.delete(0, tk.END)
    submit_btn.config(state=tk.NORMAL)

root = tk.Tk()
root.title("Guess the Number Game")
root.geometry("350x200")

number = random.randint(1, 100)

tk.Label(root, text="Enter your guess:").pack(pady=(20, 5))
guess_entry = tk.Entry(root, width=20)
guess_entry.pack()

submit_btn = tk.Button(root, text="Submit", command=check_guess)
submit_btn.pack(pady=10)

hint_label = tk.Label(root, text="Guess a number between 1 and 100")
hint_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset", command=reset_game)
reset_btn.pack()

root.mainloop()
