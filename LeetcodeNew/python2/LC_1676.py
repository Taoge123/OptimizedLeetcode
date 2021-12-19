
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionFast:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        self.nodes = set(nodes)
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return None

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if node in self.nodes:
            return node

        if left and right:
            return node
        if left or right:
            return left or right
        if not left and not right:
            return None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        nodes = set(nodes)
        return self.dfs(root, nodes)

    def dfs(self, root, nodes):
        if not root:
            return None
        if root in nodes:
            return root

        left = self.dfs(root.left, nodes)
        right = self.dfs(root.right, nodes)

        if left in nodes and right in nodes:
            return root
        else:
            return left or right




