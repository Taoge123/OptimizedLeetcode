

"""
https://leetcode.com/problems/consecutive-numbers/solution/

Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output:
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+


select distinct l1.num as ConsecutiveNums
from
    logs l1,
    logs l2,
    logs l3
where
    l1.id = l2.id - 1
    and l2.id = l3.id - 1
    and l1.num = l2.num
    and l2.num = l3.num

"""


