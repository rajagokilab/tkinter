import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime

def task1():
    # Text widget + button to save content to a file
    def save_content():
        content = text.get("1.0", tk.END)
        with open("notes.txt", "w") as f:
            f.write(content)
        messagebox.showinfo("Saved", "Content saved to notes.txt")
    
    root = tk.Tk()
    root.title("Task 1: Save Text Content")
    text = tk.Text(root, width=40, height=10)
    text.pack(padx=10, pady=10)
    btn_save = tk.Button(root, text="Save to File", command=save_content)
    btn_save.pack(pady=5)
    root.mainloop()

def task2():
    # Insert sample paragraph into Text widget
    root = tk.Tk()
    root.title("Task 2: Insert Sample Text")
    text = tk.Text(root, width=50, height=10)
    text.pack(padx=10, pady=10)
    sample_paragraph = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                        "Vestibulum ac varius sapien. Pellentesque habitant morbi tristique senectus et netus.")
    text.insert("1.0", sample_paragraph)
    root.mainloop()

def task3():
    # Use get() to print entire Text widget content
    def print_content():
        content = text.get("1.0", tk.END)
        print("Content in Text widget:\n", content)
    
    root = tk.Tk()
    root.title("Task 3: Get Text Content")
    text = tk.Text(root, width=40, height=10)
    text.pack(padx=10, pady=10)
    btn_print = tk.Button(root, text="Print Content to Console", command=print_content)
    btn_print.pack(pady=5)
    root.mainloop()

def task4():
    # Clear Text content on button click using delete()
    def clear_text():
        text.delete("1.0", tk.END)
    
    root = tk.Tk()
    root.title("Task 4: Clear Text Content")
    text = tk.Text(root, width=40, height=10)
    text.pack(padx=10, pady=10)
    btn_clear = tk.Button(root, text="Clear Text", command=clear_text)
    btn_clear.pack(pady=5)
    root.mainloop()

def task5():
    # Display number of characters and words typed in Text widget
    def update_counts(event=None):
        content = text.get("1.0", tk.END).strip()
        chars = len(content)
        words = len(content.split()) if content else 0
        label.config(text=f"Characters: {chars}  Words: {words}")
    
    root = tk.Tk()
    root.title("Task 5: Count Chars and Words")
    text = tk.Text(root, width=50, height=10)
    text.pack(padx=10, pady=10)
    label = tk.Label(root, text="Characters: 0  Words: 0")
    label.pack()
    text.bind("<KeyRelease>", update_counts)
    root.mainloop()

def task6():
    # Add scrollbar to Text widget
    root = tk.Tk()
    root.title("Task 6: Text with Scrollbar")
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text = tk.Text(frame, width=50, height=10, yscrollcommand=scrollbar.set)
    text.pack()
    scrollbar.config(command=text.yview)
    root.mainloop()

def task7():
    # Auto-save Text content every 5 seconds using after()
    def auto_save():
        content = text.get("1.0", tk.END)
        with open("autosave.txt", "w") as f:
            f.write(content)
        label.config(text="Auto-saved at " + datetime.now().strftime("%H:%M:%S"))
        root.after(5000, auto_save)  # repeat every 5 seconds
    
    root = tk.Tk()
    root.title("Task 7: Auto-Save Text Content")
    text = tk.Text(root, width=50, height=10)
    text.pack(padx=10, pady=10)
    label = tk.Label(root, text="Auto-save status")
    label.pack()
    auto_save()  # start auto-save loop
    root.mainloop()

def task8():
    # Highlight specific keywords using tags
    def highlight_keywords():
        keywords = ["Python", "Tkinter", "widget"]
        content = text.get("1.0", tk.END).lower()
        for kw in keywords:
            start = "1.0"
            while True:
                pos = text.search(kw.lower(), start, tk.END)
                if not pos:
                    break
                end = f"{pos}+{len(kw)}c"
                text.tag_add("highlight", pos, end)
                start = end
        text.tag_config("highlight", foreground="red", background="yellow")
    
    root = tk.Tk()
    root.title("Task 8: Highlight Keywords")
    text = tk.Text(root, width=60, height=10)
    text.pack(padx=10, pady=10)
    sample_text = "This is a Python Tkinter widget example. Tkinter widgets are easy to use."
    text.insert("1.0", sample_text)
    tk.Button(root, text="Highlight Keywords", command=highlight_keywords).pack(pady=5)
    root.mainloop()

def task9():
    # Load text from a file and display it in Text widget
    def load_file():
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filepath:
            with open(filepath, "r") as file:
                content = file.read()
            text.delete("1.0", tk.END)
            text.insert("1.0", content)
    
    root = tk.Tk()
    root.title("Task 9: Load Text from File")
    text = tk.Text(root, width=50, height=15)
    text.pack(padx=10, pady=10)
    btn_load = tk.Button(root, text="Load Text File", command=load_file)
    btn_load.pack(pady=5)
    root.mainloop()

def task10():
    # Mini diary app: Text widget input + date-based saving
    def save_diary():
        content = text.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Empty Entry", "Please write something before saving.")
            return
        filename = datetime.now().strftime("diary_%Y-%m-%d.txt")
        with open(filename, "a") as f:
            f.write(datetime.now().strftime("%H:%M:%S") + "\n")
            f.write(content + "\n\n")
        label.config(text=f"Diary saved to {filename}")
        text.delete("1.0", tk.END)
    
    root = tk.Tk()
    root.title("Task 10: Mini Diary App")
    text = tk.Text(root, width=50, height=15)
    text.pack(padx=10, pady=10)
    btn_save = tk.Button(root, text="Save Diary Entry", command=save_diary)
    btn_save.pack(pady=5)
    label = tk.Label(root, text="")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    # Uncomment to run specific task:
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    # task7()
    # task8()
    # task9()
    task10()
    print("Uncomment a task() call at the bottom to run a demo.")
