# Write your MySQL query statement below
with first_max(dept_name, salary) as (
    select Department.name, max(salary) as first_max
    from Employee join Department
    on Employee.departmentId = Department.id
    group by departmentId
), second_max(dept_name, salary) as (
    select Department.name, max(Employee.salary) as second_max
    from Employee join Department
    on Employee.departmentId = Department.id, first_max
    where first_max.dept_name = Department.name and Employee.salary <> first_max.salary
    group by departmentId
), third_max(dept_name, salary) as (
    select Department.name, max(Employee.salary) as third_max
    from Employee join Department
    on Employee.departmentId = Department.id, first_max, second_max
    where first_max.dept_name = Department.name and Employee.salary <> first_max.salary
    and second_max.dept_name = Department.name and Employee.salary <> second_max.salary
    group by departmentId
) 
select Department.name as Department, Employee.name as Employee, Employee.salary
from Employee join Department
on Employee.departmentId = Department.id 
left join first_max on first_max.dept_name = Department.name
left join second_max on second_max.dept_name = Department.name
left join third_max on third_max.dept_name = Department.name
where Employee.salary = first_max.salary
or Employee.salary = second_max.salary
or Employee.salary = third_max.salary;
