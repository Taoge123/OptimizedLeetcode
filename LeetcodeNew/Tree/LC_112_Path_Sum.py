
"""
https://leetcode.com/problems/path-sum/discuss/158326/Python-DFS-or-tm
"""

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.flag = False

    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.left and not root.right and sum - root.val == 0: self.flag = True
        self.hasPathSum(root.left, sum - root.val)
        self.hasPathSum(root.right, sum - root.val)
        return self.flag


#每次往下传sum - root.val，分制返回值为True或者False

class Solution2:
    def hasPathSum(self, root, sum):
        return self.dfs(root, sum)

    def dfs(self, root, sum):
        if not root: return False
        if not root.left and not root.right and sum - root.val == 0: return True
        left = self.dfs(root.left, sum - root.val)
        right = self.dfs(root.right, sum - root.val)
        return left or right


class Solution3:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)



class Solution4:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False


# DFS Recursively
def hasPathSum1(self, root, sum):
    res = []
    self.dfs(root, sum, res)
    return any(res)


def dfs(self, root, target, res):
    if root:
        if not root.left and not root.right:
            if root.val == target:
                res.append(True)
        if root.left:
            self.dfs(root.left, target - root.val, res)
        if root.right:
            self.dfs(root.right, target - root.val, res)


# DFS with stack
def hasPathSum2(self, root, sum):
    if not root:
        return False
    stack = [(root, root.val)]
    while stack:
        curr, val = stack.pop()
        if not curr.left and not curr.right:
            if val == sum:
                return True
        if curr.right:
            stack.append((curr.right, val + curr.right.val))
        if curr.left:
            stack.append((curr.left, val + curr.left.val))
    return False


# BFS with queue
def hasPathSum(self, root, sum):
    if not root:
        return False
    queue = [(root, sum - root.val)]
    while queue:
        curr, val = queue.pop(0)
        if not curr.left and not curr.right:
            if val == 0:
                return True
        if curr.left:
            queue.append((curr.left, val - curr.left.val))
        if curr.right:
            queue.append((curr.right, val - curr.right.val))
    return False