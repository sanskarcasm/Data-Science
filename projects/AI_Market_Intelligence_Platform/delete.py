from opensearchpy import OpenSearch

# Connect to OpenSearch
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True
)

# Delete the index (replace 'books_semantic' with your index name if different)
index_name = 'books_semantic'
if client.indices.exists(index=index_name):
    client.indices.delete(index=index_name)
    print(f"Index '{index_name}' deleted.")
else:
    print(f"Index '{index_name}' does not exist.")
