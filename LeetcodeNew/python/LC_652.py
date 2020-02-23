import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode):
        table = collections.defaultdict(list)
        self.dfs(root, table)
        return [table[val][0] for val in table if len(table[val]) > 1]

    def dfs(self, root, table):
        if not root:
            return "null"
        left = self.dfs(root.left, table)
        right = self.dfs(root.right, table)
        val = "%s,%s,%s" % (str(root.val), left, right)
        table[val].append(root)
        return val



