import tkinter as tk
from tkinter import messagebox

# 41. Show info message
def show_info():
    messagebox.showinfo("Information", "This is an info message.")

# 42. Confirm closing the app
def confirm_exit():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# 43. Yes/No confirmation
def ask_yes_no():
    response = messagebox.askquestion("Delete", "Are you sure you want to delete this item?")
    print("User responded:", response)

# 44. Show warning
def show_warning():
    messagebox.showwarning("Warning", "This action may cause issues!")

# 45. Confirm form submission
def submit_form():
    if messagebox.askokcancel("Submit", "Do you want to submit the data?"):
        print("Form submitted!")
    else:
        print("Submission canceled.")

# Main window
root = tk.Tk()
root.title("Tkinter Dialogs Example")
root.geometry("400x300")

# Buttons for each task
tk.Button(root, text="Show Info", command=show_info).pack(pady=5)
tk.Button(root, text="Confirm Exit", command=confirm_exit).pack(pady=5)
tk.Button(root, text="Ask Yes/No", command=ask_yes_no).pack(pady=5)
tk.Button(root, text="Show Warning", command=show_warning).pack(pady=5)

# Simple form area
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(form_frame).grid(row=0, column=1, padx=5, pady=5)
tk.Button(form_frame, text="Submit", command=submit_form).grid(row=1, columnspan=2, pady=10)

# Override window close button
root.protocol("WM_DELETE_WINDOW", confirm_exit)

root.mainloop()
