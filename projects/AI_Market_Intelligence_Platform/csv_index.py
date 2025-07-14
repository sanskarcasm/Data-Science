import pandas as pd
from opensearchpy import OpenSearch

# Load the CSV
df = pd.read_csv('books.csv')

# Connect to OpenSearch/Elasticsearch
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_compress=True
)

# Create index if not exists
index_name = 'books'
if not client.indices.exists(index=index_name):
    client.indices.create(index=index_name)

# Index each row
for _, row in df.iterrows():
    doc = {
        'title': row['Title'],
        'price': row['Price']
    }
    client.index(index=index_name, body=doc)

print("Indexing complete! All books are now searchable in OpenSearch/Elasticsearch.")
response = client.search(index=index_name, body={"query": {"match_all": {}}}, size=5)
for hit in response['hits']['hits']:
    print(hit['_source'])
