import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Schedule to run again after 1 second

root = tk.Tk()
root.title("Digital Clock")
root.geometry("250x100")

clock_label = tk.Label(root, font=('Arial', 48), fg='black')
clock_label.pack(expand=True)

update_clock()  # Start the clock updates

root.mainloop()
