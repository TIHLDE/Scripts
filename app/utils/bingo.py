import os
import random

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

from PyPDF2 import PdfMerger

from app.exceptions import (
    FileNotFound,
    DirectoryNotFound
)


def get_number_of_sheets() -> int:
    DEFAULT_NUMBER_OF_SHEETS = 10

    number = input("Hvor mange bingobrett vil du generere? (Standard er 10): ")

    if not number:
        return DEFAULT_NUMBER_OF_SHEETS
    
    try:
        return int(number)
    except ValueError:
        return DEFAULT_NUMBER_OF_SHEETS


def extract_sentences() -> list[str]:
    path = "app/scripts/bingo/sentences.txt"

    if not os.path.exists(path):
        raise FileNotFound("Kunne ikke finne filen med setningene. En fil med navn 'sentences.txt' må ligge i mappen 'bingo'.")
    
    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:
        return [line.strip() for line in file]


def generate_pdf(index: int, sentences: list[str]):
    unique_sentences = list(set(sentences)) 
    directory = "app/scripts/bingo/pdfs"

    if not os.path.exists(directory):
        raise DirectoryNotFound("Kunne ikke finne mappen 'pdfs'. Denne mappen må ligge i mappen 'bingo'.")

    pdf_file = f"{directory}/bingo{index + 1}.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)

    c.setFont("Helvetica", 10)

    CELL_WIDTH = 120
    CELL_HEIGHT = 120
    X_START = 5
    Y_START = 625

    random.shuffle(unique_sentences)

    for row in range(5):
        for col in range(5):
            sentence = unique_sentences.pop(0)

            x = X_START + col * CELL_WIDTH
            y = Y_START - row * CELL_HEIGHT

            c.rect(x, y, CELL_WIDTH, CELL_HEIGHT)

            max_chars = int(CELL_WIDTH / 6)

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
                c.drawString(x + 10, y + CELL_HEIGHT - (i * line_height) - 20, line)

    c.save()


def merge_pdfs():
    merger = PdfMerger()
    pdf_folder = "app/scripts/bingo/pdfs"
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            merger.append(file_path)
    
    merger.write("downloads/bingo.pdf")
    merger.close()


def clean_up():
    pdf_folder = "app/scripts/bingo/pdfs"
    for filename in os.listdir(pdf_folder):
        file_path = os.path.join(pdf_folder, filename)
        os.remove(file_path)