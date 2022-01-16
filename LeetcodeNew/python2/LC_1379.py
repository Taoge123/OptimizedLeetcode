
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        cache = {}
        self.dfs(original, cloned, cache)
        return cache[target]

    def dfs(self, original, cloned, cache):
        if not original and not cloned:
            return None

        cache[original] = cloned
        self.dfs(original.left, cloned.left, cache)
        self.dfs(original.right, cloned.right, cache)




