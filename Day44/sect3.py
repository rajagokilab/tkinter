import tkinter as tk
from tkinter import messagebox

def on_key_press(event):
    key_label.config(text=f"Key Pressed: {event.keysym}")
    print(f"Pressed: {event.keysym}")

def on_key_release(event):
    if event.keysym == "Shift_L" or event.keysym == "Shift_R":
        print("Shift released")

def submit_login(event=None):
    username = username_entry.get()
    password = password_entry.get()
    print(f"Login submitted: {username} / {password}")

def move_shape(event):
    if event.keysym == "Left":
        canvas.move(rect, -10, 0)
    elif event.keysym == "Right":
        canvas.move(rect, 10, 0)

def toggle_bg(event):
    if event.keysym.upper() == "B":
        root.config(bg="black")
    elif event.keysym.upper() == "W":
        root.config(bg="white")

def close_app(event):
    root.destroy()

def save_file(event):
    print("Simulated Save (Ctrl+S)")

def show_help(event):
    messagebox.showinfo("Help", "This is the help dialog.")

def capitalize_key(event):
    current = capital_entry.get()
    capital_entry.delete(0, tk.END)
    capital_entry.insert(0, current + event.char.upper())
    return "break"  # Prevent normal insertion

root = tk.Tk()
root.title("Keyboard Events Demo")
root.geometry("500x500")

# Task 26 & 27: Log key press and display key name
key_label = tk.Label(root, text="Press any key...", font=("Arial", 14))
key_label.pack(pady=10)
root.bind("<KeyPress>", on_key_press)

# Task 28: Login form with Enter to submit
tk.Label(root, text="Login Form").pack()
username_entry = tk.Entry(root)
username_entry.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
submit_btn = tk.Button(root, text="Submit", command=submit_login)
submit_btn.pack()
root.bind("<Return>", submit_login)

# Task 29: Move shape with arrow keys
canvas = tk.Canvas(root, width=300, height=100, bg="lightgray")
canvas.pack(pady=10)
rect = canvas.create_rectangle(130, 30, 170, 70, fill="blue")
root.bind("<Left>", move_shape)
root.bind("<Right>", move_shape)

# Task 30: Toggle background color (B/W)
root.bind("<KeyPress-b>", toggle_bg)
root.bind("<KeyPress-w>", toggle_bg)

# Task 31: Track key release (Shift)
root.bind("<KeyRelease>", on_key_release)

# Task 32: Press Esc to close
root.bind("<Escape>", close_app)

# Task 33: Ctrl+S to simulate save
root.bind("<Control-s>", save_file)

# Task 34: F1 shows help
root.bind("<F1>", show_help)

# Task 35: Capitalize all input in an Entry
tk.Label(root, text="Capital Entry:").pack()
capital_entry = tk.Entry(root)
capital_entry.pack()
capital_entry.bind("<KeyPress>", capitalize_key)

root.mainloop()
