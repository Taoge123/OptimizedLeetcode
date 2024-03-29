
"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Example 1:

Input: [1,1,1,1,1,null,1]
Output: true
Example 2:

Input: [2,2,2,5,2]
Output: false

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root):
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1



class Solution2:
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct


class SolutionLee:
    def isUnivalTree(self, root):
        def dfs(node):
            return not node or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)


class SolutionBFS:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a = set()
        def judge(node):
            a.add(node.val)
            if node.left :
                judge(node.left)
            if node.right :
                judge(node.right)
        judge(root)
        if len(a)>1:
            return False
        else:
            return True


