# Write your MySQL query statement below
select name
from SalesPerson
where sales_id not in (
    select sales_id
    from Orders natural join Company
    where name = 'RED'
);