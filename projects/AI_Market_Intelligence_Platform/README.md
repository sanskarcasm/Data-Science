
📚 AI-Driven Market Intelligence Platform
A next-generation platform that leverages Retrieval-Augmented Generation (RAG), semantic search, and large language models (LLMs) to deliver actionable insights from your own business, product, or market data.
Built with Python, Streamlit, ChromaDB, and Llama (Ollama).

🛑 Problem Statement
Modern businesses are overwhelmed by the volume and complexity of market, product, and competitor data.
Manual research is slow, error-prone, and cannot scale to deliver real-time, actionable insights.
Key challenges include:

Extracting relevant information from massive, unstructured datasets

Surfacing trends, recommendations, and risks quickly

Reducing human bias and error in research and reporting

Empowering non-technical users to access deep insights instantly

Our platform solves these problems by combining semantic search with AI-powered answer generation, delivering fast, accurate, and context-aware intelligence from your own data.

🎯 Objectives & Aims
Automate Market Intelligence: Rapidly extract insights from large, diverse datasets (books, products, articles, market reports).

Empower Decision-Making: Provide users with fast, accurate, and context-aware answers to complex queries.

Leverage AI for Competitive Edge: Use state-of-the-art retrieval and generation to surface trends, recommendations, and actionable knowledge.

🧩 Methods & Workflow
Data Collection & Scraping:
Scrape or import structured/unstructured data (e.g., books, product info, news articles) using Python scripts.

Prototype Note:
Data for this prototype was scraped from the BooksToScrap website.
In an industrial setting, the same pipeline can be adapted to scrape or ingest data from any required business, product, or news website, as well as internal documents and APIs.

Preprocessing & Embedding:
Clean and preprocess text data. Use Sentence Transformers to convert text into semantic embeddings.

Indexing with ChromaDB:
Store embeddings and metadata in a vector database for fast, semantic search.

Semantic Retrieval:
Retrieve the most relevant documents for a user’s query using vector similarity.

Retrieval-Augmented Generation (RAG):
Pass the query and retrieved context to an LLM (Llama via Ollama) to generate grounded, natural language answers.

User Interface:
A modern Streamlit web app for interactive querying and instant results.

🛠️ Tools & Technologies
Tool/Lib	Purpose
Python	Core programming language
Streamlit	Interactive web UI
ChromaDB	Vector database for semantic search
Sentence Transformers	Embedding generation
LangChain	RAG pipeline orchestration
Llama (Ollama)	Local LLM for answer generation
BeautifulSoup/Scrapy	(Optional) Web scraping utilities
📂 Project Structure & File Descriptions
text
MarketIntelligencePlatform/
│
├── chroma_db/                # ChromaDB persistent vector database (auto-generated)
├── venv/                     # Python virtual environment (not tracked in Git)
│
├── books/                    # Folder for raw and processed book data
│
├── chroma_books_search.py    # Script for searching books in ChromaDB
├── chroma_books_semantic.py  # Script for semantic search in ChromaDB
│
├── csv_index.py              # Script for indexing CSV data into ChromaDB
├── delete.py                 # Utility script for deleting/resetting data
│
├── langchain_persist.py      # Script to preprocess, embed, and persist data in ChromaDB
├── Logo/                     # Folder for branding assets (e.g., logo images)
│
├── rag_app.py                # Main Streamlit app (UI + RAG pipeline)
├── rag_llama.py              # Script for running the RAG pipeline via CLI
│
├── scrape_article.py         # Script for scraping articles or web data
│
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation file
File Details
chroma_books_search.py / chroma_books_semantic.py
Scripts for searching and retrieving books from ChromaDB using keyword or semantic queries.

csv_index.py
Indexes book data from CSV files into ChromaDB.

delete.py
Utility to delete or reset ChromaDB collections.

langchain_persist.py
Preprocesses, embeds, and stores your data in ChromaDB. Run this after scraping/importing new data.

scrape_article.py
Scrapes data from BooksToScrap (for prototype) or can be adapted for other websites/articles.

rag_app.py
Main Streamlit application. Provides a user-friendly web interface for querying your data using RAG.

rag_llama.py
Command-line script for running the RAG pipeline (retrieval + LLM answer) without the UI.

Logo/
Store your logo and branding images here (optional).

books/
Folder for storing raw and processed book data.

chroma_db/
Auto-generated folder where ChromaDB stores your vector database (do not edit manually).

🏁 Getting Started
1. Clone this repo
bash
git clone https://github.com/yourusername/MarketIntelligencePlatform.git
cd MarketIntelligencePlatform
2. Install dependencies
bash
pip install -r requirements.txt
3. Prepare your data
For the prototype, data is already scraped from BooksToScrap.

To use your own data, adapt scrape_article.py or add your files to the books/ folder.

4. Index your data
bash
python langchain_persist.py
5. Start Ollama and pull Llama model
bash
ollama pull llama3
ollama serve
6. Run the Streamlit app
bash
streamlit run rag_app.py
📈 Future Scope
Multi-Source Integration: Ingest news, social media, competitor websites, and internal documents.

Real-Time Intelligence: Enable continuous data scraping and live updates.

Personalization: Tailor insights and recommendations to individual users or business units.

Advanced Analytics: Integrate visualization, trend detection, and forecasting modules.

Productionization: Add authentication, monitoring, and cloud deployment for enterprise use.

📝 Conclusion
This project demonstrates a powerful, modular approach to AI-driven market intelligence:

Solves the problem of slow, manual, and error-prone market research

Transforms raw data into actionable insights in seconds

Combines the best of semantic search and LLMs

Ready for demo, feedback, and future expansion

Whether you’re a business analyst, data scientist, or AI enthusiast, this platform provides a robust foundation for next-generation decision support.

🤝 Contributing
Pull requests and feedback are welcome!
Feel free to open issues for suggestions, bugs, or feature requests.

📄 License
MIT License

Built with ❤️ using Python, Streamlit, ChromaDB, and Llama.

For questions or collaboration, please contact [your-email@example.com].
