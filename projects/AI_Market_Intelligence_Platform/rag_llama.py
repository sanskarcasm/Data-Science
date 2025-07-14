from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


# 1. Load embeddings and vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
persist_directory = "chroma_db"  # This must match your previous Chroma persist path

vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding_model
)

# 2. Set up the retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# 3. Set up the Llama LLM via Ollama
llm = Ollama(model="llama3")  # or "llama2" if you pulled that

# 4. (Optional) Prompt template for better answers
prompt_template = """
You are a helpful assistant. Use ONLY the provided book information to answer the user's question.
If the answer is not in the context, say you don't know.

Context:
{context}

Question:
{question}

Answer:
"""
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# 5. Build the RetrievalQA chain (RAG)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)

# 6. Ask your question!
query = "Suggest books about overcoming adversity in history."
result = qa_chain({"query": query})

print("LLM Answer:\n", result["result"])
