
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class SolutionTony:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        root = p
        while root.parent:
            root = root.parent

        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root:
            return None

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if root == p or root == q:
            return root
        if left and right:
            return root
        if left or right:
            return left or right
        if not left and not right:
            return None



class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent = set()
        def dfs(node):
            if not node or node in parent:
                return node
            parent.add(node)
            return dfs(node.parent)

        return dfs(p) or dfs(q)



