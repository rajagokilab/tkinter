import tkinter as tk

def on_enter_label(event):
    event.widget.config(fg="blue")

def on_leave_label(event):
    event.widget.config(fg="black")

def on_enter_button(event):
    event.widget.config(bg="lightgreen")

def on_leave_button(event):
    event.widget.config(bg=default_btn_bg)

root = tk.Tk()
root.title("Mouse Hover UI Effects")
root.geometry("300x150")

# Label with hover effect
label = tk.Label(root, text="Hover over me!", font=("Arial", 14), fg="black")
label.pack(pady=15)
label.bind("<Enter>", on_enter_label)
label.bind("<Leave>", on_leave_label)

# Button with hover effect
btn = tk.Button(root, text="Hover Button")
btn.pack(pady=15)

default_btn_bg = btn.cget("background")
btn.bind("<Enter>", on_enter_button)
btn.bind("<Leave>", on_leave_button)

root.mainloop()
