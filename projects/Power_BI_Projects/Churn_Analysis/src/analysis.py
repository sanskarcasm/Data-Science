import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

os.makedirs("reports", exist_ok=True)

def plot_order_distribution(cust_order_counts: pd.DataFrame):
    sns.histplot(cust_order_counts['order_count'], bins=30)
    plt.title('Customer Order Frequency')
    plt.xlabel('Number of Orders')
    plt.ylabel('Number of Customers')
    plt.show()
    plt.savefig("reports/order_distribution.png", bbox_inches='tight', dpi=300)
    plt.close

def plot_delivery_delay_distribution(fact_orders: pd.DataFrame):
    valid_delays = fact_orders.dropna(subset=['delivery_delay_days'])
    sns.histplot(valid_delays['delivery_delay_days'], bins=50)
    plt.title('Delivery Delay Distribution (Days)')
    plt.xlabel('Days Delay')
    plt.ylabel('Count')
    plt.show()
    plt.savefig("reports/delivery_delay_distribution.png", bbox_inches='tight', dpi=300)
    plt.close


def plot_review_vs_delay(fact_orders: pd.DataFrame):
    valid_data = fact_orders.dropna(subset=['delivery_delay_days', 'review_score'])
    sns.boxplot(x='review_score', y='delivery_delay_days', data=valid_data)
    plt.title('Delivery Delay by Review Score')
    plt.xlabel('Review Score')
    plt.ylabel('Delivery Delay (Days)')
    plt.show()
    plt.savefig("reports/review_vs_delay.png", bbox_inches='tight', dpi=300)
    plt.close


def plot_clv_by_churn(cust_order_counts: pd.DataFrame, cust_revenue: pd.DataFrame):
    print("cust_order_counts columns:", cust_order_counts.columns)
    print("cust_revenue columns:", cust_revenue.columns)
    merged = pd.merge(cust_order_counts, cust_revenue, on='customer_id', suffixes=('_orders', '_revenue'))
# Use the order count column from the orders DataFrame for churn flag
    merged['churn'] = merged['order_count_orders'].apply(lambda x: 1 if x == 1 else 0)
    sns.boxplot(x='churn', y='total_revenue', data=merged)
    plt.title('Customer Lifetime Value by Churn Status (1=Churn, 0=Retained)')
    plt.xlabel('Churn Status')
    plt.ylabel('Total Revenue (CLV)')
    plt.show()
    plt.savefig("reports/clv_by_churn.png", bbox_inches='tight', dpi=300)
    plt.close


def plot_revenue_by_category(fact_orders: pd.DataFrame, dim_products: pd.DataFrame):
    fact_with_cat = fact_orders.merge(dim_products[['product_id', 'product_category_name_english']], on='product_id')
    cat_revenue = fact_with_cat.groupby('product_category_name_english')['total_revenue'].sum().sort_values(ascending=False)
    plt.figure(figsize=(12,6))
    sns.barplot(x=cat_revenue.index, y=cat_revenue.values)
    plt.xticks(rotation=90)
    plt.title('Revenue by Product Category')
    plt.xlabel('Product Category')
    plt.ylabel('Total Revenue')
    plt.show()
    plt.savefig("reports/revenue_by_category_distribution.png", bbox_inches='tight', dpi=300)
    plt.close

