# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def isBalanced(self, root: TreeNode) -> bool:

#         self.flag = True
#         self.post(root)
#         return self.flag

#     def post(self, root):

#         if not root:
#             return True

#         left = self.post(root.left)
#         right = self.post(root.right)

#         if abs(left - right) > 1:
#             self.flag = False
#             return -1

#         return max(left, right) + 1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.helper(root) != -1

    def helper(self, root):
        if not root:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        if left == -1 or right == -1 or abs(right - left) > 1:
            return -1

        return max(left, right) + 1









