import tkinter as tk
from tkinter import messagebox

class ChatUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Chat Application")
        self.root.geometry("600x400")

        self.create_menu()
        self.create_toolbar()
        self.create_chat_frames()

    def create_menu(self):
        menubar = tk.Menu(self.root)
        chat_menu = tk.Menu(menubar, tearoff=0)
        chat_menu.add_command(label="Clear", command=self.clear_chat)
        chat_menu.add_separator()
        chat_menu.add_command(label="Exit", command=self.root.quit)
        menubar.add_cascade(label="Chat", menu=chat_menu)
        self.root.config(menu=menubar)

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        connect_btn = tk.Button(toolbar, text="Connect", command=self.connect)
        connect_btn.pack(side="left", padx=5, pady=5)

        disconnect_btn = tk.Button(toolbar, text="Disconnect", command=self.disconnect)
        disconnect_btn.pack(side="left", padx=5, pady=5)

    def create_chat_frames(self):
        # Top frame: chat window (Text)
        top_frame = tk.Frame(self.root)
        top_frame.pack(fill="both", expand=True)

        self.chat_text = tk.Text(top_frame, state="disabled", bg="white")
        self.chat_text.pack(fill="both", expand=True, padx=5, pady=5)

        # Bottom frame: entry + send button
        bottom_frame = tk.Frame(self.root, bd=2, relief=tk.GROOVE)
        bottom_frame.pack(fill="x")

        self.entry = tk.Entry(bottom_frame)
        self.entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
        self.entry.bind("<Return>", self.send_message)

        send_btn = tk.Button(bottom_frame, text="Send", command=self.send_message)
        send_btn.pack(side="right", padx=5, pady=5)

    def connect(self):
        self.log("Connected to chat.")

    def disconnect(self):
        self.log("Disconnected from chat.")

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if msg:
            self.log(f"You: {msg}")
            self.entry.delete(0, tk.END)

    def log(self, message):
        self.chat_text.config(state="normal")
        self.chat_text.insert(tk.END, message + "\n")
        self.chat_text.see(tk.END)
        self.chat_text.config(state="disabled")

    def clear_chat(self):
        if messagebox.askokcancel("Clear Chat", "Are you sure you want to clear the chat?"):
            self.chat_text.config(state="normal")
            self.chat_text.delete(1.0, tk.END)
            self.chat_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatUI(root)
    root.mainloop()
