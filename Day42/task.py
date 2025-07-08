import tkinter as tk

def resize_canvas():
    try:
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())
        canvas.config(width=new_width, height=new_height)
    except ValueError:
        print("Enter valid integers for width and height.")

# Create the main window
root = tk.Tk()
root.title("Canvas Widget Tasks")
root.geometry("600x500")

# Create a canvas with custom width and height (Task 6)
canvas = tk.Canvas(root, width=500, height=400, bg="white")
canvas.pack(pady=10)

# Task 1: Draw a rectangle
canvas.create_rectangle(20, 20, 120, 70, fill="skyblue", outline="black")

# Task 2: Draw a circle (oval)
canvas.create_oval(140, 20, 200, 80, fill="lightgreen", outline="black")

# Task 3: Draw a line between two points
canvas.create_line(220, 20, 300, 80, fill="black", width=2)

# Task 4: Draw a polygon (triangle)
canvas.create_polygon(320, 80, 360, 20, 400, 80, fill="orange", outline="black")

# Task 5: Fill shapes with different colors (done above in 'fill')

# Task 7: Use create_text()
canvas.create_text(250, 120, text="Canvas Drawing Examples", font=("Arial", 14), fill="purple")

# Task 8: Draw multiple shapes (already done above)

# Task 9: Position shapes using variables
x, y = 100, 150
canvas.create_rectangle(x, y, x+50, y+30, fill="pink", outline="black")
canvas.create_oval(x+70, y, x+120, y+30, fill="lightyellow", outline="black")
canvas.create_line(x+140, y, x+200, y+30, fill="red", width=2)

# Task 10: Resize canvas dynamically using Entry and Button
frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Width:").pack(side=tk.LEFT)
width_entry = tk.Entry(frame, width=5)
width_entry.insert(0, "500")
width_entry.pack(side=tk.LEFT)

tk.Label(frame, text="Height:").pack(side=tk.LEFT)
height_entry = tk.Entry(frame, width=5)
height_entry.insert(0, "400")
height_entry.pack(side=tk.LEFT)

tk.Button(frame, text="Resize Canvas", command=resize_canvas).pack(side=tk.LEFT)

# Run the GUI loop
root.mainloop()
