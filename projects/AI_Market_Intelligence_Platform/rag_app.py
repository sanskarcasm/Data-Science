import streamlit as st

st.set_page_config(
    page_title="Market Intelligence Platform",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
        .main .block-container {
            padding-top: 1.5rem;
            padding-bottom: 1.5rem;
            padding-left: 2rem;
            padding-right: 2rem;
            max-width: 100vw;
        }
        .stApp {
            background-color: #f7f9fa;
        }
        .big-font {
            font-size: 1.5rem !important;
        }
        .answer-font {
            font-size: 1.2rem !important;
        }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("Logo.png", width=180)
    st.markdown("## 👋 Welcome!")
    st.write(
        "This AI-driven platform helps you extract insights from your books or market data using advanced semantic search and LLMs."
    )
    st.markdown("### 💡 Example queries:")
    st.markdown("- Books about overcoming adversity in history\n"
                "- What are the most affordable business books?\n"
                "- Recommend books on innovation and leadership")
    st.info("Tip: Enter a market or book-related question in the main panel.")
    st.markdown("---")
    st.caption("Powered by ChromaDB, LangChain, and Llama (Ollama)")

# --- MAIN LAYOUT ---
st.markdown('<h1 class="big-font">🧑‍🏫 AI Market Intelligence Platform</h1>', unsafe_allow_html=True)
st.write("Ask a question about your books or market data and get instant, AI-powered answers.")


with st.container():
    
    col1, col2 = st.columns([1, 2], gap="large")

    with col1:
        st.markdown("### 🔎 Your Query")
        user_query = st.text_input("Type your question here", placeholder="E.g., Suggest books about innovation")
        get_answer = st.button("Get Answer", use_container_width=True)

    with col2:
        st.markdown("### 🤖 AI Answer")
        if get_answer and user_query:
            with st.spinner("Thinking..."):
                
                from langchain_huggingface import HuggingFaceEmbeddings
                from langchain_chroma import Chroma
                from langchain_ollama import OllamaLLM
                from langchain.chains import RetrievalQA
                from langchain.prompts import PromptTemplate

                embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
                persist_directory = "chroma_db"
                vectorstore = Chroma(
                    persist_directory=persist_directory,
                    embedding_function=embedding_model
                )
                retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

                llm = OllamaLLM(model="llama3")  

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

                qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=retriever,
                    return_source_documents=True,
                    chain_type_kwargs={"prompt": prompt}
                )

                result = qa_chain({"query": user_query})

                # --- Display the answer ---
                st.markdown(f"<div class='answer-font'>{result['result']}</div>", unsafe_allow_html=True)

                st.markdown("---")
                st.subheader("📚 Sources")
                for doc in result["source_documents"]:
                    st.write(
                        f"**{doc.metadata.get('title', 'No title')}** – {doc.metadata.get('price', 'No price')}"
                    )

                with st.expander("Show raw source data"):
                    for doc in result["source_documents"]:
                        st.json(doc.metadata)
        else:
            st.info("Enter a question and click 'Get Answer' to see results.")

# --- FOOTER ---
st.markdown("---")
st.caption("© 2025 Market Intelligence Platform Prototype | Built with Streamlit")

