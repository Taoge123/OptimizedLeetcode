

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ''
        res = [None]
        self.dfs(root, '', res)
        return res[0]

    def dfs(self, root, path, res):
        path = path + chr(ord('a') + root.val)
        if not root.left and not root.right:
            if res[0] == None:
                res[0] = path[::-1]
            else:
                res[0] = min(res[0], path[::-1])
        if root.left:
            self.dfs(root.left, path, res)
        if root.right:
            self.dfs(root.right, path, res)



root = TreeNode(4)
root.left = TreeNode(0)
root.left.left = TreeNode(1)
root.right = TreeNode(1)

a = Solution()
print(a.smallestFromLeaf(root))
