import tkinter as tk
from tkinter import messagebox

# === Quiz Data ===
questions = [
    {
        "question": "1. What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "2. What is 5 + 7?",
        "options": ["10", "12", "14", "15"],
        "answer": "12"
    },
    {
        "question": "3. Who wrote 'Hamlet'?",
        "options": ["Shakespeare", "Milton", "Chaucer", "Wordsworth"],
        "answer": "Shakespeare"
    },
    {
        "question": "4. What color do you get by mixing red and blue?",
        "options": ["Green", "Purple", "Orange", "Yellow"],
        "answer": "Purple"
    },
    {
        "question": "5. What is the boiling point of water?",
        "options": ["50°C", "100°C", "150°C", "200°C"],
        "answer": "100°C"
    }
]

current_q = 0
score = 0

def load_question():
    question_label.config(text=questions[current_q]["question"])
    selected.set(None)
    for i, option in enumerate(questions[current_q]["options"]):
        option_buttons[i].config(text=option, state=tk.NORMAL)
    next_button.config(state=tk.DISABLED)

def option_selected():
    # Enable next button and disable options
    for btn in option_buttons:
        btn.config(state=tk.DISABLED)
    next_button.config(state=tk.NORMAL)

def next_question():
    global current_q, score
    chosen = selected.get()
    correct = questions[current_q]["answer"]
    if chosen == correct:
        score += 1

    current_q += 1
    if current_q < len(questions):
        load_question()
    else:
        messagebox.showinfo("Quiz Complete", f"Your Score: {score} / {len(questions)}")
        root.quit()

# === UI Setup ===
root = tk.Tk()
root.title("Quiz Application")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Arial", 12), wraplength=350, justify="left")
question_label.grid(row=0, column=0, columnspan=2, pady=20)

selected = tk.StringVar()

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=selected, value="", command=option_selected, font=("Arial", 10))
    btn.grid(row=i+1, column=0, columnspan=2, sticky="w", padx=20)
    option_buttons.append(btn)

next_button = tk.Button(root, text="Next", command=next_question, state=tk.DISABLED)
next_button.grid(row=6, column=0, columnspan=2, pady=20)

# Load the first question
load_question()

root.mainloop()
