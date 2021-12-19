"""
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

Example :

Input:  root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

Output: 4
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return self.res
        self.helper(root)
        return self.res

    def helper(self, root):
        if not root:
            return True

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left and right:
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False

            self.res += 1
            return True

        return False


class Solution1:
    def countUnivalSubtrees(self, root) -> int:
        self.count = 0
        self.dfs(root)
        return self.count

    def dfs(self, root):
        if not root:
            return True

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left and right and (not root.left or root.val == root.left.val) \
                and (not root.right or root.val == root.right.val):
            self.count += 1
            return True

        return False


class Solution2:
    def countUnivalSubtrees(self, root) -> int:
        self.res = 0
        self.dfs(root, -1)
        return self.res

    def dfs(self, root, prev):
        if not root:
            return True

        left = self.dfs(root.left, root.val)
        right = self.dfs(root.right, root.val)
        # print(left, right, root.val, prev)
        if not left or not right:
            return False
        else:
            self.res += 1
        return root.val == prev



root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(5)
root.right.right = TreeNode(5)

a = SolutionTest()
print(a.countUnivalSubtrees(root))

