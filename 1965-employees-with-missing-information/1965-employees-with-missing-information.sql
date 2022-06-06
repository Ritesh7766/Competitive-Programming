# Write your MySQL query statement below
select employee_id
from Employees natural left join Salaries
where salary is NULL
union
select employee_id
from Employees natural right join Salaries
where name is NULL
order by employee_id;