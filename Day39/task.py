import tkinter as tk

# 1. **Check Tkinter Installation:**  Write a Python script to import Tkinter and confirm it’s installed without errors.
# import tkinter as tk
# root = tk.Tk()
# root.mainloop()

# 2. **Create a Basic Window:**  Create a Tkinter window with a title and a specific size.
# import tkinter as tk
# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("500x500")
# root.mainloop()

# 3.**Change Window Title:**   Modify your window’s title to something different.
# import tkinter as tk
# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("500x500")
# root.mainloop()

# 4. **Resize the Window:**  Adjust the window size using `.geometry()`.
# import tkinter as tk
# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("1000x500")
# root.mainloop()

# 5. **Add a Label Widget:**   Place a label widget in the window that displays “Welcome to Tkinter!”.
# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("1000x500")
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14), fg="green")
# label.pack()
# root.mainloop()

# 6. **Add an Entry Widget:**  Add a single-line text entry box beneath your label.
# root = tk.Tk()
# root.title("My First GUI")
# root.geometry("1000x500")
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14), fg="green")
# label.pack()
# entry = tk.Entry(root)
# entry.pack()
# entry.insert(0, "")
# root.mainloop()

# 7. **Add a Button Widget:**  Add a button that does nothing when clicked (for now).
# root = tk.Tk()
# root.geometry("1000x500")
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14), fg="green")
# label.pack()
# entry = tk.Entry(root)
# entry.pack()
# entry.insert(0, "")
# def update_label():
#     text = entry.get()           # Task 8
#     label.config(text=text)      # Task 9
# btn = tk.Button(root, text="Update Label", command=update_label)
# btn.pack()
# root.mainloop()

# Create a Multi-line Text Widget: Add a Text widget to your window for multi-line input.
# root = tk.Tk()
# root.geometry("1000x500")
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14), fg="green")
# label.pack()
# entry = tk.Entry(root)
# entry.pack()
# entry.insert(0, "")
# def update_label():
#     text = entry.get()      
#     label.config(text=text)      
# btn = tk.Button(root, text="Update Label", command=update_label)
# btn.pack()
# text_widget = tk.Text(root, height=5, width=40)
# text_widget.pack()
# root.mainloop()


# 11.Read from Text Widget:
# root = tk.Tk()
# root.geometry("1000x500")
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14), fg="green")
# label.pack()
# entry = tk.Entry(root)
# entry.pack()
# entry.insert(0, "")
# def update_label():
#     text = entry.get()      
#     label.config(text=text)      
# btn = tk.Button(root, text="Update Label", command=update_label)
# btn.pack()
# text_widget = tk.Text(root, height=5, width=40)
# text_widget.pack()
# def read_text():
#     print(text_widget.get("1.0", tk.END).strip())
# btn_read = tk.Button(root, text="Read Text", command=read_text)
# btn_read.pack()
# root.mainloop()

# 12Experiment with pack():
# root = tk.Tk()
# root.title("pack() Vertical Layout")
# root.geometry("300x200")
# # First widget: Label
# label = tk.Label(root, text="This is a Label", bg="lightblue")
# label.pack(pady=50)
# # Second widget: Entry
# entry = tk.Entry(root)
# entry.pack(pady=5)
# # Third widget: Button
# button = tk.Button(root, text="Click Me")
# button.pack(pady=5)
# root.mainloop()

# Experiment with grid():Arrange a label and an entry widget side by side using grid()
# root = tk.Tk()
# root.title("grid() Side by Side")
# root.geometry("300x100")
# # Label in row 0, column 0
# label = tk.Label(root, text="Name:")
# label.grid(row=0, column=0, padx=10, pady=10)
# # Entry in row 0, column 1
# entry = tk.Entry(root)
# entry.grid(row=0, column=1, padx=10, pady=10)
# root.mainloop()


# 14Experiment with place():

# root = tk.Tk()
# root.title("place() Example")
# root.geometry("300x200")
# # Button positioned at (100, 50)
# button = tk.Button(root, text="Button!")
# button.place(x=100, y=50)

# root.mainloop()


# 15Mix Layout Managers (pack and grid):
# import tkinter as tk

# root = tk.Tk()
# root.title("Mixing pack() and grid()")
# root.geometry("300x200")
# # Frame using pack()
# top_frame = tk.Frame(root)
# top_frame.pack()

# label = tk.Label(top_frame, text="Label in top_frame (pack)")
# label.pack()
# bottom_frame = tk.Frame(root)
# bottom_frame.pack()
# # Frame using grid()
# entry = tk.Entry(bottom_frame)
# entry.grid(row=0, column=1)

# btn = tk.Button(bottom_frame, text="Button next to Entry")
# btn.grid(row=0, column=2)

# root.mainloop()

# 16Create a Frame Widget:Add a frame to your main window.
# root = tk.Tk()
# root.title("Frame Example")
# root.geometry("300x200")
# # Create a Frame and add it to the root window
# frame = tk.Frame(root, bg="lightgray", borderwidth=2, relief="solid")
# frame.pack(padx=20, pady=20, fill="both", expand=True)
# # Add a label inside the frame (optional)
# label = tk.Label(frame, text="Welcome")
# label.pack(pady=10)
# root.mainloop()

# 17Add Widgets to Frame:Place at least two widgets inside the frame.
# root = tk.Tk()
# root.title("Widgets Inside Frame")
# root.geometry("300x200")
# # Create a frame inside the main window
# frame = tk.Frame(root, bg="lightblue", borderwidth=2, relief="groove")
# frame.pack(padx=20, pady=20, fill="both", expand=True)
# # Add a Label inside the frame
# label = tk.Label(frame, text="Enter your name:")
# label.pack(pady=5)
# # Add an Entry inside the frame
# entry = tk.Entry(frame)
# entry.pack(pady=5)

# root.mainloop()¨


# 18Multiple Frames:Create two frames and add different widgets to each.
# root = tk.Tk()
# root.title("Multiple Frames Example")
# root.geometry("400x250")
# # -------- Frame 1 --------
# frame1 = tk.Frame(root, bg="lightgray", borderwidth=2, relief="ridge")
# frame1.pack(padx=10, pady=10, fill="x")
# label1 = tk.Label(frame1, text="Frame 1: Name")
# label1.pack(side="left", padx=5, pady=5)
# entry1 = tk.Entry(frame1)
# entry1.pack(side="left", padx=5, pady=5)
# # -------- Frame 2 --------
# frame2 = tk.Frame(root, bg="lightblue", borderwidth=2, relief="groove")
# frame2.pack(padx=10, pady=10, fill="x")

# label2 = tk.Label(frame2, text="Frame 2: Age")
# label2.pack(side="left", padx=5, pady=5)

# entry2 = tk.Entry(frame2)
# entry2.pack(side="left", padx=5, pady=5)



# root.mainloop()

# 19Label Font and Color:Change the font size and foreground color of a label.
# from tkinter import font

# root = tk.Tk()
# root.title("Label Font and Color")
# root.geometry("300x150")

# # Create a custom font (optional, or use a tuple directly)
# custom_font = ("Helvetica", 16, "bold")  # (family, size, style)

# # Create a label with custom font and color
# label = tk.Label(root, text="Labelfont and color!", font=custom_font, fg="blue")
# label.pack(pady=20)

# root.mainloop()

# 20Button Command:Make the button print a message to the console when clicked.
# root = tk.Tk()
# root.title("Button Command Example")
# root.geometry("250x120")
# def say_hello():
#     print("Hello from the button!")
# btn = tk.Button(root, text="Click Me", command=say_hello)
# btn.pack(pady=20)
# root.mainloop()

# 21Disable/Enable Button:Add a checkbox that enables or disables the button.

# root = tk.Tk()
# root.title("Enable/Disable Button")
# root.geometry("300x150")
# def say_hello():
#     print("Hello from the button!")

# # Create the button (starts enabled)
# btn = tk.Button(root, text="Click Me", command=say_hello)
# btn.pack(pady=10)
# # Variable linked to the checkbox
# toggle_var = tk.IntVar(value=1)  # 1 = enabled by default
# # Function to enable/disable the button
# def toggle_button():
#     if toggle_var.get():
#         btn.config(state="normal")
#     else:
#         btn.config(state="disabled")
#         # Checkbox to control the button state
# checkbox = tk.Checkbutton(root, text="Enable Button", variable=toggle_var, command=toggle_button)
# checkbox.pack()
# root.mainloop()

# 22.Set Default Entry Text:Pre-fill the entry widget with default text.

# root = tk.Tk()
# root.title("Default Entry Text")
# root.geometry("300x100")
# entry = tk.Entry(root, width=30)
# entry.pack(pady=20)

# # Set default text
# entry.insert(0, "Enter your name here")

# root.mainloop()

# 23Clear Entry/Text Widget:Add a button that clears the entry or text widget contents.

# root = tk.Tk()
# root.title("Clear Entry and Text")
# root.geometry("350x250")
# # Entry widget
# entry = tk.Entry(root, width=40)
# entry.pack(pady=10)
# entry.insert(0, "Some default text")
# # Text widget
# text_widget = tk.Text(root, height=5, width=40)
# text_widget.pack(pady=10)
# text_widget.insert("1.0", "Some multiline\ntext content")
# # Clear function
# def clear_widgets():
#     entry.delete(0, tk.END)          # Clear Entry
#     text_widget.delete("1.0", tk.END)  # Clear Text
#     # Button to clear both
# clear_btn = tk.Button(root, text="Clear Entry and Text", command=clear_widgets)
# clear_btn.pack(pady=10)


# root.mainloop()

# 24Window Icon:Change the window icon (if on a supported OS).
# from PIL import Image

# img = Image.new('RGBA', (32, 32), (255, 0, 0, 255))  # Red 32x32 image
# img.save(r"F:\VTS\Rajagokila Python\PYTHON FULLSTACK DEVELOPER\TKINTER\Day39\icon.png")
# print("Icon created!")


# root = tk.Tk()
# icon = tk.PhotoImage(file=r"F:\VTS\Rajagokila Python\PYTHON FULLSTACK DEVELOPER\TKINTER\Day39\icon.png")
# root.iconphoto(True, icon)
# root.mainloop()

# 25Window Resizability:Set the window to be non-resizable.

# root = tk.Tk()
# root.title("Non-Resizable Window")
# root.geometry("300x200")

# # Disable resizing (both horizontal and vertical)
# root.resizable(False, False)

# root.mainloop()

# 26Custom Window Size on Startup:Start the window maximized or minimized.


# root = tk.Tk()
# root.title("Maximized Window")

# # Maximize window on startup
# root.state('zoomed')  # Works on Windows

# root.mainloop()

# 27Label with Image:Add an image to a label widget.

# from PIL import Image, ImageTk

# root = tk.Tk()
# root.title("Label with Image")

# # Load the JPEG image using PIL
# pil_image = Image.open(r"F:\VTS\Rajagokila Python\PYTHON FULLSTACK DEVELOPER\TKINTER\Day39\download.jpeg")
# img = ImageTk.PhotoImage(pil_image)

# # Create label with image and pack it
# label = tk.Label(root, image=img)
# label.pack()

# root.mainloop()

# 28
# def only_numbers(char):
#     # char is the text being inserted, return True if it's digit or empty (for deletion)
#     return char.isdigit() or char == ""

# root = tk.Tk()
# root.title("Entry Validation - Numbers Only")

# vcmd = (root.register(only_numbers), '%S')  # %S passes the inserted character

# entry = tk.Entry(root, validate='key', validatecommand=vcmd)
# entry.pack(padx=20, pady=20)

# root.mainloop()

# 29Button with Keyboard Shortcut:Bind a keyboard shortcut (e.g., Enter) to the button click event.

# def on_button_click():
#     print("Button clicked or Enter pressed!")

# root = tk.Tk()
# root.title("Button with Keyboard Shortcut")

# btn = tk.Button(root, text="Click Me", command=on_button_click)
# btn.pack(pady=20)

# # Bind the Enter key to call the button's command function
# root.bind('<Return>', lambda event: on_button_click())

# root.mainloop()

# 30Text Widget Scrollbar:Attach a vertical scrollbar to the Text widget.
# import tkinter as tk

# root = tk.Tk()
# root.title("Text Widget with Scrollbar")

# # Create a Text widget
# text_widget = tk.Text(root, width=40, height=10)
# text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# # Create a vertical Scrollbar and link it to the Text widget
# scrollbar = tk.Scrollbar(root, command=text_widget.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# # Configure the Text widget to update the scrollbar
# text_widget.config(yscrollcommand=scrollbar.set)

# root.mainloop()

# 31Frame Border and Relief:Add a border and a relief style (e.g., sunken) to a frame.


# import tkinter as tk

# root = tk.Tk()
# root.title("Frame with Border and Relief")

# frame = tk.Frame(root, bd=5, relief='sunken', width=200, height=100)
# frame.pack(padx=20, pady=20)

# # Optional: Add a label inside to visualize the frame
# label = tk.Label(frame, text="Inside the frame")
# label.pack(pady=20)

# root.mainloop()


# 32Pack Side Option:Use pack(side=LEFT) and pack(side=RIGHT) to see the effect.
# import tkinter as tk

# root = tk.Tk()
# root.title("Pack Side Option")

# # Button packed on the left side
# btn_left = tk.Button(root, text="Left Side")
# btn_left.pack(side=tk.LEFT, padx=10, pady=10)

# # Button packed on the right side
# btn_right = tk.Button(root, text="Right Side")
# btn_right.pack(side=tk.RIGHT, padx=10, pady=10)

# root.mainloop()

# 33Grid Row/Column Span:Make a widget span multiple columns or rows using grid().
# import tkinter as tk

# root = tk.Tk()
# root.title("Grid Row/Column Span")

# # Label spanning 2 columns
# label = tk.Label(root, text="This label spans 2 columns", bg="lightblue")
# label.grid(row=0, column=0, columnspan=2, sticky="we", padx=5, pady=5)

# # Button spanning 2 rows
# button = tk.Button(root, text="Button spans 2 rows", bg="lightgreen")
# button.grid(row=1, column=2, rowspan=2, sticky="ns", padx=5, pady=5)

# # Other widgets for comparison
# tk.Label(root, text="R1C2").grid(row=1, column=0)
# tk.Label(root, text="R2C0").grid(row=2, column=0)
# tk.Label(root, text="R2C1").grid(row=2, column=1)

# root.mainloop()

# 34Closing the Window:Add a button that closes the window when clicked using root.destroy().

root = tk.Tk()
root.title("Close Window Example")

def close_window():
    root.destroy()

close_btn = tk.Button(root, text="Close Window", command=close_window)
close_btn.pack(pady=20)

root.mainloop()
