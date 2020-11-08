
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def diameter(self, root: 'Node') -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root):
        first, second = 0, 0
        for nei in root.children:
            depth = self.dfs(nei)
            if depth > first:
                first, second = depth, first
            elif depth > second:
                second = depth

        self.res = max(self.res, first + second)
        return first + 1


