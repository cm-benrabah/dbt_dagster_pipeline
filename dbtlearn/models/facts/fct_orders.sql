-- models/facts/fct_orders.sql

with
  orders_raw as (
    select
      order_id,
      customer_id,
      order_date
    from {{ ref('raw_orders') }}
  ),

  items_raw as (
    select
      order_id,
      sum(total_price) as total_amount
    from {{ ref('raw_order_items') }}
    group by order_id
  )

select
  o.order_id,
  o.customer_id,
  o.order_date,
  i.total_amount
from orders_raw o
left join items_raw i
  on o.order_id = i.order_id
