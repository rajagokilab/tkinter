import tkinter as tk
from tkinter import ttk, font, filedialog, messagebox
import tempfile
import io
from PIL import Image, ImageOps

PREVIEW_TEXT = "The quick brown fox jumps over the lazy dog"
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 250


def main():
    root = tk.Tk()
    root.title("Font Preview Tool")

    # ---- Top control frame ----
    control_frame = ttk.Frame(root, padding=10)
    control_frame.pack(fill="x")

    # Font family selector
    ttk.Label(control_frame, text="Font:").pack(side="left", padx=(0, 5))
    families = sorted(set(font.families()))
    font_family_var = tk.StringVar(value=families[0] if families else "Arial")
    family_box = ttk.Combobox(control_frame, textvariable=font_family_var, values=families, state="readonly", width=30)
    family_box.pack(side="left", padx=(0, 15))

    # Font size selector
    ttk.Label(control_frame, text="Size:").pack(side="left", padx=(0, 5))
    font_size_var = tk.IntVar(value=24)
    size_spin = tk.Spinbox(control_frame, from_=6, to=200, textvariable=font_size_var, width=5, command=lambda: update_preview())
    size_spin.pack(side="left")

    # Save button
    save_btn = ttk.Button(control_frame, text="Save as PNG", command=lambda: save_preview())
    save_btn.pack(side="right")

    # ---- Canvas ----
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack(fill="both", expand=True, padx=10, pady=10)

    # ---- Helper functions ----
    def update_preview(event=None):
        """Redraw the preview text with the selected font and size."""
        canvas.delete("all")
        current_font = font.Font(family=font_family_var.get(), size=int(font_size_var.get()))
        canvas_font = current_font.actual()
        # Center text on canvas
        canvas.create_text(CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2, text=PREVIEW_TEXT, font=canvas_font, fill="black", anchor="center")

    def save_preview():
        """Save the canvas content as a PNG using a PostScript dump and Pillow conversion."""
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
        if not file_path:
            return
        try:
            # Export canvas to PostScript
            ps_data = canvas.postscript(colormode='color')
            # Convert to image via Pillow
            image = Image.open(io.BytesIO(ps_data.encode('utf-8')))
            # Remove extra whitespace and resize to exact canvas size
            image = ImageOps.fit(image, (CANVAS_WIDTH, CANVAS_HEIGHT), Image.LANCZOS)
            image.save(file_path, 'PNG')
            messagebox.showinfo("Success", f"Preview saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save image: {e}")

    # ---- Event bindings ----
    family_box.bind('<<ComboboxSelected>>', update_preview)
    font_size_var.trace_add('write', lambda *args: update_preview())
    canvas.bind('<Configure>', update_preview)  # Update when canvas size changes

    # Initial draw
    update_preview()

    root.mainloop()


if __name__ == "__main__":
    main()
