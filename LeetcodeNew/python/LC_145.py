"""
Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]
Follow up: Recursive solution is trivial, could you do it iteratively?

"""



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode):

        res = []
        self.postorder(root, res)
        return res

    def postorder(self, root, res):
        if not root:
            return None

        self.postorder(root.left, res)
        self.postorder(root.right, res)
        res.append(root.val)

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




