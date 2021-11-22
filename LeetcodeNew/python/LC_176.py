


"""

-> missing null check

select salary as SecondHighestSalary
from Employee
order by salary desc
limit 1 offset 1



select
    IFNULL(
        (select distinct salary
        from Employee
        order by salary desc
        limit 1 offset 1),
        NULL)  as SecondHighestSalary

"""




