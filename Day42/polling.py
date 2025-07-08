import tkinter as tk
from tkinter import ttk, messagebox

class PollApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Polling App")

        # Sample polls: question -> list of options
        self.polls = {
            "Favorite Fruit?": ["Apple", "Banana", "Orange", "Grapes", "Mango", "Peach", "Pineapple", "Strawberry", "Watermelon", "Kiwi", "Cherry"],
            "Best Programming Language?": ["Python", "JavaScript", "C++", "Java", "Ruby", "Go", "Rust", "Swift"],
            "Preferred Pet?": ["Dog", "Cat", "Fish", "Bird", "Rabbit"]
        }

        # Vote counts stored: question -> [counts per option]
        self.votes = {q: [0]*len(opts) for q, opts in self.polls.items()}

        # Combobox for poll questions
        ttk.Label(root, text="Select Poll Question:").pack(padx=10, pady=5, anchor="w")
        self.question_var = tk.StringVar()
        self.question_cb = ttk.Combobox(root, textvariable=self.question_var, state="readonly",
                                        values=list(self.polls.keys()))
        self.question_cb.pack(fill="x", padx=10)
        self.question_cb.bind("<<ComboboxSelected>>", self.load_options)
        self.question_cb.current(0)

        # Frame for Listbox + Scrollbar
        list_frame = ttk.Frame(root)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.options_lb = tk.Listbox(list_frame, height=10, exportselection=False)
        self.options_lb.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.options_lb.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.options_lb.config(yscrollcommand=self.scrollbar.set)

        # Submit vote button
        self.submit_btn = ttk.Button(root, text="Submit Vote", command=self.submit_vote)
        self.submit_btn.pack(pady=5)

        # Load initial options
        self.load_options()

    def load_options(self, event=None):
        question = self.question_var.get()
        options = self.polls.get(question, [])
        self.options_lb.delete(0, "end")

        # Show options with vote counts
        for i, opt in enumerate(options):
            count = self.votes[question][i]
            self.options_lb.insert("end", f"{opt} — Votes: {count}")

        # Select first by default
        if options:
            self.options_lb.selection_set(0)

    def submit_vote(self):
        question = self.question_var.get()
        selected = self.options_lb.curselection()
        if not selected:
            messagebox.showwarning("No selection", "Please select an option to vote.")
            return

        index = selected[0]
        self.votes[question][index] += 1
        self.load_options()  # Refresh display

        messagebox.showinfo("Thank you!", f"Your vote for '{self.polls[question][index]}' has been counted.")

if __name__ == "__main__":
    root = tk.Tk()
    PollApp(root)
    root.mainloop()
