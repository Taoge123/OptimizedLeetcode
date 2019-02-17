# Definition for a binary tree node.
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

        left  = self.helper(root.left, ret)
        right = self.helper(root.right, ret)
        level = max(left, right) + 1

        #level need to touch the bottom
        if level > len(ret):
            ret.append([])
        ret[level-1].append(root.val)
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


# 利用分制，每次bottom up的时候返回当前叶子节点的高度，然后在相对应的全球数组里面开辟数组，并且往里面增值。
class Solution3:
    def findLeaves(self, root):
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root: return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        height = max(left, right) + 1

        if len(self.res) < height:
            self.res.append([])
        self.res[height - 1].append(root.val)
        return height


