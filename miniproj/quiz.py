import tkinter as tk

questions = [
    {"question": "What is the capital of France?",
     "options": ["Berlin", "London", "Paris", "Madrid"],
     "answer": 2},
    {"question": "Which planet is known as the Red Planet?",
     "options": ["Earth", "Mars", "Jupiter", "Saturn"],
     "answer": 1},
    {"question": "Who wrote 'Hamlet'?",
     "options": ["Leo Tolstoy", "Mark Twain", "William Shakespeare", "Charles Dickens"],
     "answer": 2},
    {"question": "What is the chemical symbol for water?",
     "options": ["O2", "H2O", "CO2", "NaCl"],
     "answer": 1},
    {"question": "What is 9 * 9?",
     "options": ["81", "72", "99", "79"],
     "answer": 0}
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.current_q = 0
        self.score = 0
        self.selected_answer = tk.IntVar(value=-1)

        # Question label
        self.q_label = tk.Label(root, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.q_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Radiobuttons for options
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.selected_answer, value=i, font=("Arial", 12))
            rb.grid(row=i+1, column=0, sticky="w", padx=20)
            self.option_buttons.append(rb)

        # Next button
        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.grid(row=5, column=0, pady=10)

        # Score label (initially hidden)
        self.score_label = tk.Label(root, text="", font=("Arial", 14))
        self.score_label.grid(row=6, column=0, columnspan=2, pady=10)

        self.load_question()

    def load_question(self):
        q = questions[self.current_q]
        self.q_label.config(text=f"Q{self.current_q + 1}: {q['question']}")
        for i, option in enumerate(q['options']):
            self.option_buttons[i].config(text=option, state="normal")
        self.selected_answer.set(-1)
        self.score_label.config(text="")
        self.next_button.config(state="normal")

    def next_question(self):
        selected = self.selected_answer.get()
        if selected == -1:
            return  # Ignore if no option selected

        # Disable radiobuttons to prevent changing answer
        for rb in self.option_buttons:
            rb.config(state="disabled")

        correct = questions[self.current_q]["answer"]
        if selected == correct:
            self.score += 1

        self.next_button.config(state="disabled")

        self.current_q += 1
        if self.current_q < len(questions):
            # Delay loading next question to let user see disabled state (optional)
            self.root.after(1000, self.load_question)
        else:
            self.show_score()

    def show_score(self):
        self.q_label.config(text="Quiz Completed!")
        for rb in self.option_buttons:
            rb.grid_remove()
        self.next_button.grid_remove()
        self.score_label.config(text=f"Your score: {self.score} / {len(questions)}")

root = tk.Tk()
app = QuizApp(root)
root.mainloop()
