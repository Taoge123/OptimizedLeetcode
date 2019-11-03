
"""
Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]

"""


"""
Note that map(max, left, right) will behave differently under Python3, 
in that if left and right are not the same length, 
corresponding to different depths of the tree, 
max will produce a result with a length of the shorter of the two.
"""

import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode):

        if not root:
            return []
        queue = collections.deque([root])
        res = [root.val]
        while queue:
            nextLevel = collections.deque()
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
                if not queue and nextLevel:
                    res.append(max(i.val for i in nextLevel))
                    queue, nextLevel = nextLevel, queue

        return res





