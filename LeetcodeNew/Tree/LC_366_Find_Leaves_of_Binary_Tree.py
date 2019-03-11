
"""
Example:

Input: [1,2,3,4,5]

          1
         / \
        2   3
       / \
      4   5

Output: [[4,5,3],[2],[1]]

"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        self.helper(root, ret)
        return ret

    def helper(self, root, ret):
        if not root: return 0

        left = self.helper(root.left, ret)
        right = self.helper(root.right, ret)
        level = max(left, right) + 1

        if level > len(ret):
            ret.append([])
        ret[level - 1].append(root.val)

        return level


class Solution2:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.output = []
        while root:
            self.output.append([])
            root = self.getLeaves(root)
        return self.output

    def getLeaves(self, root):
        if root.left == None and root.right == None:
            self.output[-1].append(root.val)
            return None

        if root.left:
            root.left = self.getLeaves(root.left)

        if root.right:
            root.right = self.getLeaves(root.right)

        return root

class Solution3:
    def findLeaves(self, root):
        def order(root, dic):
            if not root:
                return 0
            left = order(root.left, dic)
            right = order(root.right, dic)
            lev = max(left, right) + 1
            dic[lev] += root.val,
            return lev
        dic, ret = collections.defaultdict(list), []
        order(root, dic)
        for i in range(1, len(dic) + 1):
            ret.append(dic[i])
        return ret













