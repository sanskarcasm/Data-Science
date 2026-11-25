import pandas as pd

def compute_churn_flag(fact_orders: pd.DataFrame) -> pd.DataFrame:
    cust_order_counts = fact_orders.groupby('customer_id')['order_id'].nunique().reset_index(name='order_count')
    cust_order_counts['churn'] = cust_order_counts['order_count'].apply(lambda x: 1 if x == 1 else 0)
    return cust_order_counts

def calculate_delivery_delay(fact_orders: pd.DataFrame) -> pd.DataFrame:
    fact_orders['order_delivered_customer_date'] = pd.to_datetime(fact_orders['order_delivered_customer_date'], errors='coerce')
    fact_orders['order_estimated_delivery_date'] = pd.to_datetime(fact_orders['order_estimated_delivery_date'], errors='coerce')
    fact_orders['delivery_delay_days'] = (fact_orders['order_delivered_customer_date'] - fact_orders['order_estimated_delivery_date']).dt.days
    return fact_orders

def calculate_revenue_metrics(fact_orders: pd.DataFrame) -> pd.DataFrame:
    fact_orders['total_revenue'] = fact_orders['price'] + fact_orders['freight_value']
    cust_revenue = fact_orders.groupby('customer_id').agg(
        total_revenue=('total_revenue', 'sum'),
        avg_order_value=('total_revenue', 'mean'),
        order_count=('order_id', 'nunique')
    ).reset_index()
    return cust_revenue
