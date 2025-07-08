import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# Try importing PdfMerger (new) or fallback to PdfFileMerger (old)
try:
    from PyPDF2 import PdfMerger
except ImportError:
    from PyPDF2 import PdfFileMerger as PdfMerger


class PDFMergerUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("600x400")

        self.pdf_files = []

        self.create_toolbar()
        self.create_paned_window()

    def create_toolbar(self):
        toolbar = tk.Frame(self.root, bd=1, relief=tk.RAISED, bg="#ddd")
        toolbar.pack(side="top", fill="x")

        tk.Button(toolbar, text="Add File", command=self.add_file).pack(side="left", padx=5, pady=5)
        tk.Button(toolbar, text="Remove File", command=self.remove_file).pack(side="left", padx=5, pady=5)
        tk.Button(toolbar, text="Merge", command=self.merge_pdfs).pack(side="left", padx=5, pady=5)

    def create_paned_window(self):
        paned = ttk.Panedwindow(self.root, orient=tk.VERTICAL)
        paned.pack(fill="both", expand=True)

        # Top pane: Listbox for files
        top_frame = ttk.Frame(paned)
        ttk.Label(top_frame, text="Selected PDF Files:").pack(anchor="w", padx=5, pady=5)

        self.listbox = tk.Listbox(top_frame, selectmode=tk.SINGLE)
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)

        paned.add(top_frame, weight=1)

        # Bottom pane: Text for log/preview
        bottom_frame = ttk.Frame(paned)
        ttk.Label(bottom_frame, text="Log / Preview:").pack(anchor="w", padx=5, pady=5)

        self.log_text = tk.Text(bottom_frame, height=8, state="disabled", bg="#f0f0f0")
        self.log_text.pack(fill="both", expand=True, padx=5, pady=5)

        paned.add(bottom_frame, weight=0)

    def add_file(self):
        files = filedialog.askopenfilenames(title="Select PDF Files",
                                            filetypes=[("PDF Files", "*.pdf")])
        if files:
            for f in files:
                if f not in self.pdf_files:
                    self.pdf_files.append(f)
                    self.listbox.insert(tk.END, f)
            self.log("Added files.")

    def remove_file(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showinfo("Remove File", "Select a file to remove.")
            return
        idx = selected[0]
        removed_file = self.pdf_files.pop(idx)
        self.listbox.delete(idx)
        self.log(f"Removed file: {removed_file}")

    def merge_pdfs(self):
        if len(self.pdf_files) < 2:
            messagebox.showinfo("Merge PDFs", "Add at least two PDF files to merge.")
            return

        output_path = filedialog.asksaveasfilename(title="Save Merged PDF",
                                                   defaultextension=".pdf",
                                                   filetypes=[("PDF Files", "*.pdf")])
        if not output_path:
            return

        merger = PdfMerger()
        try:
            for pdf in self.pdf_files:
                merger.append(pdf)
                self.log(f"Appended: {pdf}")
            merger.write(output_path)
            merger.close()
            messagebox.showinfo("Merge Complete", f"Merged PDF saved:\n{output_path}")
            self.log(f"Merge successful: {output_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to merge PDFs:\n{e}")
            self.log(f"Merge failed: {e}")

    def log(self, message):
        self.log_text.config(state="normal")
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFMergerUI(root)
    root.mainloop()
