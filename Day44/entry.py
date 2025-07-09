import tkinter as tk

def update_count(event=None):
    text = entry.get()
    count_label.config(text=f"Characters: {len(text)}")

root = tk.Tk()
root.title("Entry Field Character Counter")
root.geometry("300x120")

entry = tk.Entry(root, font=("Arial", 14), width=25)
entry.pack(pady=20)
entry.bind("<KeyRelease>", update_count)

count_label = tk.Label(root, text="Characters: 0", font=("Arial", 12))
count_label.pack()

root.mainloop()
