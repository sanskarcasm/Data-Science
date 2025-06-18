# Hierarchical Sales Forecasting with Explainable AI

## Project Overview
This project implements a hierarchical sales forecasting model using the M5 Forecasting dataset. The model predicts sales at multiple levels of the retail hierarchy including state, store, category, and product. It leverages LightGBM for time series forecasting and SHAP for model explainability.

## Features
- Multi-level hierarchical forecasting
- Feature engineering with lag and rolling window sales
- Model explainability using SHAP values
- Interactive dashboards built with Power BI for drill-down analysis

## Dataset
The project uses the [M5 Forecasting Accuracy dataset](https://www.kaggle.com/competitions/m5-forecasting-accuracy/data) from Kaggle, which contains detailed sales data for retail products across multiple stores and states.

## Tools and Libraries
- Python 3.10
- LightGBM
- SHAP
- Power BI
- Pandas, NumPy, Matplotlib

## How to Use
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Prepare the data by downloading the M5 dataset and placing it in the `/data` folder
4. Run the Jupyter notebooks for data processing, model training, and explainability
5. Use the exported CSV files to create Power BI dashboards

## Skills Demonstrated
Hierarchical forecasting, time series analysis, machine learning, explainable AI, data visualization, business intelligence

## License
MIT License
