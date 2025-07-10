import tkinter as tk

def draw_profile_card():
    name = name_entry.get().strip()
    age = age_entry.get().strip()
    email = email_entry.get().strip()

    if not name or not age or not email:
        return

    # Clear canvas
    canvas.delete("all")

    # Draw profile card background (rounded rectangle style)
    x0, y0, x1, y1 = 30, 30, 370, 200
    canvas.create_rectangle(x0, y0, x1, y1, fill="#DDEEFF", outline="#3366AA", width=2)

    # Draw text
    canvas.create_text(200, 60, text=f"Name: {name}", font=("Arial", 14, "bold"))
    canvas.create_text(200, 100, text=f"Age: {age}", font=("Arial", 12))
    canvas.create_text(200, 140, text=f"Email: {email}", font=("Arial", 12))

# ==== Main Window ====
root = tk.Tk()
root.title("User Profile Card Generator")
root.geometry("420x400")
root.configure(padx=10, pady=10)

# ==== Input Frame ====
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:").pack(anchor="w")
name_entry = tk.Entry(input_frame, width=40)
name_entry.pack()

tk.Label(input_frame, text="Age:").pack(anchor="w", pady=(10, 0))
age_entry = tk.Entry(input_frame, width=40)
age_entry.pack()

tk.Label(input_frame, text="Email:").pack(anchor="w", pady=(10, 0))
email_entry = tk.Entry(input_frame, width=40)
email_entry.pack()

tk.Button(root, text="Generate Profile Card", command=draw_profile_card).pack(pady=10)

# ==== Canvas for Profile Card ====
canvas = tk.Canvas(root, width=400, height=240, bg="white", bd=2, relief="ridge")
canvas.pack()

root.mainloop()
