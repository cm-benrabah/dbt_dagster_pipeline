-- models/analysis/analysis_customer_order_summary.sql
-- Calculates total orders and total amount spent per customer.

WITH customer_orders AS (
    SELECT
        c.customer_id,
        c.first_name,
        c.last_name,
        c.email,
        c.registration_date,
        --c.country_code,
        COUNT(o.order_id) AS total_orders,
        SUM(o.total_amount) AS total_amount_spent
    FROM
        {{ ref(	"dim_customers") }} c
    LEFT JOIN
        {{ ref(	"fct_orders") }} o ON c.customer_id = o.customer_id
    GROUP BY
        c.customer_id,
        c.first_name,
        c.last_name,
        c.email,
        c.registration_date --,c.country_code
)

SELECT
    customer_id,
    first_name,
    last_name,
    email,
    registration_date,
    --country_code,
    COALESCE(total_orders, 0) AS total_orders,
    COALESCE(total_amount_spent, 0) AS total_amount_spent
FROM
    customer_orders
ORDER BY
    total_amount_spent DESC