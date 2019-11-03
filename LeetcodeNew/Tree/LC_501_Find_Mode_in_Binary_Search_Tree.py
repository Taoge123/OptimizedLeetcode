
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
    def findMode(self, root: TreeNode):
        cache = collections.defaultdict(int)
        self.max = -1
        self.inorder(root, cache)
        return [k for k, v in cache.items() if v == self.max]

    def inorder(self, root, cache):
        if not root:
            return
        cache[root.val] += 1
        self.max = max(self.max, cache[root.val])
        self.inorder(root.left, cache)
        self.inorder(root.right, cache)










