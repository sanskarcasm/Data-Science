# Data Science & Analytics Portfolio: Sanskar Pant

Data analyst with retail media and campaign measurement experience (Boots Media Group, London) and an MSc in Data Science and AI (University of Liverpool). This repository holds the projects behind my CV: BI dashboards, forecasting, LLM and RAG applications, and analytics write-ups. Each project sits in its own folder under [`projects/`](projects) with a README, code and outputs.

**Contact:** [Email](mailto:sanskaraugpant@gmail.com) · [LinkedIn](https://www.linkedin.com/in/sanskar-pant-44b3801ab) · [Portfolio website](https://www.datascienceportfol.io/sanskaraugpant)

---

## Projects at a glance

| Project | What it shows | Tools |
|---|---|---|
| [Olist Churn Analysis & BI Dashboard](projects/Power_BI_Projects/Churn_Analysis) | Star-schema data model, churn and revenue KPIs, Power BI report | Python, SQL, Power BI, DAX |
| [Hierarchical Sales Forecasting](projects/Hierarchical_Sales_Forecasting) | Forecasts across state, store and product with explainable AI | Python, LightGBM, SHAP, pandas |
| [Instagram Performance Analytics](projects/Power_BI_Projects/Instagram_Performance_Analytics) | Engagement, reach and content-type analysis | Power BI, Python, Excel |
| [Retail Sales Analysis](projects/Power_BI_Projects/Retail_Sales_Analysis) | Sales trends, YTD and year-on-year KPIs, regional and category views | Power BI, DAX |
| [Global Chocolate Sales Dashboard](projects/Power_BI_Projects/Global_Chocolate_Sales) | Executive KPI dashboard across 5 regions | Power BI, DAX, Excel |
| [Airport Catering Performance Analysis](projects/Airport_Catering_Performance_Analysis) | Like-for-like sales, spend per passenger, outlet performance | Excel (SUMIFS, INDEX/MATCH, MAXIFS) |
| [AI Market Intelligence Platform (RAG)](projects/AI_Market_Intelligence_Platform) | Retrieval-augmented generation over business and market data | Python, Sentence Transformers, ChromaDB, Llama 3 (Ollama), Streamlit |
| [AI Sales Call Summarizer with CRM Integration](projects/AI_Sales_Call_Summarizer) | Call transcription, LLM summaries, HubSpot CRM updates | Python, Whisper, Llama 3, HubSpot API, Streamlit |
| [LLM Benchmarking for Cell Type Annotation](projects/LLM_Cell_Type_Annotation_Benchmarking) | MSc dissertation: benchmarking open-source LLMs on scRNA-seq data | Python, Scanpy, Hugging Face, HPC |
| [Tweet Sentiment Analyser](projects/Tweet_Sentiment_Analyser) | Twitter/X API collection and sentiment labelling | Python, Tweepy, TextBlob |
| [Gender Classification (ML basics)](projects/Gender_Classification_ML) | Comparing three classifiers on a small sample | scikit-learn |

---

## Business intelligence and analytics

### Olist Churn Analysis & BI Dashboard (Aug 2025)
Cleaned and modelled the Olist e-commerce data into a star schema (fact_orders plus customer, product, seller, geography and date dimensions), engineered churn, delivery-delay and revenue metrics in Python, and built a Power BI report. It highlighted a 93.7% churn rate and the geographic and product segments that matter most for retention.

### Instagram Performance Analytics (Jun 2025)
Analysed engagement and reach by post type and location in Power BI, with supporting Python analysis. Reels were the strongest content type, with clear regional targeting opportunities.

### Retail Sales Analysis (Jun 2025)
Interactive Power BI dashboard tracking total sales, Sales YTD and year-on-year growth, with regional and category breakdowns and the DAX measures documented.

### Global Chocolate Sales Dashboard (May 2025)
Executive Power BI dashboard for 12 months of global sales across 5 regions, with KPI tracking and multi-year comparisons.

### Airport Catering Performance Analysis (Aug 2026)
Interactive Excel dashboard built from 18 months of sales and passenger data for five airport catering outlets. A like-for-like January to June comparison tracks YTD sales, year-on-year growth, spend per passenger and outlet performance. It found that one outlet drove over half of all revenue, caught a likely data error inflating one month by about 10x, and surfaced a declining outlet early.

## Forecasting and machine learning

### Hierarchical Sales Forecasting with Explainable AI (Jun 2025)
Daily forecasts across a 4-level hierarchy (state, store, category, product) on the M5 dataset with LightGBM. Lag, rolling, calendar and price features improved RMSE by 18%, and SHAP on 100K+ predictions showed sell price and seasonality as the main drivers.

### Gender Classification (Mar 2025)
An introductory scikit-learn exercise comparing a Decision Tree, an SVM and k-Nearest Neighbours on a small hand-entered sample of height, weight and shoe size.

## AI and LLM applications

### AI Market Intelligence Platform (2025)
A RAG application that ingests scraped and CSV data, embeds it with Sentence Transformers, stores vectors in ChromaDB and answers questions with Llama 3 via Ollama, through a Streamlit interface.

### AI Sales Call Summarizer with CRM Integration (Jun 2025)
Transcribes sales calls with Whisper, extracts concerns, action items and next steps with Llama 3, and logs them to HubSpot CRM through its API. Sample outputs are in [`sample_outputs/`](projects/AI_Sales_Call_Summarizer/sample_outputs).

### LLM Benchmarking for Cell Type Annotation (May to Sep 2024, MSc dissertation)
Benchmarked open-source LLMs for automated cell type annotation in single-cell RNA-seq data across 100K+ records, with UMAP visualisations and accuracy, recall and F1 comparisons.

### Tweet Sentiment Analyser (Apr 2025)
Pulls recent tweets for a query through the Twitter/X API with Tweepy, labels sentiment with TextBlob and saves the results to CSV, with automatic rate-limit handling.

---

## Skills shown across these projects
SQL, Python (pandas, NumPy, scikit-learn), Power BI and DAX, Excel modelling, data modelling (star schema), LightGBM and SHAP, LLMs and RAG (Llama 3, Ollama, ChromaDB, Sentence Transformers, Hugging Face), Whisper, Streamlit, REST APIs (HubSpot, Twitter/X), Scanpy and HPC.

## Running the code
Each project lists its own setup steps. To install the main Python libraries in one go:
```bash
pip install -r requirements.txt
```
API keys (HubSpot, Twitter/X) are read from environment variables and are never stored in this repository.
