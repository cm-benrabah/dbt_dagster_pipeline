from dagster_dbt import load_assets_from_dbt_project

dbt_assets = load_assets_from_dbt_project(
    project_dir="/dbt_project/local_dwh",
    profiles_dir="/root/.dbt",
)
