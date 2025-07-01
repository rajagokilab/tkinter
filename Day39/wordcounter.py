import tkinter as tk

def count_words():
    text = text_area.get("1.0", tk.END).strip()
    # Split text by whitespace and filter out empty strings
    words = [word for word in text.split() if word]
    word_count = len(words)
    count_label.config(text=f"Word Count: {word_count}")

root = tk.Tk()
root.title("Word Counter")
root.geometry("400x300")

text_area = tk.Text(root, wrap='word', width=50, height=10)
text_area.pack(padx=10, pady=10)

count_btn = tk.Button(root, text="Count Words", command=count_words)
count_btn.pack(pady=5)

count_label = tk.Label(root, text="Word Count: 0", font=("Arial", 14))
count_label.pack(pady=10)

root.mainloop()
