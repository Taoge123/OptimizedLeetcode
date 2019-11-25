"""
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def levelOrderBottom(self, root):

        if not root:
            return []

        res = deque()
        queue = deque([root])

        while queue:
            size, cur_level = len(queue), []

            for i in range(size):
                node = queue.popleft()
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.appendleft(cur_level)

        return res

class Solution:
    def levelOrderBottom(self, root):
        res = deque()
        if not root:
            return res
        self.dfs(root, res, 0)
        return res

    def dfs(self, root, res, level):
        if not root:
            return None

        if len(res) <= level:
            res.appendleft([])

        res[len(res) - 1 - level].append(root.val)
        self.dfs(root.left, res, level + 1)
        self.dfs(root.right, res, level + 1)







