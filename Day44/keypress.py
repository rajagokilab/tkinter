import tkinter as tk

def on_key_press(event):
    key_name = event.keysym
    current_key_label.config(text=f"Key Pressed: {key_name}")
    key_log.insert("end", f"{key_name}\n")
    key_log.see("end")  # auto-scroll to latest

    if key_name == "Escape":
        root.destroy()

# Setup main window
root = tk.Tk()
root.title("Live Key Press Tracker")
root.geometry("400x300")

# Display currently pressed key
current_key_label = tk.Label(root, text="Press any key...", font=("Arial", 16))
current_key_label.pack(pady=10)

# Text widget for log
key_log = tk.Text(root, height=10, width=40, state="normal")
key_log.pack(pady=10)

# Bind key press event globally
root.bind("<KeyPress>", on_key_press)

# Set focus so key events are captured
root.focus_set()

root.mainloop()
