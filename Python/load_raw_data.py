import pandas as pd
from sqlalchemy import create_engine
import os

def main():
    DB_URL = os.getenv("DB_URL", "postgresql://dwh_user:dwh_password@localhost:5432/dwh_db")
    engine = create_engine(DB_URL)

    customers_df = pd.read_csv("/data/customers.csv")
    orders_df = pd.read_csv("/data/orders.csv")

    customers_df.columns = [c.lower().replace(" ", "_") for c in customers_df.columns]
    orders_df.columns = [c.lower().replace(" ", "_") for c in orders_df.columns]

    customers_df.to_sql("raw_customers", engine, schema="raw", if_exists="replace", index=False)
    orders_df.to_sql("raw_orders", engine, schema="raw", if_exists="replace", index=False)

if __name__ == "__main__":
    main()
