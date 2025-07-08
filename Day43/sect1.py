import tkinter as tk

root = tk.Tk()
root.title("Tkinter Frames Example")
root.geometry("800x600")

# 1. Create a Frame widget and place a label inside it.
frame1 = tk.Frame(root, bg="lightgray")
frame1.pack(pady=10)
tk.Label(frame1, text="This is inside Frame 1").pack()

# 2. Add three Buttons inside a Frame using pack().
frame2 = tk.Frame(root, bg="white")
frame2.pack(pady=10)
tk.Button(frame2, text="Button 1").pack(side="left", padx=5)
tk.Button(frame2, text="Button 2").pack(side="left", padx=5)
tk.Button(frame2, text="Button 3").pack(side="left", padx=5)

# 3. Add a Label, Entry, and Button inside a Frame using grid().
frame3 = tk.Frame(root, bg="lightblue")
frame3.pack(pady=10)
tk.Label(frame3, text="Name:").grid(row=0, column=0)
tk.Entry(frame3).grid(row=0, column=1)
tk.Button(frame3, text="Submit").grid(row=0, column=2)

# 4. Nest a Frame inside another Frame.
outer_frame = tk.Frame(root, bg="lightgreen")
outer_frame.pack(pady=10)
inner_frame = tk.Frame(outer_frame, bg="white", bd=2, relief="sunken")
inner_frame.pack(padx=10, pady=10)
tk.Label(inner_frame, text="Nested Frame").pack()

# 5. Set the background color and fixed size of a Frame.
frame5 = tk.Frame(root, bg="pink", width=200, height=100)
frame5.pack(pady=10)
frame5.pack_propagate(False)
tk.Label(frame5, text="Fixed Size Frame").pack()

# 6. Use pack_propagate(False) and test resizing behavior.
frame6 = tk.Frame(root, bg="orange", width=300, height=50)
frame6.pack(pady=10)
frame6.pack_propagate(False)
tk.Button(frame6, text="Resize Test").pack()

# 7. Create multiple frames (header, content, footer).
header = tk.Frame(root, bg="navy", height=50)
header.pack(fill="x")
content = tk.Frame(root, bg="white")
content.pack(expand=True, fill="both")
footer = tk.Frame(root, bg="gray", height=30)
footer.pack(fill="x")

# 8. Align multiple frames horizontally using pack(side="left").
frame8 = tk.Frame(root)
frame8.pack(pady=10)
tk.Frame(frame8, bg="red", width=100, height=100).pack(side="left", padx=5)
tk.Frame(frame8, bg="green", width=100, height=100).pack(side="left", padx=5)
tk.Frame(frame8, bg="blue", width=100, height=100).pack(side="left", padx=5)

# 9. Create a left sidebar Frame for navigation buttons.
sidebar = tk.Frame(root, bg="lightgray", width=150)
sidebar.pack(side="left", fill="y")
tk.Button(sidebar, text="Home").pack(fill="x")
tk.Button(sidebar, text="Settings").pack(fill="x")
tk.Button(sidebar, text="Logout").pack(fill="x")

# 10. Add form fields in one frame and result display in another.
form_frame = tk.Frame(root)
form_frame.pack(pady=10)
tk.Label(form_frame, text="Enter Age:").grid(row=0, column=0)
tk.Entry(form_frame).grid(row=0, column=1)

result_frame = tk.Frame(root, bg="lightyellow", width=200, height=50)
result_frame.pack(pady=10)
tk.Label(result_frame, text="Result will appear here").pack()

# 11. Combine pack() and grid() using different frames.
combo_frame = tk.Frame(root)
combo_frame.pack(pady=10)
tk.Label(combo_frame, text="Packed Label").pack()
inner_combo = tk.Frame(combo_frame)
inner_combo.pack()
tk.Label(inner_combo, text="Grid Label:").grid(row=0, column=0)
tk.Entry(inner_combo).grid(row=0, column=1)

# 12. Use Frame to create a login form layout.
login_frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
login_frame.pack(pady=10)
tk.Label(login_frame, text="Username:").grid(row=0, column=0)
tk.Entry(login_frame).grid(row=0, column=1)
tk.Label(login_frame, text="Password:").grid(row=1, column=0)
tk.Entry(login_frame, show="*").grid(row=1, column=1)
tk.Button(login_frame, text="Login").grid(row=2, columnspan=2)

# 13. Use Frame to group widgets by section (personal info vs contact info).
info_frame = tk.Frame(root)
info_frame.pack(pady=10)
personal = tk.LabelFrame(info_frame, text="Personal Info", padx=10, pady=10)
personal.pack(side="left", padx=10)
tk.Label(personal, text="First Name").pack()
tk.Entry(personal).pack()
tk.Label(personal, text="Last Name").pack()
tk.Entry(personal).pack()

contact = tk.LabelFrame(info_frame, text="Contact Info", padx=10, pady=10)
contact.pack(side="left", padx=10)
tk.Label(contact, text="Email").pack()
tk.Entry(contact).pack()
tk.Label(contact, text="Phone").pack()
tk.Entry(contact).pack()

# 14. Style a Frame with borders, padding, and relief.
styled_frame = tk.Frame(root, bg="white", bd=5, relief="ridge", padx=10, pady=10)
styled_frame.pack(pady=10)
tk.Label(styled_frame, text="Styled Frame").pack()

# 15. Place a Frame at a specific location using place().
placed_frame = tk.Frame(root, bg="purple", width=120, height=50)
placed_frame.place(x=600, y=500)
tk.Label(placed_frame, text="Placed Frame", fg="white", bg="purple").pack()

root.mainloop()
