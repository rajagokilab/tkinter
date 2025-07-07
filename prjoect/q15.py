import tkinter as tk
from tkinter import ttk, messagebox

class MultiStepForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📋 Multi-Step Registration Form")
        self.geometry("400x300")
        self.resizable(False, False)

        # Store user inputs
        self.data = {
            "name": tk.StringVar(),
            "age": tk.IntVar(value=18),
            "course": tk.StringVar(),
            "skill": tk.StringVar()
        }

        # Create frames
        self.frames = {}
        for F in (PersonalInfoFrame, CourseSkillFrame, SummaryFrame):
            frame = F(self)
            self.frames[F] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.show_frame(PersonalInfoFrame)

    def show_frame(self, frame_class):
        frame = self.frames[frame_class]
        frame.tkraise()

class PersonalInfoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        ttk.Label(self, text="Step 1: Personal Info", font=("Helvetica", 16)).pack(pady=10)

        # Name
        ttk.Label(self, text="Name:").pack(anchor="w", pady=(10, 0))
        self.name_entry = ttk.Entry(self, textvariable=parent.data["name"])
        self.name_entry.pack(fill="x")

        # Age
        ttk.Label(self, text="Age:").pack(anchor="w", pady=(10, 0))
        self.age_spin = ttk.Spinbox(self, from_=10, to=100, textvariable=parent.data["age"])
        self.age_spin.pack(fill="x")

        # Navigation
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20, fill="x")
        next_btn = ttk.Button(btn_frame, text="Next →", command=self.next_step)
        next_btn.pack(side="right")

    def next_step(self):
        if not self.master.data["name"].get().strip():
            messagebox.showwarning("Input Error", "Please enter your name.")
            return
        self.master.show_frame(CourseSkillFrame)

class CourseSkillFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        ttk.Label(self, text="Step 2: Course & Skill Info", font=("Helvetica", 16)).pack(pady=10)

        # Course Combobox
        ttk.Label(self, text="Select Course:").pack(anchor="w", pady=(10, 0))
        courses = ["Math", "Science", "Art", "History", "Programming"]
        self.course_combo = ttk.Combobox(self, textvariable=parent.data["course"], values=courses, state="readonly")
        self.course_combo.pack(fill="x")
        self.course_combo.current(0)

        # Skill Entry
        ttk.Label(self, text="Your Skill Level:").pack(anchor="w", pady=(10, 0))
        self.skill_entry = ttk.Entry(self, textvariable=parent.data["skill"])
        self.skill_entry.pack(fill="x")

        # Navigation buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20, fill="x")
        back_btn = ttk.Button(btn_frame, text="← Back", command=lambda: parent.show_frame(PersonalInfoFrame))
        back_btn.pack(side="left")
        next_btn = ttk.Button(btn_frame, text="Next →", command=self.next_step)
        next_btn.pack(side="right")

    def next_step(self):
        if not self.master.data["skill"].get().strip():
            messagebox.showwarning("Input Error", "Please enter your skill level.")
            return
        self.master.show_frame(SummaryFrame)
        self.master.frames[SummaryFrame].update_summary()

class SummaryFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=20)

        ttk.Label(self, text="Step 3: Summary & Submit", font=("Helvetica", 16)).pack(pady=10)

        self.summary_label = ttk.Label(self, text="", justify="left", font=("Helvetica", 12))
        self.summary_label.pack(pady=10)

        # Navigation buttons
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=20, fill="x")
        back_btn = ttk.Button(btn_frame, text="← Back", command=lambda: parent.show_frame(CourseSkillFrame))
        back_btn.pack(side="left")
        submit_btn = ttk.Button(btn_frame, text="Submit", command=self.submit_form)
        submit_btn.pack(side="right")

    def update_summary(self):
        d = self.master.data
        summary = (
            f"Name: {d['name'].get()}\n"
            f"Age: {d['age'].get()}\n"
            f"Course: {d['course'].get()}\n"
            f"Skill Level: {d['skill'].get()}"
        )
        self.summary_label.config(text=summary)

    def submit_form(self):
        messagebox.showinfo("Form Submitted", "Your registration has been submitted successfully!")
        self.master.destroy()

if __name__ == "__main__":
    MultiStepForm().mainloop()
