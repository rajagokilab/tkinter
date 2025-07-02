import tkinter as tk
from tkinter import messagebox
import random

def task1():
    def say_hello():
        print("Hello from Task 1!")
    root = tk.Tk()
    root.title("Task 1: Button → print")
    tk.Button(root, text="Click me", command=say_hello).pack(padx=20, pady=20)
    root.mainloop()

def task2():
    def key_pressed(event):
        print(f"Key pressed: {event.keysym}")
    root = tk.Tk()
    root.title("Task 2: Key press")
    root.geometry("300x100")
    tk.Label(root, text="Press any key...").pack(pady=20)
    root.bind("<Key>", key_pressed)
    root.mainloop()

def task3():
    def toggle_label(event):
        label.config(text="Clicked!" if label.cget("text") == "Click me" else "Click me")
    root = tk.Tk()
    root.title("Task 3: Label click")
    label = tk.Label(root, text="Click me", width=20, relief="ridge")
    label.pack(padx=20, pady=20)
    label.bind("<Button-1>", toggle_label)
    root.mainloop()

def task4():
    colors = ["lightblue", "lightgreen", "lavender", "misty rose", "lightyellow"]
    def change_bg():
        root.config(bg=random.choice(colors))
    root = tk.Tk()
    root.title("Task 4: Change background")
    tk.Button(root, text="Change background", command=change_bg).pack(padx=20, pady=20)
    root.mainloop()

def task5():
    def display_text():
        label.config(text=entry.get())
    root = tk.Tk()
    root.title("Task 5: Display Entry Text")
    entry = tk.Entry(root, width=25)
    entry.pack(padx=10, pady=10)
    label = tk.Label(root, text="", fg="blue")
    label.pack()
    tk.Button(root, text="Display", command=display_text).pack(pady=10)
    root.mainloop()

def task6():
    def show_message():
        messagebox.showinfo("Greeting", "Hello from Task 6!")
    root = tk.Tk()
    root.title("Task 6: Message Box")
    tk.Button(root, text="Say hi", command=show_message).pack(padx=20, pady=20)
    root.mainloop()

def task7():
    def on_enter(event):
        print("You entered:", entry.get())
    root = tk.Tk()
    root.title("Task 7: Entry + Enter Key")
    entry = tk.Entry(root, width=30)
    entry.pack(padx=20, pady=20)
    entry.bind("<Return>", on_enter)
    entry.focus_set()
    root.mainloop()

def task8():
    def update_label(event):
        direction = "Up" if event.keysym == "Up" else "Down"
        label.config(text=direction)
    root = tk.Tk()
    root.title("Task 8: Arrow Keys")
    label = tk.Label(root, text="Press ↑ or ↓", width=20)
    label.pack(padx=20, pady=20)
    root.bind("<Up>", update_label)
    root.bind("<Down>", update_label)
    root.mainloop()

def task9():
    def show_mouse_position(event):
        label.config(text=f"x={event.x}, y={event.y}")
    root = tk.Tk()
    root.title("Task 9: Mouse Tracker")
    root.geometry("300x150")
    label = tk.Label(root, text="Move mouse inside window", width=30, relief="sunken")
    label.pack(fill="both", expand=True, padx=10, pady=10)
    root.bind("<Motion>", show_mouse_position)
    root.mainloop()

def task10():
    def on_hover(event):
        button.config(text="Hello!")
    def on_leave(event):
        button.config(text="Hover over me")
    root = tk.Tk()
    root.title("Task 10: Hover")
    button = tk.Button(root, text="Hover over me")
    button.pack(padx=20, pady=20)
    button.bind("<Enter>", on_hover)
    button.bind("<Leave>", on_leave)
    root.mainloop()

if __name__ == "__main__":
    # Uncomment one task below to run it:
    task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    # task10()
    print("Uncomment a task() call at the bottom to run a demo.")
