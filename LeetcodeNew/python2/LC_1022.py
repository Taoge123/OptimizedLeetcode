
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class SolutionRika:
    def sumRootToLeaf(self, root):

        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, summ):
        if not node:
            return 0
        summ = (summ << 1) + node.val
        if node and not node.left and not node.right:
            self.res += summ
        self.dfs(node.left, summ)
        self.dfs(node.right, summ)




class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.dfs(root, 0)


    def dfs(self, root, res):
        if not root:
            return 0

        res = res * 2 + root.val

        left = self.dfs(root.left, res)
        right = self.dfs(root.right, res)

        if root.left == None and root.right == None:
            return res

        else:
            return left + right





