import tkinter as tk

def update_counts(event=None):
    text_content = text_area.get("1.0", tk.END).strip()
    char_count = len(text_content)
    word_count = len(text_content.split()) if text_content else 0
    count_label.config(text=f"Words: {word_count} | Characters: {char_count}")

def reset_text():
    text_area.delete("1.0", tk.END)
    update_counts()

root = tk.Tk()
root.title("Live Typing Tracker")

text_area = tk.Text(root, width=50, height=10)
text_area.pack(padx=10, pady=10)
text_area.bind("<Key>", update_counts)

count_label = tk.Label(root, text="Words: 0 | Characters: 0", font=("Arial", 12))
count_label.pack(pady=5)

reset_btn = tk.Button(root, text="Reset", command=reset_text)
reset_btn.pack(pady=5)

root.mainloop()
