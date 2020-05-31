
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        self.dfs(root, inorder)
        return self.buildBST(inorder)

    def buildBST(self, inorder):
        if not inorder:
            return None

        mid = (len(inorder)) // 2
        root = TreeNode(inorder[mid])
        root.left = self.buildBST(inorder[:mid])
        root.right = self.buildBST(inorder[mid + 1:])
        return root

    def dfs(self, root, res):
        if not root:
            return None
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)





