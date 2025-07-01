import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def log_temperature():
    temp = temp_entry.get().strip()
    if not temp:
        messagebox.showwarning("Input Error", "Please enter a temperature.")
        return
    try:
        float(temp)  # Validate if it’s a number
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_text.insert(tk.END, f"{timestamp} - {temp}°\n")
    log_text.see(tk.END)  # Scroll to the end
    temp_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Temperature Logger")
root.geometry("400x300")

tk.Label(root, text="Enter Temperature:").pack(pady=(10,0))
temp_entry = tk.Entry(root, width=30)
temp_entry.pack()

log_btn = tk.Button(root, text="Log Temperature", command=log_temperature)
log_btn.pack(pady=10)

log_text = tk.Text(root, width=50, height=10)
log_text.pack(pady=10)

root.mainloop()
