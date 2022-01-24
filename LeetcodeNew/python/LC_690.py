
class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


import collections


class SolutionTony:
    def getImportance(self, employees, id: int) -> int:

        graph = collections.defaultdict(list)
        values = collections.defaultdict(int)

        for employee in employees:
            u, v, vals = employee.id, employee.importance, employee.subordinates
            for val in vals:
                graph[u].append(val)
            values[u] = v

        def dfs(node):
            self.res += values[node]
            for nei in graph[node]:
                dfs(nei)

        self.res = 0
        dfs(id)
        return self.res



class Solution:
    def getImportance(self, employees, id: int) -> int:

        table = {}
        for employee in employees:
            table[employee.id] = employee
        return self.helper(table, id)

    def helper(self, table, rootId):
        root = table[rootId]
        total = root.importance
        for subordinate in root.subordinates:
            total += self.helper(table, subordinate)
        return total






