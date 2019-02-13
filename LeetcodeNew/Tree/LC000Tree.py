class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class SolutionInorder:
    # @param {TreeNode} root
    # @return {integer[]}
    def inorderTraversal(self, root):
        result, stack = [], [(root, False)]

        while stack:
            cur, visited = stack.pop()
            if cur:
                if visited:
                    result.append(cur.val)
                else:
                    stack.append((cur.right, False))
                    stack.append((cur, True))
                    stack.append((cur.left, False))

        return result



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


