"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def inorderTraversal(self, root):
#         if not root:
#             return None

#         stack, res = [root], []

#         while stack:
#             cur = stack.pop()
#             if isinstance(cur, int):
#                 res.append(cur)
#                 continue

#             if cur.right:
#                 stack.append(cur.right)

#             stack.append(cur.val)

#             if cur.left:
#                 stack.append(cur.left)

#         return res





class Solution:
    def inorderTraversal(self, root):

        stack, res = [], []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res










# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:

#         stack, res = [], []
#         cur = root

#         while cur or stack:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left

#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right

#         return res




# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.inorder(root, res)
#         return res

#     def inorder(self, root, res):
#         if not root:
#             return None
#         self.inorder(root.left, res)
#         res.append(root.val)
#         self.inorder(root.right, res)











