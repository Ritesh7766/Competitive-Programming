# Write your MySQL query statement below
select a.id
from Weather as a, Weather as b
where a.recordDate = b.recordDate + interval 1 day
and a.temperature > b.temperature;