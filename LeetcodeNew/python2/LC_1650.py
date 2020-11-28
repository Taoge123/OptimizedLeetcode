
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent = set()
        def dfs(node):
            if not node or node in parent:
                return node
            parent.add(node)
            return dfs(node.parent)

        return dfs(p) or dfs(q)



