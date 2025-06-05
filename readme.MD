# Dagster + dbt Data Pipeline

This project demonstrates how to orchestrate a data transformation pipeline using **Dagster** and **dbt**, with data stored in **PostgreSQL**.

## 📦 Project Overview

- **dbt** is used to:
  - Seed raw data
  - Transform raw tables into dimensional and fact tables
  - Create analytical summaries
- **Dagster** orchestrates the dbt models as assets
- **PostgreSQL** serves as the database backend

## 🛠 Components

- **dbt models**:
  - `raw_customers`, `raw_orders`, `raw_order_items`, `raw_products`
  - `dim_customers`, `fct_orders`
  - `analysis_customer_order_summary`
  
- **Dagster job**: `materialize_dbt_models`
  - Runs dbt seed and model transformations
  - Materializes assets based on dbt models

## 🖥 Local Execution

To run Dagster on your local machine:

```bash
dagster dev -h 0.0.0.0 -p 3000
