
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root, target):

        return self.dfs(root, target)

    def dfs(self, node, target):
        if not node:
            return None

        node.left = self.dfs(node.left, target)
        node.right = self.dfs(node.right, target)

        if node.val == target and not node.left and not node.right:
            return None

        return node


