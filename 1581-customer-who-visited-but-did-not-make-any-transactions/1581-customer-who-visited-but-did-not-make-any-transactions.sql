# Write your MySQL query statement below
select customer_id, count(Visits.visit_id) as count_no_trans
from Visits natural left join Transactions
where transaction_id is NULL
group by customer_id;