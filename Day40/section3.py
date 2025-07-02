import tkinter as tk
import sys

def task1():
    # Fixed size 400x300, no resizing
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(False, False)
    root.title("Task 1: Fixed Size")
    root.mainloop()

def task2():
    # Change title to "My First GUI App"
    root = tk.Tk()
    root.title("My First GUI App")
    root.geometry("300x200")
    root.mainloop()

def task3():
    # Set custom icon (requires 'icon.ico' in the same directory)
    root = tk.Tk()
    root.title("Task 3: Custom Icon")
    try:
        root.iconbitmap("icon.ico")
    except Exception as e:
        print("Icon file not found or invalid:", e)
    root.geometry("300x200")
    root.mainloop()

def task4():
    # Window at position (200, 100)
    root = tk.Tk()
    root.geometry("300x200+200+100")
    root.title("Task 4: Positioned Window")
    root.mainloop()

def task5():
    # Display current window width and height dynamically
    root = tk.Tk()
    root.title("Task 5: Dynamic Size Display")
    label = tk.Label(root, text="Width: ?, Height: ?")
    label.pack(padx=20, pady=20)

    def update_size(event):
        w = root.winfo_width()
        h = root.winfo_height()
        label.config(text=f"Width: {w}, Height: {h}")

    root.bind("<Configure>", update_size)
    root.geometry("400x300")
    root.mainloop()

def task6():
    # Disable only horizontal resizing
    root = tk.Tk()
    root.title("Task 6: Disable Horizontal Resize")
    root.geometry("400x300")
    root.resizable(False, True)
    root.mainloop()

def task7():
    # Resizable notepad-style window using Text widget
    root = tk.Tk()
    root.title("Task 7: Notepad Style")
    root.geometry("600x400")
    text = tk.Text(root)
    text.pack(fill="both", expand=True)
    root.mainloop()

def task8():
    # Centered window on screen by calculating screen width and height
    root = tk.Tk()
    root.title("Task 8: Centered Window")

    win_width = 400
    win_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - win_width) // 2
    y = (screen_height - win_height) // 2

    root.geometry(f"{win_width}x{win_height}+{x}+{y}")
    root.mainloop()

def task9():
    # Splash screen that disappears after 3 seconds
    splash = tk.Tk()
    splash.title("Splash Screen")
    splash.geometry("300x150")
    splash_label = tk.Label(splash, text="Welcome to My App!", font=("Arial", 16))
    splash_label.pack(expand=True)

    def close_splash():
        splash.destroy()

    splash.after(3000, close_splash)
    splash.mainloop()

def task10():
    # Open window maximized using zoomed state if on Windows
    root = tk.Tk()
    root.title("Task 10: Maximized Window")
    if sys.platform.startswith("win"):
        root.state("zoomed")
    else:
        # For other platforms, maximize (works in many)
        root.attributes("-zoomed", True)
    root.mainloop()

if __name__ == "__main__":
    # Uncomment the task you want to run:
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    task10()
    print("Uncomment a task() call at the bottom to run a demo.")
