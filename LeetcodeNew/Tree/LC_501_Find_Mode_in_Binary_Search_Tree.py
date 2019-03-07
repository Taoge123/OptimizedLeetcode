
"""
For example:
Given BST [1,null,2,2],

   1
    \
     2
    /
   2


return [2].

"""
import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        def dfs(node):
            if node:
                cnt[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        cnt = collections.Counter()
        dfs(root)
        mx = max(cnt.values() or [0])
        return [k for k, v in cnt.items() if v == mx]


class Solution1:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}

        def DFS(node):
            if node:
                count[node.val] = count.get(node.val, 0) + 1
                DFS(node.left)
                DFS(node.right)

        if not root:
            return []

        DFS(root)
        most_frequent = max(count.values())

        res = [n for n, f in count.items() if f == most_frequent]

        return res












