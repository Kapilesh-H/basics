# -*- coding: utf-8 -*-
"""### **Importing necessary libraries**"""

import fitz  # PyMuPDF
import pandas as pd
import re

"""### **Extracting features**"""

'''This function helps to extract the various features of an input pdf such file name, no. of pages, count of tokens, words & sentence and finally the text present in the pdf and store it in form of a dictionary'''

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

"""### **Dict->CSV**"""

'''This method helps us to convert the above extracted dictionary of features into a target csv file'''

def create_csv(pdf_files, output_csv):
    # Initialize an empty list to store features for all PDFs
    all_features = []

    # Extract features for each PDF file
    for pdf_file in pdf_files:
        features = extract_features(pdf_file)
        all_features.append(features)

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(all_features)

    # Save DataFrame to a CSV file
    df.to_csv(output_csv, index=False)

    return df
