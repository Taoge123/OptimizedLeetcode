
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        self.visited = {}
        return self.dfs(root)

    def dfs(self, root):
        if not root:
            return None
        if root in self.visited:
            return self.visited[root]

        node = NodeCopy(root.val, None, None, None)
        self.visited[root] = node

        node.left = self.dfs(root.left)
        node.right = self.dfs(root.right)
        node.random = self.dfs(root.random)

        return node



