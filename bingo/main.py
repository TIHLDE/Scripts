import os
import random

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from PyPDF2 import PdfMerger


sentences = []
with open("bingo/sentences.txt", "r", encoding="utf-8") as file:
    for line in file:
        sentences.append(line.strip())


for i in range(100):
    unique_sentences = list(set(sentences)) 
    pdf_file = f"bingo/pdfs/bingo{i + 1}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    c.setFont("Helvetica", 10)

    cell_width = 120
    cell_height = 120
    x_start = 5
    y_start = 625

    random.shuffle(unique_sentences)

    for row in range(5):
        for col in range(5):
            sentence = unique_sentences.pop(0)

            x = x_start + col * cell_width
            y = y_start - row * cell_height

            c.rect(x, y, cell_width, cell_height)

            max_chars = int(cell_width / 6)

            lines = []
            current_line = ""
            for word in sentence.split():
                if len(current_line) + len(word) <= max_chars:
                    current_line += word + " "
                else:
                    lines.append(current_line.strip())
                    current_line = word + " "
            if current_line:
                lines.append(current_line.strip())

            line_height = 20

            for i, line in enumerate(lines):
                c.drawString(x + 10, y + cell_height - (i * line_height) - 20, line)

    c.save()


merger = PdfMerger()
pdf_folder = "bingo/pdfs"
for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_folder, filename)
        merger.append(file_path)

merged_pdf_path = "bingo/merged_bingo.pdf"
merger.write(merged_pdf_path)
merger.close()


for filename in os.listdir(pdf_folder):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_folder, filename)
        os.remove(file_path)