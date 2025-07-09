import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Widget States (Tasks 1–15)")
root.geometry("600x850")

# Task 1: Button disables itself when clicked
def disable_self(btn):
    btn.config(state="disabled")

btn1 = tk.Button(root, text="Task 1: Click to Disable", command=lambda: disable_self(btn1))
btn1.pack(pady=5)

# Task 2: Checkbutton disables a text input field when selected
def toggle_entry():
    state = "disabled" if check2_var.get() else "normal"
    entry2.config(state=state)

check2_var = tk.BooleanVar()
check2 = tk.Checkbutton(root, text="Task 2: Disable Entry", variable=check2_var, command=toggle_entry)
check2.pack()
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Task 3: One button disables the other
def disable_other():
    btn3b.config(state="disabled")

btn3a = tk.Button(root, text="Task 3A: Disables B", command=disable_other)
btn3a.pack()
btn3b = tk.Button(root, text="Task 3B")
btn3b.pack(pady=5)

# Task 4: Form with checkbox enabling Submit
def toggle_submit():
    submit_btn.config(state="normal" if check4_var.get() else "disabled")

check4_var = tk.BooleanVar()
check4 = tk.Checkbutton(root, text="Agree to terms", variable=check4_var, command=toggle_submit)
check4.pack()
submit_btn = tk.Button(root, text="Task 4: Submit", state="disabled")
submit_btn.pack(pady=5)

# Task 5: Entry becomes non-editable when button is clicked
def disable_entry5():
    entry5.config(state="disabled")

entry5 = tk.Entry(root)
entry5.pack()
btn5 = tk.Button(root, text="Task 5: Lock Entry", command=disable_entry5)
btn5.pack(pady=5)

# Task 6: Button enabled after 5 seconds
def enable_btn6():
    btn6.config(state="normal")

btn6 = tk.Button(root, text="Task 6: Wait 5 sec", state="disabled")
btn6.pack()
root.after(5000, enable_btn6)

# Task 7: Label with activeforeground change on hover (simulate with binding)
def on_enter7(event): lbl7.config(fg="red")
def on_leave7(event): lbl7.config(fg="black")

lbl7 = tk.Label(root, text="Task 7: Hover Me", fg="black")
lbl7.bind("<Enter>", on_enter7)
lbl7.bind("<Leave>", on_leave7)
lbl7.pack(pady=5)

# Task 8: Button with state="active" (changes on hover)
btn8 = tk.Button(root, text="Task 8: Hover Active", activebackground="lightblue")
btn8.pack(pady=5)

# Task 9: Toggle widget states using Combobox
def toggle_widgets(event):
    selected = combo9.get()
    state = "disabled" if selected == "Disable" else "normal"
    entry9.config(state=state)
    btn9.config(state=state)

combo9 = ttk.Combobox(root, values=["Enable", "Disable"])
combo9.set("Enable")
combo9.bind("<<ComboboxSelected>>", toggle_widgets)
combo9.pack()
entry9 = tk.Entry(root)
entry9.pack()
btn9 = tk.Button(root, text="Task 9: Toggle Me")
btn9.pack(pady=5)

# Task 10: Disable group of buttons using a loop
btn_group = []
for i in range(3):
    b = tk.Button(root, text=f"Task 10 Btn {i+1}")
    b.pack()
    btn_group.append(b)

def disable_group():
    for b in btn_group:
        b.config(state="disabled")

btn10_toggle = tk.Button(root, text="Task 10: Disable Group", command=disable_group)
btn10_toggle.pack(pady=5)

# Task 11: Reset all widgets to default state
def reset_all():
    btn1.config(state="normal")
    entry2.config(state="normal")
    check2_var.set(False)
    btn3b.config(state="normal")
    check4_var.set(False)
    submit_btn.config(state="disabled")
    entry5.config(state="normal")
    btn6.config(state="disabled")
    root.after(5000, enable_btn6)
    lbl7.config(fg="black")
    entry9.config(state="normal")
    btn9.config(state="normal")
    combo9.set("Enable")
    for b in btn_group:
        b.config(state="normal")
    spin13.config(state="normal")
    rb_var.set("")
    entry14.config(state="normal")
    entry15.config(state="normal")
    btn15.config(state="normal")
    lbl15.config(text="Ready")

reset_btn = tk.Button(root, text="Task 11: Reset All", command=reset_all, bg="lightgray")
reset_btn.pack(pady=5)

# Task 12: Visual state change (bg/fg)
def toggle_colors():
    state = btn12.cget("state")
    if state == "normal":
        btn12.config(bg="gray", fg="white", state="disabled")
    else:
        btn12.config(bg="SystemButtonFace", fg="black", state="normal")

btn12 = tk.Button(root, text="Task 12: Color Toggle", command=toggle_colors)
btn12.pack(pady=5)

# Task 13: Disable Spinbox with another widget
def disable_spin():
    spin13.config(state="disabled")

spin13 = tk.Spinbox(root, from_=0, to=10)
spin13.pack()
btn13 = tk.Button(root, text="Task 13: Disable Spinbox", command=disable_spin)
btn13.pack(pady=5)

# Task 14: Radio buttons disabling other controls
def update_radio():
    if rb_var.get() == "Disable":
        entry14.config(state="disabled")
    else:
        entry14.config(state="normal")

rb_var = tk.StringVar()
rb1 = tk.Radiobutton(root, text="Enable", variable=rb_var, value="Enable", command=update_radio)
rb2 = tk.Radiobutton(root, text="Disable", variable=rb_var, value="Disable", command=update_radio)
rb1.pack()
rb2.pack()
entry14 = tk.Entry(root)
entry14.pack(pady=5)

# Task 15: Combine controls and toggle their states
def toggle_15():
    new_state = "disabled" if entry15.cget("state") == "normal" else "normal"
    entry15.config(state=new_state)
    btn15.config(state=new_state)
    lbl15.config(text="Disabled" if new_state == "disabled" else "Ready")

entry15 = tk.Entry(root)
entry15.pack()
btn15 = tk.Button(root, text="Task 15: Combo Toggle", command=toggle_15)
btn15.pack()
lbl15 = tk.Label(root, text="Ready")
lbl15.pack(pady=5)

root.mainloop()
