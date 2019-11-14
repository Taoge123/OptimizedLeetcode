
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def hasPathSum(self, root: TreeNode, sum: int) -> bool:
#         if not root:
#             return False

#         if not root.left and not root.right:
#             return root.val == sum

#         return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [root]

        while stack:
            node = stack.pop()
            print(node.val)
            if not node.left and not node.right:
                if node.val == sum:
                    return True

            if node.left:
                node.left.val += node.val
                stack.append(node.left)

            if node.right:
                node.right.val += node.val
                stack.append(node.right)

        return False



