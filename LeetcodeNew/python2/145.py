
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def postorderTraversal(self, root: TreeNode) -> List[int]:

#         res = []
#         self.postorder(root, res)
#         return res

#     def postorder(self, root, res):
#         if not root:
#             return None

#         self.postorder(root.left, res)
#         self.postorder(root.right, res)
#         res.append(root.val)

class Solution:
    def postorderTraversal(self, root: TreeNode):
        if not root:
            return None

        stack, res = [root], []

        while stack:
            cur = stack.pop()

            if isinstance(cur, int):
                res.append(cur)
                continue

            stack.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)


        return res








