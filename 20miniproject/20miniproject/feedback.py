import tkinter as tk
from tkinter import messagebox

def save_feedback():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    comments = comments_text.get("1.0", tk.END).strip()
    rating = rating_spinbox.get()

    if not name or not email:
        messagebox.showwarning("Input Error", "Please enter both name and email.")
        return

    feedback = f"Name: {name}, Email: {email}, Rating: {rating}, Comments: {comments}"
    feedback_listbox.insert(tk.END, feedback)

    thank_you_label.config(text=f"Thank you for your feedback, {name}!")

    # Clear inputs
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    comments_text.delete("1.0", tk.END)
    rating_spinbox.delete(0, tk.END)
    rating_spinbox.insert(0, "5")

# Main window
root = tk.Tk()
root.title("Feedback Form with Rating")
root.geometry("550x500")
root.configure(padx=15, pady=15)

# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(fill=tk.X, pady=10)

tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(input_frame, width=40)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Email:").grid(row=1, column=0, sticky="w")
email_entry = tk.Entry(input_frame, width=40)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Comments:").grid(row=2, column=0, sticky="nw", pady=5)
comments_text = tk.Text(input_frame, width=40, height=5)
comments_text.grid(row=2, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Rating (1-10):").grid(row=3, column=0, sticky="w")
rating_spinbox = tk.Spinbox(input_frame, from_=1, to=10, width=5)
rating_spinbox.grid(row=3, column=1, sticky="w", padx=10, pady=5)
rating_spinbox.delete(0, tk.END)
rating_spinbox.insert(0, "5")

# Save Button
save_btn = tk.Button(root, text="Submit Feedback", command=save_feedback)
save_btn.pack(pady=10)

# Feedback Listbox with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

feedback_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
feedback_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=feedback_listbox.yview)

# Thank You Label
thank_you_label = tk.Label(root, text="", fg="green", font=("Arial", 12))
thank_you_label.pack(pady=10)

root.mainloop()
