"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:

            size, cur_level = len(queue), []
            for i in range(size):
                node = queue.popleft()
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)

        return res










