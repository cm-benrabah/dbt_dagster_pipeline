# -*- coding: utf-8 -*-
"""
Created on Sun Jun  1 15:51:41 2025

@author: cm_be
"""

from faker import Faker
import random
import pandas as pd
from datetime import datetime, timedelta

fake = Faker()

# Parameters
num_customers = 500
num_products = 100
num_orders = 1000
max_items_per_order = 5

# Generate customers
customers = [
    {
        'customer_id': i,
        'name': fake.name(),
        'email': fake.email(),
        'signup_date': fake.date_between(start_date='-3y', end_date='today')
    }
    for i in range(1, num_customers + 1)
]

# Generate products
products = [
    {
        'product_id': i,
        'name': fake.word().capitalize(),
        'category': fake.random_element(elements=('Electronics', 'Books', 'Clothing', 'Home', 'Sports')),
        'price': round(random.uniform(5.0, 500.0), 2)
    }
    for i in range(1, num_products + 1)
]

# Generate orders
orders = []
order_items = []

for i in range(1, num_orders + 1):
    cust_id = random.randint(1, num_customers)
    order_date = fake.date_between(start_date='-2y', end_date='today')
    orders.append({
        'order_id': i,
        'customer_id': cust_id,
        'order_date': order_date,
        'shipping_address': fake.address().replace('\n', ', ')
    })
    
    for _ in range(random.randint(1, max_items_per_order)):
        product = random.choice(products)
        quantity = random.randint(1, 4)
        order_items.append({
            'order_id': i,
            'product_id': product['product_id'],
            'quantity': quantity,
            'unit_price': product['price'],
            'total_price': round(product['price'] * quantity, 2)
        })
import os
print("Current working directory:", os.getcwd())

# Save to CSV
pd.DataFrame(customers).to_csv('../dbtlearn/seeds/raw_customers.csv', index=False)
pd.DataFrame(products).to_csv('../dbtlearn/seeds/raw_products.csv', index=False)
pd.DataFrame(orders).to_csv('../dbtlearn/seeds/raw_orders.csv', index=False)
pd.DataFrame(order_items).to_csv('../dbtlearn/seeds/raw_order_items.csv', index=False)
