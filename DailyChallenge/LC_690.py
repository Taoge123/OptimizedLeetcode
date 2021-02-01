

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

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

