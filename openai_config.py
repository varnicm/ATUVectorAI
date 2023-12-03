from os import environ

MILVUS_HOST = "localhost"
MILVUS_PORT = "19530"
OPENAI_API_KEY = "" # example: "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

environ["OPENAI_API_KEY"] = OPENAI_API_KEY
