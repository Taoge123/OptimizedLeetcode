
"""
Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7

Doing BFS right-to-left means we can simply return the last node's value
and don't have to keep track of the first node in the current row
or even care about rows at all.
Inspired by @fallcreek's solution (not published) which uses two nested loops to go
row by row but already had the right-to-left idea making it easier.
I just took that further.

"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        deque = collections.deque([root])
        res=TreeNode(0)
        while deque:
            res=deque.popleft()
            if res.right:
                deque.append(res.right)
            if res.left:
                deque.append(res.left)
        return res.val


class Solution1:
    def findLeftMostNode(self, root):
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val


class Solution2:
    def findBottomLeftValue(self, root):
        self.ans = None
        self.level = -1
        self.helper(root, 0)
        return self.ans

    def helper(self, node, level):
        if not node:
            return
        if self.level < level:
            self.level = level
            self.ans = node.val
        self.helper(node.left, level + 1)
        self.helper(node.right, level + 1)


