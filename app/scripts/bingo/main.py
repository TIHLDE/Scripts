from app.utils.bingo import (
    extract_sentences,
    generate_pdf,
    merge_pdfs,
    clean_up,
    get_number_of_sheets
)


def create_bingo_sheets():
    """
    Create bingo sheets and merge to one pdf file.
    """
    sentences = extract_sentences()

    number = get_number_of_sheets()

    print(f"\nGenererer {number} bingobrett...\n")
    for i in range(number):
        generate_pdf(i, sentences)
    
    print("Slår sammen bingobrettene til en pdf-fil...\n")
    merge_pdfs()
    clean_up()
    print("Ferdig! Bingo-brettet er laget og ligger i mappen 'downloads'.")
