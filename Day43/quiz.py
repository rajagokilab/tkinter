import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x300")

        self.create_menu()
        self.create_widgets()

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Berlin", "London", "Paris", "Rome"], "answer": 2},
            {"question": "2 + 2 = ?", "options": ["3", "4", "5", "6"], "answer": 1},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": 1},
        ]
        self.score = 0
        self.current_q = -1

    def create_menu(self):
        menubar = tk.Menu(self.root)
        quiz_menu = tk.Menu(menubar, tearoff=0)
        quiz_menu.add_command(label="Start New", command=self.start_quiz)
        quiz_menu.add_command(label="End", command=self.end_quiz)
        menubar.add_cascade(label="Quiz", menu=quiz_menu)
        self.root.config(menu=menubar)

    def create_widgets(self):
        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack(fill="both", expand=True)

        self.question_label = tk.Label(self.frame, text="", font=("Arial", 14), wraplength=350)
        self.question_label.pack(pady=10)

        self.selected_option = tk.IntVar(value=-1)

        self.options_frame = tk.Frame(self.frame)
        self.options_frame.pack()

        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.options_frame, text="", variable=self.selected_option, value=i)
            rb.pack(anchor="w")
            self.option_buttons.append(rb)

        self.submit_btn = tk.Button(self.frame, text="Submit Answer", command=self.submit_answer, state="disabled")
        self.submit_btn.pack(pady=20)

    def start_quiz(self):
        self.score = 0
        self.current_q = 0
        self.load_question()
        self.submit_btn.config(state="normal")

    def load_question(self):
        q = self.questions[self.current_q]
        self.question_label.config(text=q["question"])
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option)
        self.selected_option.set(-1)

    def submit_answer(self):
        if self.selected_option.get() == -1:
            messagebox.showwarning("No selection", "Please select an option.")
            return

        correct_answer = self.questions[self.current_q]["answer"]
        user_answer = self.selected_option.get()

        confirm = messagebox.askyesno("Confirm Answer", f"Are you sure your answer is '{self.option_buttons[user_answer].cget('text')}'?")
        if not confirm:
            return

        if user_answer == correct_answer:
            self.score += 1

        self.current_q += 1
        if self.current_q < len(self.questions):
            self.load_question()
        else:
            self.show_score_dialog()
            self.submit_btn.config(state="disabled")
            self.question_label.config(text="Quiz completed!")
            for rb in self.option_buttons:
                rb.config(text="", state="disabled")

    def show_score_dialog(self):
        dlg = tk.Toplevel(self.root)
        dlg.title("Quiz Result")
        dlg.geometry("300x150")
        dlg.transient(self.root)
        dlg.grab_set()

        tk.Label(dlg, text=f"Your final score is {self.score} out of {len(self.questions)}", font=("Arial", 14)).pack(pady=30)
        tk.Button(dlg, text="Close", command=dlg.destroy).pack(pady=10)

    def end_quiz(self):
        if messagebox.askyesno("End Quiz", "Are you sure you want to end the quiz?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
