import tkinter as tk

def save_text():
    content = text_area.get("1.0", tk.END).strip()
    print("Saved content:\n", content)
    update_word_count()

def clear_text():
    text_area.delete("1.0", tk.END)
    update_word_count()

def load_preset():
    preset = "This is some preset text.\nYou can edit or clear it."
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, preset)
    update_word_count()

def update_word_count(event=None):
    content = text_area.get("1.0", tk.END).strip()
    words = len(content.split()) if content else 0
    word_count_label.config(text=f"Word count: {words}")

root = tk.Tk()
root.title("Mini Notepad")
root.geometry("400x400")

# Text widget for editing area
text_area = tk.Text(root, wrap="word")
text_area.pack(expand=True, fill="both", padx=10, pady=10)

# Buttons frame
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

save_btn = tk.Button(button_frame, text="Save", command=save_text)
save_btn.pack(side="left", padx=5)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_text)
clear_btn.pack(side="left", padx=5)

load_btn = tk.Button(button_frame, text="Load Preset", command=load_preset)
load_btn.pack(side="left", padx=5)

# Word count label
word_count_label = tk.Label(root, text="Word count: 0")
word_count_label.pack(pady=5)

# Bind key release to update word count live
text_area.bind("<KeyRelease>", update_word_count)

root.mainloop()
