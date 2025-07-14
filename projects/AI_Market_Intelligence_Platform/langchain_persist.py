from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
persist_directory = "chroma_db"  # This must match the path you used before

vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model
)
