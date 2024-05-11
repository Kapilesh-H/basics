{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Importing necessary libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import fitz  # PyMuPDF\n",
    "import pandas as pd\n",
    "import re"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Feature extraction strategy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def extract_features(pdf_file):\n",
    "    # Open the PDF file\n",
    "    pdf_document = fitz.open(pdf_file)\n",
    "\n",
    "    # Initialize variables for features\n",
    "    num_pages = len(pdf_document)\n",
    "    token_count = 0\n",
    "    word_count = 0\n",
    "    sentence_count = 0\n",
    "    text = ''\n",
    "\n",
    "    # Extract text and calculate features\n",
    "    for page_number in range(num_pages):\n",
    "        page = pdf_document[page_number]\n",
    "        text += page.get_text()\n",
    "\n",
    "        # Tokenization\n",
    "        tokens = re.findall(r'\\b\\w+\\b', page.get_text())\n",
    "        token_count += len(tokens)\n",
    "\n",
    "        word_count += len(page.get_text().split())\n",
    "        sentence_count += len(page.get_text().split('.'))\n",
    "\n",
    "    pdf_document.close()\n",
    "\n",
    "    # Create a dictionary to store features\n",
    "    pdf_features = {\n",
    "        'PDF File': pdf_file,\n",
    "        'Number of Pages': num_pages,\n",
    "        'Token Count': token_count,\n",
    "        'Word Count': word_count,\n",
    "        'Sentence Count': sentence_count,\n",
    "        'Text': text\n",
    "    }\n",
    "\n",
    "    return pdf_features"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Implementing data extraction"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_csv(pdf_files, output_csv):\n",
    "    # Initialize an empty list to store features for all PDFs\n",
    "    all_features = []\n",
    "\n",
    "    # Extract features for each PDF file\n",
    "    for pdf_file in pdf_files:\n",
    "        features = extract_features(pdf_file)\n",
    "        all_features.append(features)\n",
    "\n",
    "    # Convert the list of dictionaries to a pandas DataFrame\n",
    "    df = pd.DataFrame(all_features)\n",
    "\n",
    "    # Save DataFrame to a CSV file\n",
    "    df.to_csv(output_csv, index=False)\n",
    "\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

