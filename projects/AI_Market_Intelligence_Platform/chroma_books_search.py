import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_collection("books")
model = SentenceTransformer('all-MiniLM-L6-v2')

query = "adventure stories with friendship"
query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=5
)

print("Top semantic matches:")
for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
    print(f"{doc} | {meta['price']}")
