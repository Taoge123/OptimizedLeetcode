
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:

        if not root:
            return None

        if root.val == target and not root.left and not root.right:
            return None

        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)


        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
root.right.right = TreeNode(4)

target = 2
a = Solution()
print(a.removeLeafNodes(root, target))




