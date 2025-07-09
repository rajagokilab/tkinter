import tkinter as tk

# Mapping arrow keys to colors
color_map = {
    "Left": "lightblue",
    "Right": "lightgreen",
    "Up": "lightyellow",
    "Down": "lightpink"
}

def change_color(event):
    key = event.keysym
    if key in color_map:
        color = color_map[key]
        color_frame.config(bg=color)
        color_label.config(text=f"Current Color: {color}")

root = tk.Tk()
root.title("Dynamic Color Picker")
root.geometry("300x200")

color_frame = tk.Frame(root, width=280, height=120, bg="white", relief="ridge", borderwidth=2)
color_frame.pack(pady=20)

color_label = tk.Label(root, text="Current Color: white", font=("Arial", 14))
color_label.pack()

# Bind arrow keys
root.bind("<Left>", change_color)
root.bind("<Right>", change_color)
root.bind("<Up>", change_color)
root.bind("<Down>", change_color)

# Set focus to root so keys are captured
root.focus_set()

root.mainloop()
