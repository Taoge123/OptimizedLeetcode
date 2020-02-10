"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        self.preorder(root, res)
        return res

    def preorder(self, root, res):
        if not root:
            return None

        res.append(root.val)
        self.preorder(root.left, res)
        self.preorder(root.right, res)

class Solution1:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return None

        stack, res = [root], []

        while stack:
            node = stack.pop()
            # print(node)
            if isinstance(node, int):
                res.append(node)
                continue

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            stack.append(node.val)

        return res


class Solution2:
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





