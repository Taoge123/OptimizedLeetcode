class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
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
            stack.append(node.val)  # Push VALUE into stack, in between left and right
            if node.left:  # if has left node, push into stack
                stack.append(node.left)
        return ans

    def preorderTraversal(self, root):

        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            print(type(node))
            if isinstance(node, int):
                ans.append(node)
                continue
            if node.right:  # if has right node, push into stack
                stack.append(node.right)
            if node.left:  # if has left node, push into stack
                stack.append(node.left)
            stack.append(node.val)  # Push VALUE into stack, in between left and right
        return ans

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



tree = TreeNode(1)
tree.left = None
tree.right = TreeNode(2)
tree.right.left = TreeNode(3)

a = Solution()

print(a.preorderTraversal(tree))


