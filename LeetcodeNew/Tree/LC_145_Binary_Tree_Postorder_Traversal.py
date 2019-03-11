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

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            if isinstance(node, int):
                ans.append(node)
                continue

            stack.append(node.val)  # Push VALUE into stack, in between left and right

            if node.right:  # if has right node, push into stack
                stack.append(node.right)

            if node.left:  # if has left node, push into stack
                stack.append(node.left)

        return ans