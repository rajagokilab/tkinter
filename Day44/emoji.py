import tkinter as tk

class EmojiReactionPanel(tk.Frame):
    def __init__(self, master, emojis=None, **kwargs):
        super().__init__(master, **kwargs)
        self.emojis = emojis or ["😀", "😢", "😠", "😍", "👍", "👎"]
        self.selected_emoji = tk.StringVar(value="No reaction yet")

        # Label to show selected emoji
        self.label = tk.Label(self, textvariable=self.selected_emoji, font=("Arial", 14))
        self.label.pack(side="bottom", pady=5)

        # Frame for emoji buttons
        btn_frame = tk.Frame(self)
        btn_frame.pack()

        for emj in self.emojis:
            btn = tk.Button(btn_frame, text=emj, font=("Arial", 20), bd=0,
                            command=lambda e=emj: self.react(e))
            btn.pack(side="left", padx=5)

    def react(self, emoji):
        self.selected_emoji.set(f"Reaction: {emoji}")
        print(f"Emoji clicked: {emoji}")

# Example usage with multiple instances
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300")
    root.title("Emoji Reaction Panel Demo")

    tk.Label(root, text="Message 1: Hello world!").pack(pady=(10,0))
    panel1 = EmojiReactionPanel(root)
    panel1.pack(pady=5)

    tk.Label(root, text="Message 2: Tkinter is fun!").pack(pady=(20,0))
    panel2 = EmojiReactionPanel(root)
    panel2.pack(pady=5)

    root.mainloop()
