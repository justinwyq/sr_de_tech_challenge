---- there are 2 ways to interpret this question:

-- A. if frequency is defined as total item quantity

with total_item_quantity as (
    select item_id
        , sum(item_quantity) as total_item_quantity
    from transaction_items
    group by 1
    order by 2 desc
)

select *
from total_item_quantity
limit 3;


-- B. if frequency is defined as how many members bought it

with total_members_purchasing as (
    select item_id
        , count(distinct membership_id) as number_members
    from transaction_items
    group by 1
    order by 2 desc
)

select *
from total_members_purchasing
limit 3;