import tkinter as tk
from tkinter import messagebox
import random

# Sample news headlines and details database
NEWS_DATA = [
    ("Breaking: Market hits record high", "The stock market reached an all-time high today with major indexes..."),
    ("Sports: Local team wins championship", "In an exciting finale, the local team clinched the championship title..."),
    ("Weather: Storm warning issued", "Meteorologists have issued a severe storm warning for the area..."),
    ("Tech: New smartphone released", "The latest smartphone model features innovative technology and design..."),
    ("Health: Tips for a balanced diet", "Experts share tips to maintain a balanced and healthy diet..."),
    ("Politics: Election campaigns heating up", "Candidates are ramping up their campaigns ahead of the upcoming election..."),
    ("Travel: Top 10 destinations in 2025", "Here are the top travel destinations to visit in 2025 according to experts..."),
    ("Finance: How to save for retirement", "Financial advisors discuss strategies for effective retirement saving..."),
    ("Entertainment: Award show highlights", "Highlights from last night's major entertainment awards..."),
    ("Education: New online courses available", "Several new online courses are now available to boost your skills..."),
    ("Science: Breakthrough in renewable energy", "Scientists have developed a new method for efficient renewable energy..."),
    ("Local: Community garden project launched", "A new community garden project has been launched downtown..."),
    ("Business: Startup secures funding", "A local startup announced it has secured major funding from investors..."),
    ("Environment: Conservation efforts increase", "Efforts to conserve endangered species have increased significantly..."),
    ("Culture: Festival dates announced", "Dates for the annual cultural festival have been officially announced..."),
    ("Automotive: Electric car sales surge", "Sales of electric vehicles continue to surge worldwide..."),
    ("Fashion: Trends to watch this year", "Here are the fashion trends to watch this year..."),
    ("Real Estate: Housing market update", "An update on the housing market shows steady growth..."),
    ("Science: Mars rover sends new images", "The Mars rover has sent back stunning new images from the red planet..."),
    ("Tech: Cybersecurity threats rise", "Experts warn about the rise in cybersecurity threats globally..."),
    ("Health: Benefits of mindfulness", "Mindfulness practices have been linked to better mental health..."),
    ("Travel: Airline announces new routes", "A major airline has announced new international routes starting next month...")
]

class NewsReader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scrolling News Reader")
        self.geometry("500x350")

        # Frame for Listbox and scrollbar
        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Listbox with scrollbar
        self.listbox = tk.Listbox(frame, height=15)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.listbox.bind('<<ListboxSelect>>', self.show_details)

        scrollbar = tk.Scrollbar(frame, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Refresh button
        self.refresh_button = tk.Button(self, text="Refresh Headlines", command=self.refresh_headlines)
        self.refresh_button.pack(pady=5)

        # Load initial headlines
        self.headlines = []
        self.load_headlines()

        # Start auto-scroll ticker
        self.auto_scroll_delay = 2000  # milliseconds
        self.after(self.auto_scroll_delay, self.auto_scroll)

    def load_headlines(self):
        self.listbox.delete(0, tk.END)
        self.headlines = random.sample(NEWS_DATA, k=20)
        for title, _ in self.headlines:
            self.listbox.insert(tk.END, title)

    def show_details(self, event):
        if not self.listbox.curselection():
            return
        index = self.listbox.curselection()[0]
        title, details = self.headlines[index]
        messagebox.showinfo(title, details)

    def refresh_headlines(self):
        self.load_headlines()

    def auto_scroll(self):
        size = self.listbox.size()
        if size == 0:
            return
        current = self.listbox.curselection()
        if current:
            next_index = (current[0] + 1) % size
        else:
            next_index = 0
        self.listbox.selection_clear(0, tk.END)
        self.listbox.selection_set(next_index)
        self.listbox.see(next_index)
        # Schedule next scroll
        self.after(self.auto_scroll_delay, self.auto_scroll)

if __name__ == "__main__":
    app = NewsReader()
    app.mainloop()
