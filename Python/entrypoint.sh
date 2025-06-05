#!/bin/bash
set -e

echo "Running your Python script..."
cd /dbt_dagster_pipeline/Python
python ./seeds_creation.py

echo "Running dbt seed from mounted dbtlearn project..."
cd /dbt_dagster_pipeline/dbtlearn
dbt seed

echo "Launching Dagster..."
cd /dbt_dagster_pipeline/dbt_dagster_project 

dagster dev -h 0.0.0.0 -p 3000

