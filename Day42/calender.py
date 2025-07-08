import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class CalendarPickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interactive Calendar Picker")

        # Current date
        self.today = datetime.today()

        # Month names
        self.month_names = list(calendar.month_name)[1:]  # Jan-Dec

        # Widgets: Month combobox, Year spinbox
        control_frame = ttk.Frame(root)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="Month:").grid(row=0, column=0)
        self.month_var = tk.StringVar(value=self.month_names[self.today.month - 1])
        self.month_cb = ttk.Combobox(control_frame, textvariable=self.month_var, values=self.month_names, state="readonly", width=10)
        self.month_cb.grid(row=0, column=1, padx=5)
        self.month_cb.bind("<<ComboboxSelected>>", self.draw_calendar)

        ttk.Label(control_frame, text="Year:").grid(row=0, column=2)
        self.year_var = tk.IntVar(value=self.today.year)
        self.year_spin = ttk.Spinbox(control_frame, from_=1900, to=2100, textvariable=self.year_var, width=6, command=self.draw_calendar)
        self.year_spin.grid(row=0, column=3, padx=5)

        # Canvas for calendar (7 columns x 6 rows)
        self.cell_width = 50
        self.cell_height = 40
        self.cols = 7
        self.rows = 6
        canvas_width = self.cell_width * self.cols
        canvas_height = self.cell_height * self.rows
        self.canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
        self.canvas.pack(pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        # Label for date info
        self.info_label = ttk.Label(root, text="Select a date")
        self.info_label.pack(pady=5)

        # Dictionary to keep date rectangle coordinates for click detection
        self.date_positions = {}

        # Example events dict: (year, month, day) -> event string
        self.events = {
            (self.today.year, self.today.month, self.today.day): "Today’s event: Meeting at 3 PM",
            (2025, 7, 4): "Independence Day",
            (2025, 12, 25): "Christmas Day",
        }

        self.draw_calendar()

    def draw_calendar(self, event=None):
        self.canvas.delete("all")
        self.date_positions.clear()

        year = self.year_var.get()
        month = self.month_names.index(self.month_var.get()) + 1

        # Weekday headers
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, day in enumerate(days):
            x = col * self.cell_width + self.cell_width // 2
            self.canvas.create_text(x, 15, text=day, font=("Arial", 10, "bold"))

        # Get calendar for the month
        month_cal = calendar.monthcalendar(year, month)

        # Draw dates
        for row in range(self.rows):
            if row >= len(month_cal):
                # Blank rows at end if month shorter than 6 weeks
                continue
            week = month_cal[row]
            for col in range(self.cols):
                day_num = week[col]
                x1 = col * self.cell_width
                y1 = row * self.cell_height + 30
                x2 = x1 + self.cell_width
                y2 = y1 + self.cell_height

                # Draw cell rectangle
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white", outline="gray")

                if day_num != 0:
                    # Save rectangle coords keyed by date
                    self.date_positions[(year, month, day_num)] = (x1, y1, x2, y2)

                    # Highlight current day
                    if (year, month, day_num) == (self.today.year, self.today.month, self.today.day):
                        self.canvas.itemconfig(rect_id, fill="#ffecb3")  # light yellow

                    # Draw day number
                    self.canvas.create_text(x1 + 10, y1 + 20, text=str(day_num), anchor="w", font=("Arial", 12))

                    # Draw a dot if event exists for that day
                    if (year, month, day_num) in self.events:
                        self.canvas.create_oval(x2 - 15, y2 - 15, x2 - 5, y2 - 5, fill="red")

    def on_canvas_click(self, event):
        x, y = event.x, event.y

        for (year, month, day), (x1, y1, x2, y2) in self.date_positions.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                # Show event info or default message
                event_text = self.events.get((year, month, day), "No events for this date.")
                self.info_label.config(text=f"{day} {self.month_var.get()} {year}: {event_text}")
                return

        # If clicked outside dates
        self.info_label.config(text="Select a valid date")

if __name__ == "__main__":
    root = tk.Tk()
    CalendarPickerApp(root)
    root.mainloop()
