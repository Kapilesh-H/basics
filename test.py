##Importing necessary libraries
'''
import fitz  # PyMuPDF
import pandas as pd
import re

##Data Extraction method
'''
def extract_features(pdf_file):
    # Open the PDF file
    pdf_document = fitz.open(pdf_file)

    # Initialize variables for features
    num_pages = len(pdf_document)
    token_count = 0
    word_count = 0
    sentence_count = 0
    text = ''

    # Extract text and calculate features
    for page_number in range(num_pages):
        page = pdf_document[page_number]
        text += page.get_text()

        # Tokenization
        tokens = re.findall(r'\b\w+\b', page.get_text())
        token_count += len(tokens)

        word_count += len(page.get_text().split())
        sentence_count += len(page.get_text().split('.'))

    pdf_document.close()

    # Create a dictionary to store features
    pdf_features = {
        'PDF File': pdf_file,
        'Number of Pages': num_pages,
        'Token Count': token_count,
        'Word Count': word_count,
        'Sentence Count': sentence_count,
        'Text': text
    }

    return pdf_features
    '''


