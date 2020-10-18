
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        path1 = []
        path2 = []
        self.helper(root1, path1)
        self.helper(root2, path2)

        if len(path1) != len(path2):
            return False

        # optimization
        # return path1 == path2 directely also works
        for i in range(len(path1)):
            if path1[i] != path2[i]:
                return False
        return True

    def helper(self, root, path):
        if not root:
            return

        if not root.left and not root.right:
            path.append(root.val)

        self.helper(root.left, path)
        self.helper(root.right, path)




