import chromadb
from sentence_transformers import SentenceTransformer
import pandas as pd

# Load your CSV data
df = pd.read_csv('books.csv')

# Initialize Chroma client
client = chromadb.PersistentClient(path="chroma_db")
collection_name = "books"

# Try to get or create the collection
try:
    collection = client.get_collection(collection_name)
    print(f"Collection '{collection_name}' already exists.")
except chromadb.errors.NotFoundError:
    collection = client.create_collection(collection_name)
    print(f"Collection '{collection_name}' created.")

# Check if collection is empty before indexing
if collection.count() == 0:
    # Load embedding model
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # Index each book (title + price)
    for i, row in df.iterrows():
        title = str(row['Title'])
        price = str(row['Price'])
        embedding = model.encode(title).tolist()
        collection.add(
            documents=[title],
            embeddings=[embedding],
            metadatas=[{"price": price}],
            ids=[str(i)]
        )
    print("All books indexed in Chroma!")
else:
    print(f"Collection '{collection_name}' already has data.")

print("Number of documents in collection:", collection.count())
print("Peek:", collection.peek())

