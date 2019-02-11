class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorderTraversal(self, root):

        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            if isinstance(node, int):
                ans.append(node)
                continue



            if node.right:  # if has right node, push into stack
                stack.append(node.right)


            if node.left:  # if has left node, push into stack
                stack.append(node.left)
            stack.append(node.val)  # Push VALUE into stack, in between left and right

        return ans
