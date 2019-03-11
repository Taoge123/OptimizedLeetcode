"""

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates:
employee 2 and employee 3. They both have importance value 3.
So the total importance value of employee 1 is 5 + 3 + 3 = 11.

题目意思就是题目自定了一个数据结构，第一个值为id，第二个值为权重，第三个值为下属
一个公司每个人对应一个数据结构，给你一个人的id，让你返回他以及他的所有下属的权重和。

"""


# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        a = []
        sum = 0
        a.append(id)
        while a:
            id = a[0]

            sum = employees[id - 1][1] + sum
            if employees[id - 1][2]:
                for i in range(len(employees[id - 1][2])):
                    a.append(employees[id - 1][2][i])
            a.remove(id)


class Solution2(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        # Time: O(n)
        # Space: O(n)
        emps = {employee.id: employee for employee in employees}
        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return subordinates_importance + emps[id].importance
        return dfs(id)










