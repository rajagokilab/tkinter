import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Tkinter PanedWindow Examples")
root.geometry("1000x700")

# 16. Create a horizontal PanedWindow with two frames.
paned1 = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief="raised", bg="gray")
paned1.pack(fill="x", pady=5)

left_frame1 = tk.Frame(paned1, width=200, height=100, bg="lightblue")
right_frame1 = tk.Frame(paned1, width=200, height=100, bg="lightgreen")

paned1.add(left_frame1)
paned1.add(right_frame1)

# 17. Create a vertical PanedWindow with a text area and a form.
paned2 = tk.PanedWindow(root, orient=tk.VERTICAL, sashrelief="raised")
paned2.pack(fill="both", expand=True, pady=5)

text_area = tk.Text(paned2, height=5)
form_frame = tk.Frame(paned2, bg="white", height=100)
tk.Label(form_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(form_frame).grid(row=0, column=1, padx=5, pady=5)

paned2.add(text_area)
paned2.add(form_frame)

# 18. Add a Label on each side of the PanedWindow.
paned3 = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief="raised")
paned3.pack(fill="x", pady=5)

paned3.add(tk.Label(paned3, text="Left Label", bg="orange", width=20))
paned3.add(tk.Label(paned3, text="Right Label", bg="yellow", width=20))

# 19. Embed a scrollable Text widget inside one PanedWindow pane.
paned4 = tk.PanedWindow(root, sashrelief="raised")
paned4.pack(fill="both", expand=True, pady=5)

text_frame = tk.Frame(paned4)
scrollbar = tk.Scrollbar(text_frame)
scroll_text = tk.Text(text_frame, yscrollcommand=scrollbar.set, wrap="word")
scrollbar.config(command=scroll_text.yview)
scrollbar.pack(side="right", fill="y")
scroll_text.pack(side="left", fill="both", expand=True)
paned4.add(text_frame)

paned4.add(tk.Label(paned4, text="Another Pane", bg="lightgray", width=25))

# 20. Allow user to resize a drawing area (Canvas) using PanedWindow.
paned5 = tk.PanedWindow(root, sashrelief="raised")
paned5.pack(fill="both", expand=True, pady=5)

canvas = tk.Canvas(paned5, bg="white", width=300, height=200)
paned5.add(canvas)
paned5.add(tk.Label(paned5, text="Side Info", bg="lightyellow"))

# 21. Split the window into 3 resizable panes using nested PanedWindows.
outer_paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief="raised")
outer_paned.pack(fill="both", expand=True, pady=5)

left = tk.Label(outer_paned, text="Left", bg="lightgray", width=20)
middle_paned = tk.PanedWindow(outer_paned, orient=tk.VERTICAL)

middle_top = tk.Label(middle_paned, text="Middle Top", bg="lightblue")
middle_bottom = tk.Label(middle_paned, text="Middle Bottom", bg="lightgreen")

middle_paned.add(middle_top)
middle_paned.add(middle_bottom)

right = tk.Label(outer_paned, text="Right", bg="lightpink", width=20)

outer_paned.add(left)
outer_paned.add(middle_paned)
outer_paned.add(right)

# 22. Add a resizable file explorer pane on the left.
explorer_paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief="raised")
explorer_paned.pack(fill="both", expand=True, pady=5)

file_explorer = tk.Listbox(explorer_paned)
for item in ["File1.txt", "File2.docx", "Image.png", "Script.py"]:
    file_explorer.insert("end", item)

main_view = tk.Label(explorer_paned, text="Main View Area", bg="white")

explorer_paned.add(file_explorer, minsize=150)
explorer_paned.add(main_view)

# 23. Use different background colors in each pane.
color_paned = tk.PanedWindow(root, orient=tk.HORIZONTAL)
color_paned.pack(fill="x", pady=5)
color_paned.add(tk.Frame(color_paned, bg="red", width=100, height=50))
color_paned.add(tk.Frame(color_paned, bg="blue", width=100, height=50))
color_paned.add(tk.Frame(color_paned, bg="green", width=100, height=50))

# 24. Add widgets like Entry, Listbox, or Canvas to different panes.
widget_paned = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief="raised")
widget_paned.pack(fill="x", pady=5)
widget_paned.add(tk.Entry(widget_paned))
widget_paned.add(tk.Listbox(widget_paned, height=3))
widget_paned.add(tk.Canvas(widget_paned, bg="lightgray", width=100, height=30))

# 25. Combine Frame and PanedWindow to build a 3-column layout.
layout_frame = tk.Frame(root)
layout_frame.pack(fill="both", expand=True, pady=5)

layout_paned = tk.PanedWindow(layout_frame, orient=tk.HORIZONTAL, sashrelief="raised")
layout_paned.pack(fill="both", expand=True)

left_col = tk.Frame(layout_paned, bg="gray90", width=150)
center_col = tk.Frame(layout_paned, bg="white", width=500)
right_col = tk.Frame(layout_paned, bg="gray95", width=150)

tk.Label(left_col, text="Sidebar").pack(pady=10)
tk.Label(center_col, text="Main Content").pack(pady=10)
tk.Label(right_col, text="Tools").pack(pady=10)

layout_paned.add(left_col)
layout_paned.add(center_col)
layout_paned.add(right_col)

root.mainloop()
