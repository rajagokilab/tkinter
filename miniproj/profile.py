import tkinter as tk

def draw_profile_card():
    # Clear canvas first
    canvas.delete("all")

    name = entry_name.get().strip()
    age = entry_age.get().strip()
    email = entry_email.get().strip()

    # Draw card background
    canvas.create_rectangle(10, 10, 390, 190, fill="#DDEEFF", outline="#3399FF", width=3, roundness=25)

    # Draw a circle as avatar placeholder
    canvas.create_oval(20, 20, 120, 120, fill="#5577AA")

    # Display user info text
    canvas.create_text(150, 40, anchor='w', text=f"Name: {name}", font=("Arial", 16, "bold"))
    canvas.create_text(150, 80, anchor='w', text=f"Age: {age}", font=("Arial", 14))
    canvas.create_text(150, 120, anchor='w', text=f"Email: {email}", font=("Arial", 14))

root = tk.Tk()
root.title("User Profile Card Generator")

# Input frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
entry_name = tk.Entry(input_frame, width=25)
entry_name.grid(row=0, column=1, padx=5, pady=5)
entry_name.insert(0, "John Doe")

tk.Label(input_frame, text="Age:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
entry_age = tk.Entry(input_frame, width=25)
entry_age.grid(row=1, column=1, padx=5, pady=5)
entry_age.insert(0, "30")

tk.Label(input_frame, text="Email:").grid(row=2, column=0, sticky='e', padx=5, pady=5)
entry_email = tk.Entry(input_frame, width=25)
entry_email.grid(row=2, column=1, padx=5, pady=5)
entry_email.insert(0, "john@example.com")

# Button to generate profile card
generate_btn = tk.Button(root, text="Generate Profile Card", command=draw_profile_card)
generate_btn.pack(pady=10)

# Canvas to draw the profile card
canvas = tk.Canvas(root, width=400, height=200, bg="white")
canvas.pack(pady=10)

root.mainloop()
