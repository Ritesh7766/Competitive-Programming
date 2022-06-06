# Write your MySQL query statement below
with max_salary(value) as (
    select max(salary)
    from Employee
), sub_set(id, salary) as (
    select id, salary
    from Employee, max_salary
    where salary <> max_salary.value
)
select max(salary) as SecondHighestSalary
from sub_set;