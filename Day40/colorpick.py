import tkinter as tk

def change_color(color):
    root.config(bg=color)
    selected_label.config(text=f"Selected Color: {color}", bg=color)

root = tk.Tk()
root.title("Color Picker")
root.geometry("400x150")

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

button_frame = tk.Frame(root)
button_frame.pack(side="left", padx=10, pady=20)

for color in colors:
    btn = tk.Button(button_frame, text=color.capitalize(), bg=color, fg="white" if color != "yellow" else "black",
                    width=10, command=lambda c=color: change_color(c))
    btn.pack(pady=5)

selected_label = tk.Label(root, text="Selected Color: None", font=("Arial", 14))
selected_label.pack(pady=20, fill="both", expand=True)

root.mainloop()
