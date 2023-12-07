from milvus import Milvus, DataType
import re
import spacy
from bs4 import BeautifulSoup

# Initialize Milvus client and spaCy model
milvus_client = Milvus(host='Your_Host', port='Your_Port')
nlp = spacy.load('en_core_web_md')

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    return text

def embed_text(text):
    doc = nlp(text)
    return doc.vector

def insert_to_milvus(collection_name, embeddings):
    # Define your logic to insert embeddings into Milvus
    pass

def read_texts_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        # Splitting by new lines; modify this as per your content structure
        texts = content.split('\n\n') 
        return texts

# In your main function
def main():
    texts = read_texts_from_file('overview.md')
    for text in texts:
        processed_text = preprocess_text(text)
        embeddings = embed_text(processed_text)
        insert_to_milvus('your_collection_name', embeddings)

def chunk_file(input_filename, chunk_size=1000):
    """
    Splits a large file into smaller chunk files.

    :param input_filename: The name of the large file.
    :param chunk_size: The number of lines in each chunk.
    :return: A list of filenames for the chunk files created.
    """
    chunk_filenames = []
    with open(input_filename, 'r') as file:
        chunk_file_number = 0
        chunk_file_name = f'chunk_{chunk_file_number}.md'
        chunk_file = open(chunk_file_name, 'w')
        chunk_filenames.append(chunk_file_name)
        for i, line in enumerate(file):
            if i % chunk_size == 0 and i > 0:
                chunk_file.close()
                chunk_file_number += 1
                chunk_file_name = f'chunk_{chunk_file_number}.md'
                chunk_file = open(chunk_file_name, 'w')
                chunk_filenames.append(chunk_file_name)
            chunk_file.write(line)
        chunk_file.close()
    return chunk_filenames

from bs4 import BeautifulSoup

def clean_text(text):
    """
    Cleans the given text by removing HTML tags and unwanted characters.

    :param text: The text to clean.
    :return: Cleaned text.
    """
    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(text, 'html.parser')
    cleaned_text = soup.get_text(separator=' ')

    # Further cleaning: remove special characters, numbers, etc., as per your requirement
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', cleaned_text, re.I|re.A)
    cleaned_text = cleaned_text.lower()

    return cleaned_text

def process_chunk_files(chunk_filenames):
    for filename in chunk_filenames:
        texts = read_texts_from_file(filename)
        for text in texts:
            cleaned_text = clean_text(text)  # Clean the text
            processed_text = preprocess_text(cleaned_text)  # Preprocess the cleaned text
            embeddings = embed_text(processed_text)  # Embed the text
            insert_to_milvus('your_collection_name', embeddings)  # Insert into Milvus


def main():
    chunk_filenames = chunk_file('overview.md', chunk_size=1000)  # Adjust chunk_size as needed
    process_chunk_files(chunk_filenames)

if __name__ == "__main__":
    main()


