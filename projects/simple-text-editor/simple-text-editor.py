"""
simple_text_editor.py

A minimal text editor (built with tkinter) that can save your writing
directly as a PDF. No Word, no LibreOffice — just Python.

Requirements:
    pip install reportlab

Usage:
    python simple_text_editor.py

Features:
- New / Open / Save (.txt) / Save As
- Export to PDF (with automatic line-wrapping and pagination)
- Basic keyboard shortcuts: Ctrl+N (new), Ctrl+O (open), Ctrl+S (save)
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Untitled - Simple Text Editor")
        self.root.geometry("800x600")

        self.current_file = None  # tracks the currently open .txt file, if any

        self._build_menu()
        self._build_text_area()
        self._bind_shortcuts()

    # ---------- UI setup ----------

    def _build_menu(self):
        menu_bar = tk.Menu(self.root)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Export as PDF...", command=self.export_as_pdf)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menu_bar.add_cascade(label="File", menu=file_menu)
        self.root.config(menu=menu_bar)

    def _build_text_area(self):
        self.text_area = tk.Text(
            self.root, wrap="word", undo=True, font=("Helvetica", 12)
        )
        self.text_area.pack(fill="both", expand=True)

    def _bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())

    # ---------- File operations ----------

    def new_file(self):
        if self._confirm_discard_changes():
            self.text_area.delete("1.0", tk.END)
            self.current_file = None
            self.root.title("Untitled - Simple Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not file_path:
            return

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        self.text_area.delete("1.0", tk.END)
        self.text_area.insert("1.0", content)
        self.current_file = file_path
        self.root.title(f"{Path(file_path).name} - Simple Text Editor")

    def save_file(self):
        if self.current_file:
            self._write_txt(self.current_file)
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not file_path:
            return
        self._write_txt(file_path)
        self.current_file = file_path
        self.root.title(f"{Path(file_path).name} - Simple Text Editor")

    def _write_txt(self, file_path):
        content = self.text_area.get("1.0", tk.END)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    # ---------- PDF export ----------

    def export_as_pdf(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")],
        )
        if not file_path:
            return

        content = self.text_area.get("1.0", tk.END)

        try:
            self._render_pdf(content, file_path)
            messagebox.showinfo("Success", f"Saved PDF to:\n{file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not create PDF:\n{e}")

    def _render_pdf(self, text, output_path, font_name="Helvetica", font_size=12):
        """
        Renders plain text into a paginated PDF, wrapping long lines to fit
        the page width and starting new pages as needed.
        """
        c = canvas.Canvas(output_path, pagesize=LETTER)
        page_width, page_height = LETTER

        margin = 1 * inch
        max_width = page_width - 2 * margin
        line_height = font_size * 1.2

        c.setFont(font_name, font_size)
        y = page_height - margin

        for raw_line in text.split("\n"):
            wrapped_lines = self._wrap_line(c, raw_line, font_name, font_size, max_width)

            # Preserve blank lines
            if not wrapped_lines:
                wrapped_lines = [""]

            for line in wrapped_lines:
                if y < margin:  # start a new page
                    c.showPage()
                    c.setFont(font_name, font_size)
                    y = page_height - margin

                c.drawString(margin, y, line)
                y -= line_height

        c.save()

    @staticmethod
    def _wrap_line(c, line, font_name, font_size, max_width):
        """Breaks a single line of text into pieces that fit within max_width."""
        if line == "":
            return []

        words = line.split(" ")
        wrapped = []
        current = ""

        for word in words:
            candidate = f"{current} {word}".strip()
            if c.stringWidth(candidate, font_name, font_size) <= max_width:
                current = candidate
            else:
                if current:
                    wrapped.append(current)
                current = word

        if current:
            wrapped.append(current)

        return wrapped

    # ---------- Helpers ----------

    def _confirm_discard_changes(self):
        # Simple guard so "New" doesn't silently wipe unsaved work.
        if self.text_area.get("1.0", tk.END).strip():
            return messagebox.askyesno(
                "New File", "Discard current content and start a new file?"
            )
        return True


def main():
    root = tk.Tk()
    app = SimpleTextEditor(root)
    root.mainloop()


if __name__ == "__main__":
    main()