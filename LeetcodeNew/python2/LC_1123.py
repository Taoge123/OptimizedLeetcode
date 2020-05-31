"""
https://www.youtube.com/watch?v=7KAxl9TxcQE
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
Solution 2: Get Subtree Deepest Depth
helper function return the deepest depth of descendants.
deepest represent the deepest depth.
We use a global variable lca to represent the result.
One pass, Time O(N) Space O(H)

  1 
 2 3 

        1
      2   3
    4

         1
       2   3
      4 5

"""

class Solution:
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
        if left == self.deepest and right == self.deepest:
            self.res = node
        return max(left, right)


"""
Solution 1: Get Subtree Height and LCA
helper function return the subtree height and lca and at the same time.
null node will return depth 0,
leaves will return depth 1.
"""


class Solution:
    def lcaDeepestLeaves(self, root):
        return self.helper(root)[1]

    def helper(self, root):
        if not root:
            return 0, None
        h1, left = self.helper(root.left)
        h2, right = self.helper(root.right)
        if h1 > h2:
            return h1 + 1, left
        if h1 < h2:
            return h2 + 1, right
        return h1 + 1, root
