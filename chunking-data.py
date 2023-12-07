from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Milvus
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter

loader = WebBaseLoader([
    "overview.md",
])

docs = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
docs = text_splitter.split_documents(docs)

# The output of the text splitter would be similar to the following:

# Created a chunk of size 1745, which is longer than the specified 1024
# Created a chunk of size 1278, which is longer than the specified 1024