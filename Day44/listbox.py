import tkinter as tk

def on_key_press(event):
    selection = listbox.curselection()
    if not selection:
        index = 0
    else:
        index = selection[0]

    if event.keysym == "Up":
        if index > 0:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(index - 1)
            listbox.activate(index - 1)
    elif event.keysym == "Down":
        if index < listbox.size() - 1:
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(index + 1)
            listbox.activate(index + 1)
    elif event.keysym == "Return":
        if listbox.curselection():
            selected = listbox.get(listbox.curselection())
            selected_label.config(text=f"Selected: {selected}")

root = tk.Tk()
root.title("Listbox Navigator")

items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

listbox = tk.Listbox(root, height=7)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(padx=20, pady=10)

selected_label = tk.Label(root, text="Selected: None")
selected_label.pack(pady=(0,10))

listbox.bind("<Up>", on_key_press)
listbox.bind("<Down>", on_key_press)
listbox.bind("<Return>", on_key_press)

listbox.focus_set()

root.mainloop()
