

"""
You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""

import collections

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):

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


root = TreeNode(0)

a = Solution()
print(a.largestValues(root))



