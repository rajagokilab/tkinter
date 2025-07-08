import tkinter as tk
from tkinter import ttk

class LiveScoreboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Live Scoreboard")
        self.root.geometry("400x300")

        # Default teams
        self.team_names = ["Lions", "Tigers", "Bears", "Wolves", "Eagles"]

        # Variables
        self.team_a_name = tk.StringVar(value=self.team_names[0])
        self.team_b_name = tk.StringVar(value=self.team_names[1])
        self.score_a = tk.IntVar(value=0)
        self.score_b = tk.IntVar(value=0)

        # Top frame for team selection and score input
        top_frame = ttk.Frame(root)
        top_frame.pack(pady=10, fill="x")

        # Team A
        ttk.Label(top_frame, text="Team A:").grid(row=0, column=0, sticky="e")
        self.team_a_cb = ttk.Combobox(top_frame, values=self.team_names, textvariable=self.team_a_name, state="readonly", width=10)
        self.team_a_cb.grid(row=0, column=1, padx=5)
        self.team_a_cb.bind("<<ComboboxSelected>>", self.update_canvas)

        ttk.Label(top_frame, text="Score:").grid(row=1, column=0, sticky="e")
        self.score_a_spin = ttk.Spinbox(top_frame, from_=0, to=100, textvariable=self.score_a, width=5, command=self.update_canvas)
        self.score_a_spin.grid(row=1, column=1, padx=5)
        self.score_a.trace_add("write", lambda *args: self.update_canvas())

        # Team B
        ttk.Label(top_frame, text="Team B:").grid(row=0, column=2, sticky="e")
        self.team_b_cb = ttk.Combobox(top_frame, values=self.team_names, textvariable=self.team_b_name, state="readonly", width=10)
        self.team_b_cb.grid(row=0, column=3, padx=5)
        self.team_b_cb.bind("<<ComboboxSelected>>", self.update_canvas)

        ttk.Label(top_frame, text="Score:").grid(row=1, column=2, sticky="e")
        self.score_b_spin = ttk.Spinbox(top_frame, from_=0, to=100, textvariable=self.score_b, width=5, command=self.update_canvas)
        self.score_b_spin.grid(row=1, column=3, padx=5)
        self.score_b.trace_add("write", lambda *args: self.update_canvas())

        # Reset button
        self.reset_btn = ttk.Button(root, text="Reset Scores", command=self.reset_scores)
        self.reset_btn.pack(pady=10)

        # Canvas for scoreboard
        self.canvas_width = 350
        self.canvas_height = 120
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack(pady=10)

        self.update_canvas()

    def update_canvas(self, event=None):
        self.canvas.delete("all")

        # Draw background rectangles for teams
        self.canvas.create_rectangle(10, 10, self.canvas_width//2 - 5, self.canvas_height - 10, fill="#003366")
        self.canvas.create_rectangle(self.canvas_width//2 + 5, 10, self.canvas_width - 10, self.canvas_height - 10, fill="#660000")

        # Team A Name & Score
        self.canvas.create_text((self.canvas_width//4), 40, text=self.team_a_name.get(),
                                font=("Arial", 20, "bold"), fill="white")
        self.canvas.create_text((self.canvas_width//4), 80, text=str(self.score_a.get()),
                                font=("Arial", 40, "bold"), fill="white")

        # Team B Name & Score
        self.canvas.create_text((self.canvas_width*3//4), 40, text=self.team_b_name.get(),
                                font=("Arial", 20, "bold"), fill="white")
        self.canvas.create_text((self.canvas_width*3//4), 80, text=str(self.score_b.get()),
                                font=("Arial", 40, "bold"), fill="white")

    def reset_scores(self):
        self.score_a.set(0)
        self.score_b.set(0)
        self.update_canvas()

if __name__ == "__main__":
    root = tk.Tk()
    LiveScoreboardApp(root)
    root.mainloop()
