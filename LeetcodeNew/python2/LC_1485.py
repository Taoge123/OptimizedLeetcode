
class NodeCopy:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class SolutionTony:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        if not root:
            return None

        self.tree = {}
        # self.tree[root] = NodeCopy(root.val)
        self.dfs(root)
        return self.tree[root]

    def dfs(self, node):
        if not node:
            return node

        if node in self.tree:
            return self.tree[node]

        newNode = NodeCopy(node.val)
        self.tree[node] = newNode

        newNode.left = self.dfs(node.left)
        newNode.right = self.dfs(node.right)
        newNode.random = self.dfs(node.random)
        return newNode




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



