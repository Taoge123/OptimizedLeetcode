
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:

#         res = []
#         self.preorder(root, res)
#         return res

#     def preorder(self, root, res):
#         if not root:
#             return None

#         res.append(root.val)
#         self.preorder(root.left, res)
#         self.preorder(root.right, res)

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         if not root:
#             return None

#         stack, res = [root], []

#         while stack:
#             node = stack.pop()
#             # print(node)
#             if isinstance(node, int):
#                 res.append(node)
#                 continue

#             if node.right:
#                 stack.append(node.right)
#             if node.left:
#                 stack.append(node.left)

#             stack.append(node.val)

#         return res


class Solution:
    def preorderTraversal(self, root):

        if not root:
            return None

        stack, res = [root], []

        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
                res.append(cur.val)
        return res














