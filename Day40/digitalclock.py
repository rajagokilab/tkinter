import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # schedule to run again after 1 second

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.resizable(False, False)

label = tk.Label(root, font=("Helvetica", 40), fg="black")
label.place(relx=0.5, rely=0.5, anchor="center")

update_time()  # start the clock
root.mainloop()
