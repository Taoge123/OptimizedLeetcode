"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3


Note:
Bonus points if you could solve it both recursively and iteratively.

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        if p and q:
            return p.val == q.val \
                   and self.dfs(p.left, q.right) \
                   and self.dfs(p.right, q.left)

        return p == q


class SolutionTony:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.dfs(root.left, root.right)

    def dfs(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2:
            return False

        if root1.val != root2.val:
            return False
        return root1.val == root2.val and self.dfs(root1.left, root2.right) and self.dfs(root1.right, root2.left)




