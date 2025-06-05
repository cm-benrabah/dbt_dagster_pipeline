-- models/dimensions/dim_customers.sql

with raw as (
    select
        customer_id,
        -- Suppose your CSV had a single “name” column like 'John Smith'.
        -- You can split it into first/last, or just alias it:
        split_part(name, ' ', 1) as first_name,
        split_part(name, ' ', 2) as last_name,
        email,
        signup_date       as registration_date --,country           as country_code
    from {{ ref('raw_customers') }}
)

select * from raw

