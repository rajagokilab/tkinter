import tkinter as tk

# Functions
def save_text():
    content = text_editor.get("1.0", tk.END).strip()
    print("Saved Content:\n" + content)

def clear_text():
    text_editor.delete("1.0", tk.END)
    update_word_count()

def load_preset():
    preset = "This is some preset content.\nYou can edit this text as needed."
    text_editor.delete("1.0", tk.END)
    text_editor.insert("1.0", preset)
    update_word_count()

def update_word_count(event=None):
    content = text_editor.get("1.0", tk.END)
    words = len(content.strip().split())
    word_count_label.config(text=f"Word Count: {words}")

# Main Window
root = tk.Tk()
root.title("Mini Notepad App")
root.geometry("500x400")
root.configure(padx=10, pady=10)

# === Text Editor ===
text_editor = tk.Text(root, wrap="word", height=15, width=60)
text_editor.pack(pady=(0, 10))
text_editor.bind("<KeyRelease>", update_word_count)

# === Button Frame ===
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

save_btn = tk.Button(button_frame, text="Save", command=save_text)
save_btn.pack(side="left", padx=5)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_text)
clear_btn.pack(side="left", padx=5)

load_btn = tk.Button(button_frame, text="Load Preset", command=load_preset)
load_btn.pack(side="left", padx=5)

# === Word Count Label ===
word_count_label = tk.Label(root, text="Word Count: 0", font=("Arial", 10))
word_count_label.pack(pady=5)

root.mainloop()
