with grouped_members as (
    select membership_id
        , sum(subtotal_price) as total_spending
    from transaction_items
    group by 1
    order by 2 desc
)

select *
from grouped_members
limit 10