import tkinter as tk

root = tk.Tk()
root.title("Responsive Layout Demo")
root.geometry("900x300")

# Left Frame - pack()
frame_pack = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame_pack.pack(side="left", fill="both", expand=True, padx=5, pady=5)

tk.Label(frame_pack, text="pack() Layout", font=("Arial", 14, "bold")).pack(pady=5)

btn1 = tk.Button(frame_pack, text="Button 1")
btn2 = tk.Button(frame_pack, text="Button 2")
btn3 = tk.Button(frame_pack, text="Button 3")

btn1.pack(fill="x", pady=5)
btn2.pack(fill="x", pady=5)
btn3.pack(fill="x", pady=5)

# Middle Frame - grid()
frame_grid = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame_grid.pack(side="left", fill="both", expand=True, padx=5, pady=5)

tk.Label(frame_grid, text="grid() Layout", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=5)

tk.Label(frame_grid, text="Name:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
tk.Entry(frame_grid).grid(row=1, column=1, sticky="we", pady=5, padx=5)

tk.Label(frame_grid, text="Email:").grid(row=2, column=0, sticky="e", pady=5, padx=5)
tk.Entry(frame_grid).grid(row=2, column=1, sticky="we", pady=5, padx=5)

tk.Label(frame_grid, text="Age:").grid(row=3, column=0, sticky="e", pady=5, padx=5)
tk.Entry(frame_grid).grid(row=3, column=1, sticky="we", pady=5, padx=5)

frame_grid.columnconfigure(1, weight=1)

# Right Frame - place()
frame_place = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10)
frame_place.pack(side="left", fill="both", expand=True, padx=5, pady=5)

tk.Label(frame_place, text="place() Layout", font=("Arial", 14, "bold")).place(x=10, y=10)

btn_a = tk.Button(frame_place, text="Button A")
btn_b = tk.Button(frame_place, text="Button B")
entry = tk.Entry(frame_place)

btn_a.place(x=20, y=50, width=100, height=30)
btn_b.place(x=130, y=50, width=100, height=30)
entry.place(x=20, y=100, width=210, height=25)

root.mainloop()
