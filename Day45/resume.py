import tkinter as tk
from tkinter import filedialog, messagebox

class ResumeBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("Resume Builder")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack()

        # Name
        tk.Label(frame, text="Name:").grid(row=0, column=0, sticky="w")
        self.name_entry = tk.Entry(frame, width=50)
        self.name_entry.grid(row=0, column=1, pady=5)

        # Skills
        tk.Label(frame, text="Skills:").grid(row=1, column=0, sticky="nw")
        self.skills_text = tk.Text(frame, width=38, height=5)
        self.skills_text.grid(row=1, column=1, pady=5)

        # Experience
        tk.Label(frame, text="Experience:").grid(row=2, column=0, sticky="nw")
        self.exp_text = tk.Text(frame, width=38, height=8)
        self.exp_text.grid(row=2, column=1, pady=5)

        # Save Button
        save_btn = tk.Button(frame, text="Save Resume", command=self.save_resume)
        save_btn.grid(row=3, column=0, columnspan=2, pady=10)

    def save_resume(self):
        name = self.name_entry.get().strip()
        skills = self.skills_text.get("1.0", tk.END).strip()
        experience = self.exp_text.get("1.0", tk.END).strip()

        if not name:
            messagebox.showwarning("Input Error", "Please enter your name.")
            return

        content = f"Name: {name}\n\nSkills:\n{skills}\n\nExperience:\n{experience}\n"

        filepath = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            title="Save Resume As"
        )
        if not filepath:
            return

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Success", "Resume saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = ResumeBuilder(root)
    root.mainloop()
