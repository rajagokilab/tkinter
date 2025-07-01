import tkinter as tk

# Sample question and answer
question = "What is the capital of Sweden?"
correct_answer = "Stockholm"

def check_answer():
    user_answer = answer_entry.get().strip()
    if user_answer.lower() == correct_answer.lower():
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect. Try again.", fg="red")

root = tk.Tk()
root.title("Basic Quiz App")
root.geometry("400x200")

tk.Label(root, text="Question:", font=("Arial", 12)).pack(pady=(20, 5))
tk.Label(root, text=question, font=("Arial", 14)).pack()

tk.Label(root, text="Your Answer:").pack(pady=(10, 0))
answer_entry = tk.Entry(root, width=30)
answer_entry.pack()

submit_btn = tk.Button(root, text="Submit", command=check_answer)
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
