import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = name_entry.get().strip()
    comments = comments_text.get("1.0", tk.END).strip()
    if not name or not comments:
        messagebox.showwarning("Incomplete", "Please enter both your name and comments.")
        return
    messagebox.showinfo("Thank you!", f"Thanks for your feedback, {name}!")
    name_entry.delete(0, tk.END)
    comments_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Feedback Collector")
root.geometry("400x300")

# Name label and entry
tk.Label(root, text="Name:").pack(anchor='w', padx=10, pady=(10,0))
name_entry = tk.Entry(root, width=50)
name_entry.pack(padx=10)

# Comments label and text box
tk.Label(root, text="Comments:").pack(anchor='w', padx=10, pady=(10,0))
comments_text = tk.Text(root, width=50, height=10)
comments_text.pack(padx=10)

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_feedback)
submit_btn.pack(pady=10)

root.mainloop()
