
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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




