import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Hide root, we use Toplevels for each task


# Task 1: Three labels stacked vertically using pack()
def task1():
    win = tk.Toplevel()
    win.title("Task 1: Vertical Labels")
    for text in ["Label 1", "Label 2", "Label 3"]:
        tk.Label(win, text=text).pack()


# Task 2: Horizontal layout using pack(side="left") for three buttons
def task2():
    win = tk.Toplevel()
    win.title("Task 2: Horizontal Buttons")
    for i in range(1, 4):
        tk.Button(win, text=f"Button {i}").pack(side="left")


# Task 3: Login form with grid()
def task3():
    win = tk.Toplevel()
    win.title("Task 3: Grid Login Form")
    tk.Label(win, text="Username").grid(row=0, column=0)
    tk.Entry(win).grid(row=0, column=1)
    tk.Label(win, text="Password").grid(row=1, column=0)
    tk.Entry(win, show="*").grid(row=1, column=1)


# Task 4: 3x3 button matrix
def task4():
    win = tk.Toplevel()
    win.title("Task 4: 3x3 Button Grid")
    for i in range(3):
        for j in range(3):
            tk.Button(win, text=f"{i*3 + j + 1}").grid(row=i, column=j)


# Task 5: grid(sticky='E')
def task5():
    win = tk.Toplevel()
    win.title("Task 5: Sticky Right Label")
    tk.Label(win, text="Right Aligned").grid(row=0, column=0, sticky="E")


# Task 6: place() at (50, 50) and center
def task6():
    win = tk.Toplevel()
    win.title("Task 6: place() Example")
    win.geometry("300x200")
    tk.Label(win, text="Placed at 50, 50").place(x=50, y=50)
    tk.Label(win, text="Centered").place(relx=0.5, rely=0.5, anchor="center")


# Task 7: Mixed geometry error
def task7():
    win = tk.Toplevel()
    win.title("Task 7: Mixed Geometry")
    tk.Label(win, text="Title using pack()").pack()
    try:
        tk.Label(win, text="Username").grid(row=0, column=0)
        tk.Entry(win).grid(row=0, column=1)
    except Exception as e:
        tk.Label(win, text=f"Error: {e}").pack()


# Task 8: grid() form with padding
def task8():
    win = tk.Toplevel()
    win.title("Task 8: Grid with Padding")
    tk.Label(win, text="Name").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(win).grid(row=0, column=1, padx=10, pady=10)
    tk.Label(win, text="Email").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(win).grid(row=1, column=1, padx=10, pady=10)


# Task 9: Form using place()
def task9():
    win = tk.Toplevel()
    win.title("Task 9: Form with place()")
    win.geometry("300x200")
    tk.Label(win, text="Username").place(x=30, y=30)
    tk.Entry(win).place(x=100, y=30)
    tk.Label(win, text="Password").place(x=30, y=70)
    tk.Entry(win, show="*").place(x=100, y=70)
    tk.Button(win, text="Login").place(x=120, y=110)


# Task 10: Sidebar + main content
def task10():
    win = tk.Toplevel()
    win.title("Task 10: Sidebar Layout")
    sidebar = tk.Frame(win, bg="lightgray", width=100)
    sidebar.pack(side="left", fill="y")

    content = tk.Frame(win, bg="white")
    content.pack(fill="both", expand=True)

    tk.Label(sidebar, text="Menu", bg="lightgray").pack(pady=10)
    tk.Label(content, text="Main Content", bg="white").pack(pady=20)


# Run all tasks
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

tk.mainloop()
