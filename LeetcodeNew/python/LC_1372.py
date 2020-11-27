"""
Recursive return [left, right, result], where:
left is the maximum length in direction of root.left
right is the maximum length in direction of root.right
result is the maximum length in the whole sub tree.

"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionTonyDFS:
    def longestZigZag(self, root):
        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, node):
        if not node:
            return [-1, -1]
        a, b = self.dfs(node.left)
        c, d = self.dfs(node.right)
        self.max = max(self.max, b + 1, c + 1)
        return [b + 1, c + 1]


class SolutionDFS:
    def longestZigZag(self, root):
        self.max = 0
        self.dfs(root)
        return self.max

    def dfs(self, node):
        if not node:
            return [-1, -1]
        a, b = self.dfs(node.left)
        c, d = self.dfs(node.right)
        self.max = max(self.max, a, b, c, d, b + 1, c + 1)
        return [b + 1, c + 1]


class SolutionBFS:
    def longestZigZag(self, root):
        res = 0
        queue = collections.deque()
        queue.append([root, 0, 0])
        while queue:
            node, left, right = queue.popleft()
            res = max(res, left, right)
            if node.left:
                queue.append([node.left, 0, left + 1])
            if node.right:
                queue.append([node.right, right + 1, 0])

        return res


