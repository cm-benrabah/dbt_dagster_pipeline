from dagster import Definitions
from .assets import dbt_assets

defs = Definitions(assets=[dbt_assets])
