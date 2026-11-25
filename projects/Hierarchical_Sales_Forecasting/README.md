# Hierarchical Sales Forecasting with Explainable AI

## Project Overview
This project implements a hierarchical sales forecasting pipeline using the M5 Forecasting dataset. The objective is to generate accurate and consistent sales forecasts across multiple levels of the retail hierarchy (state, store, category, product) using machine learning models and to interpret these models with explainable AI techniques.

## Objective
- Predict sales at different aggregation levels (state, store, category, product) to ensure coherent and actionable forecasts for retail operations.
- Use model explainability (SHAP) to understand the drivers of sales and support transparent decision-making.

## Dataset
- [M5 Forecasting Accuracy dataset (Kaggle)](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data)
- Contains daily sales data for thousands of products across multiple stores and states.

## Tools and Libraries
- Python 3.x
- LightGBM (gradient boosting machine learning)
- SHAP (model explainability)
- Pandas, NumPy (data manipulation)
- Matplotlib, Seaborn (visualization)

## Key Features
- **Hierarchical Forecasting:** Models sales at multiple levels of aggregation, ensuring consistency across the hierarchy.
- **Advanced Feature Engineering:** Incorporates lagged sales, rolling means, calendar events, and pricing information.
- **Model Interpretability:** Uses SHAP values to visualize and explain feature importance and model predictions.
- **Scalable Workflow:** Efficient data handling and model training for large-scale retail datasets.

## How to Run
1. Clone this repository.
2. Download the M5 dataset from Kaggle and place the CSV files in the `/data` folder.
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Open and run the Jupyter notebooks in sequence for data preparation, feature engineering, model training, and explainability.

## Results
- Achieved accurate, consistent forecasts across all hierarchy levels.
- SHAP analysis revealed key drivers of sales, such as recent demand trends, price changes, and calendar events.
- Insights support better inventory management and business planning.

## Skills Demonstrated
Python, LightGBM, SHAP, Pandas, Numpy, Data Visualization, Time Series Forecasting, Hierarchical Forecasting, Machine Learning, Feature Engineering, Model Explainability, Data Analysis

## Visuals

![Overall daily sales trend](Snippets/overall%20daily%20sales%20trend....png)

![Total sales per store](Snippets/Total%20Sales%20per%20store.png)

![Average sales by day of week](Snippets/Average%20sales%20by%20day%20for%20a%20week.png)

![SHAP summary plot for top 10 features](Snippets/SHAP%20summary%20plot%20for%20top%2010%20features.png)

The full pipeline is in [Hierarchical_Sales_Forecasting.ipynb](Hierarchical_Sales_Forecasting.ipynb).

## License
MIT License

## Acknowledgements
- M5 Forecasting Competition (Kaggle)
- Research on hierarchical and grouped time series forecasting
