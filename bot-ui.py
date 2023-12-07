
import re
import spacy
import config
from milvus import Milvus, MetricType

milvus_client = Milvus(host=config.MILVUS_HOST, port=config.MILVUS_PORT)

def search_in_milvus(query_embedding, top_k=10):
    search_param = {"metric_type": MetricType.IP, "params": {"nprobe": 10}}
    status, results = milvus_client.search(collection_name='your_collection',
                                           query_records=[query_embedding],
                                           top_k=top_k,
                                           params=search_param)
    if not status.OK():
        return []
    return results

def format_results_for_cli(search_results):
    formatted_results = []
    for result in search_results:
        # Each result is processed to create a readable string
        # This is a placeholder; adjust the formatting as needed
        formatted_result = f"Document ID: {result.id}, Score: {result.distance}"
        formatted_results.append(formatted_result)
    return "\n".join(formatted_results)

def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove special characters
    text = re.sub(r'[^a-zA-Z\s]', '', text, re.I|re.A)
    return text

# Load spaCy's medium English model
nlp = spacy.load('en_core_web_md')

def embed_text(text):
    doc = nlp(text)
    return doc.vector

def process_query(user_query):
    # Preprocess the query
    preprocessed_query = preprocess_text(user_query)

    # Embed the query
    query_embedding = embed_text(preprocessed_query)

    # Search in Milvus
    search_results = search_in_milvus(query_embedding)

    # Format the results for CLI output
    formatted_results = format_results_for_cli(search_results)
    return formatted_results

def format_results_for_cli(search_results):
    # Format the search results into a readable format for CLI output
    # This can be as simple as a list of titles, a numbered list, etc.
    # The formatting will depend on the structure of your search results
    return "\n".join([str(result) for result in search_results])

def main():
    user_query = input("Enter your question: ")
    results = process_query(user_query)
    print(results)

if __name__ == "__main__":
    main()
