"""
Complexity
Both solution are one pass.
Time O(N) for one pass
Space O(H) for recursion management


Solution 1: Get Subtree Height and LCA
helper function return the subtree height and lca and at the same time.
null node will return depth 0,
leaves will return depth 1.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, None
        h1, lca1 = self.helper(root.left)
        h2, lca2 = self.helper(root.right)
        if h1 > h2:
            return h1 + 1, lca1
        if h1 < h2:
            return h2 + 1, lca2
        return h1 + 1, root



class Solution2:
    def __init__(self):
        self.res = None
        self.deepest = 0

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        self.helper(root, 0)
        return self.res

    def helper(self, node, depth):
        self.deepest = max(self.deepest, depth)
        if not node:
            return depth
        left = self.helper(node.left, depth + 1)
        right = self.helper(node.right, depth + 1)
        if left == right == self.deepest:
            self.res = node
        return max(left, right)





