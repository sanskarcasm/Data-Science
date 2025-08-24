from data_processing import load_raw_data, create_dimensions, create_fact_table, save_star_schema
from feature_engineering import compute_churn_flag, calculate_delivery_delay, calculate_revenue_metrics
from analysis import plot_order_distribution, plot_delivery_delay_distribution, plot_review_vs_delay, plot_clv_by_churn, plot_revenue_by_category

def main():
    # Step 1: Load raw data and create star schema
    customers, geolocation, order_items, order_payments, order_reviews, orders, products, sellers, categories = load_raw_data()
    dim_customers, dim_sellers, dim_products, dim_geolocation, dim_date = create_dimensions(customers, geolocation, products, categories, sellers, orders)
    fact_orders = create_fact_table(orders, order_items, order_payments, order_reviews)
    save_star_schema(dim_customers, dim_sellers, dim_products, dim_geolocation, dim_date, fact_orders)
    
    # Step 2: Feature engineering
    cust_order_counts = compute_churn_flag(fact_orders)
    fact_orders = calculate_delivery_delay(fact_orders)
    cust_revenue = calculate_revenue_metrics(fact_orders)
    
    # Step 3: Analysis and plots
    plot_order_distribution(cust_order_counts)
    plot_delivery_delay_distribution(fact_orders)
    plot_review_vs_delay(fact_orders)
    plot_clv_by_churn(cust_order_counts, cust_revenue)
    plot_revenue_by_category(fact_orders, dim_products)

if __name__ == "__main__":
    main()
