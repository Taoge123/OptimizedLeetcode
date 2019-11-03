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


Usually when we do DFS, we pop a node from stack and push back its left
and right child. But we lose the information of the order.
To keep track of the order, we can push back into stack right-child,
current node, and left-child, so when we are done with left child (sub-tree),
we know who's its father. To avoid process the same node twice,
we push the VALUE of the current node to stack, instead of the node itself.
This way, every time we saw a number in the stack,
we know we are done with a left sub-tree and this number is what's in order.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal1(self, root):
        if not root:
            return None

        stack, res = [root], []

        while stack:
            cur = stack.pop()
            if isinstance(cur, int):
                res.append(cur)
                continue

            if cur.right:
                stack.append(cur.right)

            stack.append(cur.val)

            if cur.left:
                stack.append(cur.left)

        return res


    def inorderTraversal2(self, root):

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

    def inorderTraversal3(self, root):

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


    def inorderTraversal4(self, root):
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if not root:
            return None
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)

