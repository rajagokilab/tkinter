import tkinter as tk

def update_counts(event=None):
    text = text_widget.get("1.0", tk.END)
    chars = len(text) - 1  # subtract trailing newline
    words = len(text.split())
    count_label.config(text=f"Words: {words} | Characters: {chars}")

def reset_text():
    text_widget.delete("1.0", tk.END)
    update_counts()

# Main window
root = tk.Tk()
root.title("Live Typing Tracker")
root.geometry("500x400")
root.configure(padx=15, pady=15)

# Text widget
text_widget = tk.Text(root, wrap=tk.WORD, font=("Arial", 12), height=15)
text_widget.pack(fill=tk.BOTH, expand=True)
text_widget.bind("<Key>", update_counts)

# Count label
count_label = tk.Label(root, text="Words: 0 | Characters: 0", font=("Arial", 12))
count_label.pack(pady=10)

# Reset button
reset_btn = tk.Button(root, text="Reset", command=reset_text)
reset_btn.pack()

root.mainloop()
