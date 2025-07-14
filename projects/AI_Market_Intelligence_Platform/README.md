# 🧑‍🏫 **AI-Driven Market Intelligence Platform**

A next-generation platform that leverages **Retrieval-Augmented Generation (RAG)**, **semantic search**, and **large language models (LLMs)** to deliver actionable insights from your own business, product, or market data.  
Built with **Python**, **Streamlit**, **ChromaDB**, and **Llama (via Ollama)**.

---

## 🛑 **Problem Statement**

Modern businesses are overwhelmed by the volume and complexity of market, product, and competitor data. Manual research is:

- Slow and error-prone  
- Difficult to scale  
- Biased by human judgment  
- Inaccessible to non-technical users  

### **Key Challenges**

- Extracting relevant information from massive, unstructured datasets  
- Surfacing trends, recommendations, and risks quickly  
- Reducing human bias and error in research  
- Empowering all users with real-time, intelligent answers  

This platform solves these problems by combining semantic search with AI-powered answer generation, delivering **fast**, **accurate**, and **context-aware intelligence** from your data.

---

## 🎯 **Objectives & Aims**

- **Automate Market Intelligence**: Extract insights from large, diverse datasets (books, product catalogs, news articles).
- **Empower Decision-Making**: Answer complex queries with speed, precision, and context.
- **Leverage AI for Competitive Edge**: Detect trends, make recommendations, and uncover insights.

---

## 🧩 **Methods & Workflow**

1. **Data Collection & Scraping**  
   - Import or scrape structured/unstructured data using Python scripts.  
   - _Prototype Note_: Sample data scraped from [BooksToScrap](http://books.toscrape.com/). In production, this can be adapted to scrape business websites, internal documents, APIs, etc.

2. **Preprocessing & Embedding**  
   - Clean text and convert to semantic embeddings using `Sentence Transformers`.

3. **Indexing with ChromaDB**  
   - Store embeddings and metadata in `ChromaDB` for efficient semantic retrieval.

4. **Semantic Retrieval**  
   - Retrieve relevant documents using vector similarity search.

5. **Retrieval-Augmented Generation (RAG)**  
   - Combine user queries with retrieved context and generate grounded answers using LLMs (via `Llama` from `Ollama`).

6. **User Interface**  
   - Interactive querying and results via a modern `Streamlit` web app.

---

## 🛠️ **Tools & Technologies**

| **Tool/Library**        | **Purpose**                                        |
|-------------------------|----------------------------------------------------|
| Python                  | Core programming language                          |
| Streamlit               | Interactive web UI                                 |
| ChromaDB                | Vector database for semantic search                |
| Sentence Transformers   | Embedding generation                               |
| LangChain               | RAG pipeline orchestration                         |
| Llama (Ollama)          | Local LLM for natural language answer generation   |
| BeautifulSoup/Scrapy    | Optional: Web scraping utilities                   |

---

## 📂 **Project Structure**

MarketIntelligencePlatform/
│
├── chroma_db/ # ChromaDB vector database (auto-generated)
├── venv/ # Python virtual environment (not tracked)
├── books/ # Raw and processed book data
├── Logo/ # Branding assets (e.g., logos)
│
├── chroma_books_search.py # Keyword search in ChromaDB
├── chroma_books_semantic.py # Semantic search in ChromaDB
├── csv_index.py # Index CSV data into ChromaDB
├── delete.py # Utility for deleting/resetting ChromaDB
├── langchain_persist.py # Preprocess and embed data
├── rag_app.py # Main Streamlit RAG interface
├── rag_llama.py # CLI RAG pipeline runner
├── scrape_article.py # Article/web data scraper
├── requirements.txt # Python dependencies
└── README.md # Documentation (this file)

yaml
Copy
Edit

### 🔍 **File Highlights**

- **`chroma_books_search.py / chroma_books_semantic.py`**  
  Search ChromaDB using keyword or semantic queries.

- **`csv_index.py`**  
  Index structured CSV data.

- **`delete.py`**  
  Reset or clear ChromaDB collections.

- **`langchain_persist.py`**  
  Preprocess, embed, and persist new data.

- **`scrape_article.py`**  
  Scrape articles (prototype: BooksToScrap).

- **`rag_app.py`**  
  Streamlit app for querying and viewing results.

- **`rag_llama.py`**  
  Run RAG pipeline via CLI without UI.

---

## 🏁 **Getting Started**

### **1. Clone this repository**

git clone https://github.com/yourusername/MarketIntelligencePlatform.git
cd MarketIntelligencePlatform

2. Install dependencies

pip install -r requirements.txt

3. Prepare your data
Prototype data is preloaded from BooksToScrap. To use your own:

Modify scrape_article.py, or

Drop files into the books/ folder

4. Index your data

python langchain_persist.py

5. Start Ollama with Llama model

ollama pull llama3
ollama serve

6. Launch the Streamlit app

streamlit run rag_app.py
📈 Future Scope
Multi-Source Integration: Ingest news, social media, internal docs

Real-Time Intelligence: Enable live scraping & updates

Personalization: Tailored insights per user or department

Advanced Analytics: Visualizations, forecasting, trend detection

Productionization: Authentication, cloud deployment, monitoring

📝 Conclusion
This project demonstrates a modular, powerful AI-powered platform for market intelligence that:

✅ Solves the pain of manual market research
✅ Turns raw data into actionable insights
✅ Combines the best of retrieval and generation
✅ Ready for demos, feedback, and scaling

Whether you're a business analyst, data scientist, or AI enthusiast, this platform is a solid foundation for next-gen decision support.

🤝 Contributing
Pull requests and feedback are welcome!
Feel free to open issues for suggestions, bugs, or feature requests.

📄 License
MIT License

Built with ❤️ using Python, Streamlit, ChromaDB, and Llama (Ollama).
For questions or collaboration: sanskaraugpant@gmail.com
