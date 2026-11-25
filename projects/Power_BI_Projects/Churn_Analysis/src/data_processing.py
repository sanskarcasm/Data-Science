import pandas as pd

def load_raw_data():
    customers = pd.read_csv("data/olist_customers_dataset.csv")
    geolocation = pd.read_csv("data/olist_geolocation_dataset.csv")
    order_items = pd.read_csv("data/olist_order_items_dataset.csv")
    order_payments = pd.read_csv("data/olist_order_payments_dataset.csv")
    order_reviews = pd.read_csv("data/olist_order_reviews_dataset.csv")
    orders = pd.read_csv("data/olist_orders_dataset.csv")
    products = pd.read_csv("data/olist_products_dataset.csv")
    sellers = pd.read_csv("data/olist_sellers_dataset.csv")
    categories = pd.read_csv("data/product_category_name_translation.csv")
    return customers, geolocation, order_items, order_payments, order_reviews, orders, products, sellers, categories

def create_dimensions(customers, geolocation, products, categories, sellers, orders):
    dim_customers = customers[['customer_id', 'customer_unique_id', 'customer_zip_code_prefix', 'customer_city', 'customer_state']].drop_duplicates()
    dim_sellers = sellers[['seller_id', 'seller_zip_code_prefix', 'seller_city', 'seller_state']].drop_duplicates()
    dim_products = products.merge(categories, how='left', on='product_category_name')
    dim_products = dim_products[['product_id', 'product_category_name_english', 
                                 'product_name_lenght', 'product_description_lenght', 
                                 'product_photos_qty', 'product_weight_g', 
                                 'product_length_cm', 'product_height_cm', 'product_width_cm']].drop_duplicates()
    dim_geolocation = geolocation.groupby(['geolocation_zip_code_prefix', 'geolocation_city', 'geolocation_state']).first().reset_index()
    dim_date = pd.DataFrame()
    dim_date['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
    dim_date['order_id'] = orders['order_id']
    dim_date['year'] = dim_date['order_purchase_timestamp'].dt.year
    dim_date['month'] = dim_date['order_purchase_timestamp'].dt.month
    dim_date['day'] = dim_date['order_purchase_timestamp'].dt.day
    dim_date['weekday'] = dim_date['order_purchase_timestamp'].dt.day_name()
    return dim_customers, dim_sellers, dim_products, dim_geolocation, dim_date

def create_fact_table(orders, order_items, order_payments, order_reviews):
    fact_orders = orders.merge(order_items, on='order_id', how='left') \
                        .merge(order_payments, on='order_id', how='left') \
                        .merge(order_reviews[['order_id','review_score']], on='order_id', how='left')
    fact_orders = fact_orders[['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp',
                               'order_approved_at', 'order_delivered_carrier_date',
                               'order_delivered_customer_date', 'order_estimated_delivery_date',
                               'product_id', 'seller_id', 'price', 'freight_value',
                               'payment_type', 'payment_value', 'review_score']]
    fact_orders = fact_orders.drop_duplicates()
    return fact_orders

def save_star_schema(dim_customers, dim_sellers, dim_products, dim_geolocation, dim_date, fact_orders):
    dim_customers.to_csv("data/cleaned/dim_customers.csv", index=False)
    dim_sellers.to_csv("data/cleaned/dim_sellers.csv", index=False)
    dim_products.to_csv("data/cleaned/dim_products.csv", index=False)
    dim_geolocation.to_csv("data/cleaned/dim_geolocation.csv", index=False)
    dim_date.to_csv("data/cleaned/dim_date.csv", index=False)
    fact_orders.to_csv("data/cleaned/fact_orders.csv", index=False)
    print("✅ Star schema tables created and saved in data/cleaned!")

if __name__ == "__main__":
    customers, geolocation, order_items, order_payments, order_reviews, orders, products, sellers, categories = load_raw_data()
    dim_customers, dim_sellers, dim_products, dim_geolocation, dim_date = create_dimensions(customers, geolocation, products, categories, sellers, orders)
    fact_orders = create_fact_table(orders, order_items, order_payments, order_reviews)
    save_star_schema(dim_customers, dim_sellers, dim_products, dim_geolocation, dim_date, fact_orders)
